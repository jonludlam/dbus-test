open Idl
    
type exn =
  | Unimplemented of string
  [@@deriving rpc]

type query_result = {
  plugin : string [@doc "plugin name, used in the XenAPI as SR.type"];
  name : string [@doc "short name"] [@key "name"];
  description : string [@doc "description"] [@key "description"];
  vendor : string [@doc "entity (e.g. company, project, group) which produced this implementation"];
  copyright : string [@doc "copyright"];
  version : string [@doc "version"];
  required_api_version : string [@doc "minimum required API version"];
  features : string list [@doc "features supported by this plugin"];
  configuration : (string * string) list [@doc "key/description pairs describing required device_config parameters"];
  required_cluster_stack : string list [@doc "the plugin requires one of these cluster stacks to be active"];
} [@@deriving rpc] [@@doc "properties of this implementation"]

type srs = string list [@@deriving rpc]

let dbg = Param.mk ~name:"dbg" ~description:"Debug context from the caller" Types.string
    
module Plugin(R : RPC) = struct
  open R
      
  let interface = R.describe
      {Idl.Interface.name = "Plugin";
       description="Discover properties of this implementation. Every implementation  must support the query interface or it will not be recognised as  a storage plugin by xapi.";
       version=1}
      
  let unit = Param.mk Types.unit
  let query_result = Param.mk query_result_def
  let query = declare "query"
      "Query this implementation and return its properties. This is  called by xapi to determine whether it is compatible with xapi  and to discover the supported features."
      (unit @-> returning query_result)

  let srs = Param.mk ~name:"srs" ~description:"The attached SRs" srs_def

  let ls = declare "ls"
      "[ls dbg]: returns a list of attached SRs"
      (unit @-> returning srs)

  let diagnostics_p = Param.mk ~name:"diagnostics" ~description:"A string containing loggable human-readable diagnostics information" Types.string
  let diagnostics = declare "diagnostics"
      "Returns a printable set of backend diagnostic information. Implementations are encouraged to include any data which will  be useful to diagnose problems. Note this data should not  include personally-identifiable data as it is intended to be  automatically included in bug reports."
      (unit @-> returning diagnostics_p)

end


module Code=Plugin(Codegen)
    
let interfaces =
  let interface = Code.(interface
                        |> query
                        |> ls
                        |> diagnostics) in

  let interfaces = Codegen.Interfaces.empty
      "plugin"
      "The Datapath plugin interface"
      "The Datapath plugin takes a URI which points to virtual disk data and chooses a Xen datapath implementation: driver domain, blkback implementation and caching strategy."
  in

  let interface = Codegen.Interface.prepend_arg interface dbg in
  let interfaces = Codegen.Interfaces.add_interface interfaces interface in
  let interfaces = Codegen.Interfaces.register_exn interfaces exn_def in

  interfaces


  

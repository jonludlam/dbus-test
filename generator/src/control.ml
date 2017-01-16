open Rpc
open Idl
open Common

type exns =
  | Sr_not_attached of string
        [@doc ["An SR must be attached in order to access volumes"]]
  | SR_does_not_exist of string
        [@doc ["The specified SR could not be found"]]
  | Volume_does_not_exist of string
        [@doc ["The specified volume could not be found in the SR"]]
  | Unimplemented of string
        [@doc ["The operation has not been implemented"]]
  | Cancelled of string
        [@doc ["The operation has not been implemented"]]
[@@deriving rpcty]

exception Sr_error of exns

let errors = Error.{
    def = exns;
    raiser = (fun e -> Sr_error e);
    matcher = (function | Sr_error e -> Some e | _ -> None);
  }

type health =
  | Healthy of string
        [@doc ["Storage is fully available"]]
  | Recovering of string
        [@doc ["Storage is busy recovering, e.g. rebuilding mirrors"]]
[@@deriving rpcty]

type sr = string [@@deriving rpcty] [@@doc
  ["Primary key for a specific Storage Repository. This can be any string ";
   "which is meaningful to the implementation. For example this could be an ";
   "NFS directory name, an LVM VG name or even a URI. This string is ";
   "abstract."]]

type sr_stat = {
  sr: sr [@doc
      ["The URI identifying this volume. A typical value would be a file:// ";
       "URI pointing to a directory or block device" ]];

  name: string [@doc
      ["Short, human-readable label for the SR." ]];

  description: string [@doc
      ["Longer, human-readable description of the SR. Descriptions are ";
       "generally only displayed by clients when the user is examining SRs in ";
       "detail."]];

  free_space: int64 [@doc
      ["Number of bytes free on the backing storage (in bytes)"]];

  total_space: int64 [@doc
      ["Total physical size of the backing storage (in bytes)"]];

  datasources: string list [@doc
      ["URIs naming datasources: time-varying quantities representing ";
       "anything from disk access latency to free space. The entities named ";
       "by these URIs are self-describing."]];

  clustered: bool
      [@doc ["Indicates whether the SR uses clustered local storage."]];

  health: health
      [@doc ["The health status of the SR."]]
} [@@deriving rpcty]

type key = string [@@deriving rpcty] [@@doc
  ["Primary key for a volume. This can be any string which is meaningful to ";
   "the implementation. For example this could be an NFS filename, an LVM LV ";
   "name or even a URI. This string is abstract."]]

type volume = {
  key : key [@doc
      ["A primary key for this volume. The key must be unique within the ";
       "enclosing Storage Repository (SR). A typical value would be a ";
       "filename or an LVM volume name."]];

  uuid : string option [@doc
      ["A uuid (or guid) for the volume, if one is available. If a ";
       "storage system has a built-in notion of a guid, then it will be ";
       "returned here."]];

  name : string [@doc
      ["Short, human-readable label for the volume. Names are commonly used ";
       "by when displaying short lists of volumes."]];

  description : string [@doc
      ["Longer, human-readable description of the volume. Descriptions are ";
       "generally only displayed by clients when the user is examining ";
       "volumes individually."]];

  read_write : bool [@doc
      ["True means the VDI may be written to, false means the volume is ";
       "read-only. Some storage media is read-only so all volumes are ";
       "read-only; for example .iso disk images on an NFS share. Some volume ";
       "are created read-only; for example because they are snapshots of some ";
       "other VDI."]];

  virtual_size : int64 [@doc
      ["Size of the volume from the perspective of a VM (in bytes)"]];

  physical_utilisation : int64 [@doc
      ["Amount of space currently used on the backing storage (in bytes)"]];

  uri : string list [@doc
      ["A list of URIs which can be opened and used for I/O. A URI could ";
       "reference a local block device, a remote NFS share, iSCSI LUN or RBD ";
       "volume. In cases where the data may be accessed over several ";
       "protocols, he list should be sorted into descending order of ";
       "desirability. Xapi will open the most desirable URI for which it has ";
       "an available datapath plugin."]];

  keys : (string * string) list [@doc
      ["A list of key=value pairs which have been stored in the Volume ";
      "metadata. These should not be interpreted by the Volume plugin."]]
} [@@deriving rpcty]


let sr = Param.mk ~name:"sr" ~description:["The Storage Repository"]
    Types.string


module Volume(R: RPC) = struct
  open R

  let key = Param.mk ~name:"key" ~description:["The volume key"] key

  let uri = Param.mk ~name:"uri" ~description:["The Storage Repository URI"]
      Types.string

  let name = Param.mk ~name:"name" ~description:
      ["A human-readable name to associate with the new disk. This name is ";
       "intended to be short, to be a good summary of the disk."]
      Types.string

  let description = Param.mk ~name:"description" ~description:
      ["A human-readable description to associate with the new disk. This can ";
       "be arbitrarily long, up to the general string size limit."]
      Types.string

  let size = Param.mk ~name:"size" ~description:
      ["A minimum size (in bytes) for the disk. Depending on the ";
       "characteristics of the implementation this may be rounded up to ";
       "(for example) the nearest convenient block size. The created disk ";
       "will not be smaller than this size."]
      Types.int64

  let volume = Param.mk ~name:"volume" ~description:
      ["Properties of the volume"] volume

  let interface = R.describe
      {Idl.Interface.name = "Volume";
       description=["Operations which operate on volumes (also known as ";
                    "Virtual Disk Images)"];
       version=(1,0,0)}

  let create = R.declare "create"
      ["[create sr name description size] creates a new volume in [sr] with ";
       "[name] and [description]. The volume will have size >= [size] i.e. it ";
       "is always permissable for an implementation to round-up the volume to ";
       "the nearest convenient block size"]
      (sr @-> name @-> description @-> size @-> returning volume errors)

  let snapshot = R.declare "snapshot"
      ["[snapshot sr volume] creates a new volue which is a  snapshot of ";
       "[volume] in [sr]. Snapshots should never be written to; they are ";
       "intended for backup/restore only. Note the name and description are ";
       "copied but any extra metadata associated by [set] is not copied."]
      (sr @-> key @-> returning volume errors)

  let clone = R.declare "clone"
      ["[clone sr volume] creates a new volume which is a writable clone of ";
       "[volume] in [sr]. Note the name and description are copied but any ";
       "extra metadata associated by [set] is not copied."]
      (sr @-> key @-> returning volume errors)

  let destroy = R.declare "destroy"
      ["[destroy sr volume] removes [volume] from [sr]"]
      (sr @-> key @-> returning unit errors)

  let new_name = Param.mk ~name:"new_name" ~description:["New name"]
      Types.string

  let set_name = R.declare "set_name"
      ["[set_name sr volume new_name] changes the name of [volume]"]
      (sr @-> key @-> new_name @-> returning unit errors)

  let new_description = Param.mk ~name:"new_description"
      ~description:["New description"] Types.string

  let set_description = R.declare "set_description"
      ["[set_description sr volume new_description] changes the description ";
       "of [volume]"]
      (sr @-> key @-> new_description @-> returning unit errors)

  let k = Param.mk ~name:"k" ~description:["Key"] Types.string
  let v = Param.mk ~name:"v" ~description:["Value"] Types.string
  let set = R.declare "set"
      ["[set sr volume key value] associates [key] with [value] in the ";
       "metadata of [volume] Note these keys and values are not interpreted ";
       "by the plugin; they are intended for the higher-level software only."]
      (sr @-> key @-> k @-> v @-> returning unit errors)

  let unset = R.declare "unset"
      ["[unset sr volume key] removes [key] and any value associated with it ";
       "from the metadata of [volume] Note these keys and values are not ";
       "interpreted by the plugin; they are intended for the higher-level ";
       "software only."]
      (sr @-> key @-> k @-> returning unit errors)

  let new_size = Param.mk ~name:"new_size" ~description:["New disk size"]
      Types.int64
  let resize = R.declare "resize"
      ["[resize sr volume new_size] enlarges [volume] to be at least ";
       "[new_size]."]
      (sr @-> key @-> new_size @-> returning unit errors)

  let stat = R.declare "stat"
      ["[stat sr volume] returns metadata associated with [volume]."]
      (sr @-> key @-> returning volume errors)

  let key2 = {key with Param.name="key2"}
  let blocklist_result = Param.mk blocklist
  let compare = R.declare "compare"
      ["[compare sr volume1 volume2] compares the two volumes and returns a ";
       "result of type blocklist that describes the differences between the ";
       "two volumes. If the two volumes are unrelated, or the second volume ";
       "does not exist, the result will be a list of the blocks that are ";
       "non-empty in volume1. If this information is not available to the ";
       "plugin, it should return a result indicating that all blocks are in ";
       "use."]
      (sr @-> key @-> key2 @-> returning blocklist_result errors)
end

type probe_result = {
  srs : sr_stat list [@doc ["SRs found on this storage device"]];
  uris : uri list [@doc ["Other possible URIs which may contain SRs"]];
} [@@deriving rpcty]

module Sr(R : RPC) = struct
  open R

  let interface = R.describe
      {Idl.Interface.name = "SR";
       description=["Operations which act on Storage Repositories"];
       version=(1,0,0)}

  let uri = Param.mk ~name:"uri" ~description:["The Storage Repository URI"]
      Types.string

  let probe_result_p = Param.mk ~name:"result"
      ~description:["Contents of the storage device"] probe_result

  let probe = R.declare "probe"
      ["[probe uri]: looks for existing SRs on the storage device"]
      (uri @-> returning probe_result_p errors)


  let name = Param.mk ~name:"name" ~description:
      ["Human-readable name for the SR"] Types.string
  let description = Param.mk ~name:"description" ~description:
      ["Human-readable description for the SR"] Types.string
  let configuration = Param.mk ~name:"configuration"
      Types.{
        name = "configuration";
        description =
          ["Plugin-specific configuration which describes where and how to ";
           "create the storage repository. This may include the physical ";
           "block device name, a remote NFS server and path or an RBD storage ";
           "pool."];
       ty = Dict(String, Basic String)}
  let create = R.declare "create"
      ["[create uri name description configuration]: creates a fresh SR"]
      (uri @-> name @-> description @-> configuration @-> returning unit errors)

  let attach = R.declare "attach"
      ["[attach uri]: attaches the SR to the local host. Once an SR is ";
       "attached then volumes may be manipulated."]
      (uri @-> returning sr errors)

  let detach = R.declare "detach"
      ["[detach sr]: detaches the SR, clearing up any associated resources. ";
       "Once the SR is detached then volumes may not be manipulated."]
      (sr @-> returning unit errors)

  let destroy = R.declare "destroy"
      ["[destroy sr]: destroys the [sr] and deletes any volumes associated ";
       "with it. Note that an SR must be attached to be destroyed; otherwise ";
       "Sr_not_attached is thrown."]
      (sr @-> returning unit errors)

  let stat_result = Param.mk ~name:"sr" ~description:["SR metadata"] sr_stat
  let stat = R.declare "stat"
      ["[stat sr] returns summary metadata associated with [sr]. Note this ";
       "call does not return details of sub-volumes, see SR.ls."]
      (sr @-> returning stat_result errors)

  let new_name = Param.mk ~name:"new_name"
      ~description:["The new name of the SR"]
      Types.string
  let set_name = R.declare "set_name"
      ["[set_name sr new_name] changes the name of [sr]"]
      (sr @-> new_name @-> returning unit errors)

  let new_description = Param.mk ~name:"new_description"
      ~description:["The new description for the SR"]
      Types.string
  let set_description = R.declare "set_description"
      ["[set_description sr new_description] changes the description of [sr]"]
      (sr @-> new_description @-> returning unit errors)

  let volumes = Param.mk ~name:"volumes"
      Types.{name="volumes";
             description=["A list of volumes"];
             ty=Array (typ_of_volume)}

  let ls = R.declare "ls"
      ["[ls sr] returns a list of volumes contained within an attached SR."]
      (sr @-> returning volumes errors)
end

module VolumeCode = Codegen.Gen ()
module V = Volume(VolumeCode)
module SrCode = Codegen.Gen ()
module S=Sr(SrCode)

let interfaces =
  let interfaces = Codegen.Interfaces.empty
      "volume"
      "The Volume plugin interface"
      ["The xapi toolstack delegates all storage control-plane functions to ";
       "\"Volume plugins\".These plugins allow the toolstack to ";
       "create/destroy/snapshot/clone volumes which are organised into groups ";
       "called Storage Repositories (SR). Volumes have a set of URIs which ";
       "can be used by the \"Datapath plugins\" to connect the disk data to ";
       "VMs."]
  in

  let vinterface = Codegen.Interface.prepend_arg (VolumeCode.get_interface ()) dbg in

  let sinterface = Codegen.Interface.prepend_arg (SrCode.get_interface ()) dbg in

  let interfaces = Codegen.Interfaces.add_interface sinterface interfaces in
  let interfaces = Codegen.Interfaces.add_interface vinterface interfaces in

  interfaces

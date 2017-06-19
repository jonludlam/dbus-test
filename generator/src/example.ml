open Rpc
open Idl

(**** New type definitions ****)

(* New types, for example structures or variant types, or even just aliases
   for existing standard types, can be declared here. Use
   standard ocaml syntax with the "[@@deriving rpcty]" extension *)

type new_struct = {
  name : string;
  size : int;
} [@@deriving rpcty]



type new_variant =
  | VariantOne of new_struct
  | VariantTwo of string
[@@deriving rpcty]



type alias = string
[@@deriving rpcty]







(* Although that is strictly all that's required to use these types
   in RPCs, it is strongly recommended that any new type definitions
   are well documentated. These documentation strings go into the
   generated markdown description and the python code. 

   Note that fields and individual variant tags are documented by
   using a single '@' character, whereas the whole type is documented
   using double '@@' characters. *)

type documented_struct = {
  doc_name : string [@doc ["Documentation goes here."]];
  
  doc_size : int [@doc
      ["This integer is for measuring the size of things.";
       "It comes with a slightly longer documentation string ";
       "that help to demonstrate that documentation is done in ";
       "lists."]];
}
[@@doc [
  "Here is where we put the documentation for the ";
  "entire structure." ]]
[@@deriving rpcty]




type mytype = string [@@doc
  ["This type is a string, but we can call it something else ";
   "to help clarify the interface"]]
[@@deriving rpcty]




(***** Error declarations *************)

(* Again, not stricly necessary, since there is a generic error type
   already defined. However, we strongly encourage specific 
   actionable errors to be declared as part of the interface to
   help the layer above to respond appropriately to failures. *)

(* The suggestion is to use a variant type for the errors: *)

type myerror =
  | ThisHappened of string [@doc
        ["If a thing went wrong, this error will be returned with ";
         "argument describing the problem"]]
  | ThatHappened of int [@doc
        ["If a thing went wrong more than once, this error will ";
         "be returned with argument counting the number of times ";
         "it failed"]]
  | Unimplemented [@doc ["The requested method is unimplemented"]]
[@@doc
  ["If it all went horribly wrong, an error of this type will ";
   "be returned."]]
[@@deriving rpcty]


(* This is some annoying boilerplate that's necessary for use
   of exceptions for these errors in the OCaml code. I'd like
   to autogenerate this as part of the ppx at some point, but
   for now we need to declare an exception and an Error.t. 
   It's only used in the OCaml code, but it's necessary even
   if it's just python code being generated, as the type
   is part of the RPC declarations below. *)
exception MyError of myerror
let error = Error.{
    def = myerror;
    raiser = (function e -> MyError e);
    matcher = (function | MyError e -> Some e | _ -> None)
  }







(***** Parameter definitions ********)

(* Parameterss are declared here. They are named and used for both 
   input and output, and have type Param.t. These parameters
   are constructed out of types, either the generic types or any
   new types declared above.

   Common parameters (e.g. 'dbg') can be declared ahead of time and
   used in several RPC declarations. Parameters that are used for a
   single RPC could be declared next to the RPC declaration itself.

   The types used here are either the types declared above, or
   there are some common types declared in the 'Types' module.
   These are:

       Types.int
       Types.int32
       Types.int64
       Types.bool
       Types.float
       Types.string
       Types.char
       Types.unit -- useful as a return type.
*)

let debug = Param.mk ~name:"debug" ~description:
    ["A common debug parameter that all RPCs take"]
    Types.string

let unit = Param.mk ~name:"unit" ~description:
    ["An RPC that is called for side-effect and doesn't ";
     "explicitly return a value can use this value as ";
     "a return parameter."]
    Types.unit

let name = Param.mk ~name:"name" ~description:
    ["The name of a thing"]
    Types.string

let str = Param.mk ~name:"struct" ~description:
    ["This demonstrates use of a new type declared above"]
    documented_struct






(****** ACTUAL RPC DECLARATIONS *************)
    
(* This is where the actual RPCs are declared. They are grouped
   together into individual interfaces, and then these are 
   grouped into a single 'interfaces' type

*)
    
module NewInterface (R : RPC) = struct
  open R
  (* Here we declare a new RPC method. This is done via
     declare [rpcname] [description] [type] where the 
     wire-name of the API call is formed by concatenating
     the interface name described above with [rpcname].
     The [type] parameter is constructed out of the 
     parameter definitions we've already made.
     
     the return parameters are formed out of the expected
     return parameter (unit, in this case, declared above),
     and the error type (again, declared above).
  *)
  let newrpc = declare "newrpc"
      ["This is the description of the new RPC"]
      (str @-> name @-> returning unit error)

  (* We must write a little documentation for the interface, with
     name, description and version. This _MUST_ be after all of 
     the RPC declarations. *)
  let implementation = implement
      Idl.Interface.{
        name = "NewInterface";
        namespace = Some "NewInterface";
        description = ["Here we describe the new interface."];
        version=(1,0,0)}
end



(* To use this declared interface to generate python code,
   there's a bit more documentation required *)

module Code = NewInterface(Codegen.Gen ())

let interfaces = Codegen.Interfaces.create
    ~name:"example"
    ~title:"The example interfaces"
    ~description:[
      "This code serves as an example for how to add a new ";
      "set of interfaces to the xapi-storage code"]
    ~interfaces:[Code.implementation ()]

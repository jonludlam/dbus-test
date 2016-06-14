(* Tasks API *)

open Idl

type exn =
  | Unimplemented of string
  [@@deriving rpc]

type error_t = string [@@deriving rpc]
type id = string [@@deriving rpc] [@@doc "Unique identifier for a task"]
type task_list = id list [@@deriving rpc]

type async_result_t =
  | Volume of Control.volume
  | Mirror of string (* Mirror.id *)
  [@@deriving rpc]
  
type completion_t = {
  duration : float;
  result : async_result_t option
} [@@deriving rpc]

type state =
  | Pending of float [@doc "the task is in progress, with progress info from 0..1"]
  | Completed of completion_t
  | Failed of error_t
  [@@deriving rpc]

type task = {
  id : id;
  debug_info : string;
  ctime : float;
  state : state;
} [@@deriving rpc]

let unit = Param.mk Types.unit
let dbg = Param.mk ~name:"dbg" ~description:"Debug context from the caller" Types.string
    
module Task(R : RPC) = struct
  open R
      
  let interface = R.describe {
      Idl.Interface.name = "task";
      description = "The task interface is for querying the status of asynchronous tasks. All long-running
        operations are associated with tasks, including copying and mirroring of data.";
      version=1}

  let task = Param.mk id_def
  let result = Param.mk ~name:"result" task_def
  let stat = R.declare "stat"
      "[stat task_id] returns the status of the task"
      (task @-> returning result)

  let cancel = R.declare "cancel"
      "[cancel task_id] performs a best-effort cancellation of an ongoing task. The effect of this should leave the system in one of two states: Either that the task has completed successfully, or that it had never been made at all. The call should return immediately and the status of the task can the be queried via the [stat] call."
      (task @-> returning unit)

  let destroy = R.declare "destroy"
      "[destroy task_id] should remove all traces of the task_id. This call should fail if the task is currently in progress."
      (task @-> returning unit)

  let task_list = Param.mk task_list_def
  let list = R.declare "list"
      "[list] should return a list of all of the tasks the plugin is aware of"
      (unit @-> returning task_list)
end

module Code=Task(Codegen)

let interfaces =
  let interface = Code.(interface
                        |> stat
                        |> cancel
                        |> destroy
                        |> list
                       ) in

  let interfaces = Codegen.Interfaces.empty
      "task"
      "The Task interface"
      "The Task interface is required if the backend supports long-running tasks."
  in

  let interface = Codegen.Interface.prepend_arg interface dbg in
  let interfaces = Codegen.Interfaces.add_interface interfaces interface in
  let interfaces = Codegen.Interfaces.register_exn interfaces exn_def in
  interfaces


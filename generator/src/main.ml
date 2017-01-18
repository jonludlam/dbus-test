open Rpc
open Codegen
open Files
    
let gen_html apis =
  Www.write apis

let _ =
  let generate_html = ref false in
  Arg.parse [
    "-html", Arg.Set generate_html, "Output HTML docs";
  ] (fun x -> Printf.fprintf stderr "Unknown argument: %s\n%!" x; exit 1)
  "Generate OCaml/Python/HTML documentation";

  let open Types in
  let open Files in
  let apis = [
    Plugin.interfaces;
    Control.interfaces;
    Data.interfaces;
    Task.interfaces;
    Example.interfaces;
  ] in

  if !generate_html
  then gen_html apis;

  List.iter
    (fun api ->
       with_output_file (Printf.sprintf "python/xapi/storage/api/%s.py" api.Interfaces.name)
         (fun oc ->
            let p = Pythongen.of_interfaces api |> Pythongen.string_of_ts in
            output_string oc p
         )
    ) apis

open Codegen
open Cow.Html
open Files

type page = {
  name: string;
  title: string;
  filename: string;
  path: string;
  description: string;
  api: Codegen.Interfaces.t;
}

let topbar pages =
  let link_of_page page =
    let html = page.name ^ ".html" in
    let name = page.name in
    li (a ~href:(Uri.of_string html) (string name))
  in
  list [ div ~cls:"title-bar" ~attrs:["data-responsive-toggle","main-menu"; "data-hide-for","medium"]
      (list [
          tag "button" ~cls:"menu-icon" ~attrs:["type","button"; "data-toggle",""] (string "");
          div ~cls:"title-bar-title" (string "Menu");
        ]);
    div ~cls:"top-bar" ~id:"main-menu"
      (list [
          div ~cls:"top-bar-left"
            (list [
                tag "ul" ~cls:"menu" ~attrs:["data-dropdown-menu",""]
                  (li ~cls:"menu-text" (string "SMAPIv3"))
              ]);
          div ~cls:"top-bar-right"
            (tag "ul" ~cls:"menu" ~attrs:["data-responsive-menu","drilldown medium-dropdown"]
               (list [
                   li ~cls:"has-submenu"
                     (list [
                         a ~href:(Uri.of_string "features.html") (string "Learn");
                         tag "ul" ~cls:"submenu menu vertical" ~attrs:["data-submenu",""]
                           (list [
                               li (a ~href:(Uri.of_string "features.html") (string "Features"));
                               li (a ~href:(Uri.of_string "concepts.html") (string "Concepts"));
                               li (a ~href:(Uri.of_string "architecture.html") (string "Architecture"));
                               li (a ~href:(Uri.of_string "faq.html") (string "FAQ"));
                             ])
                       ]);
                   li (list [
                       a ~href:(Uri.of_string "#") (string "Develop");
                       tag "ul" ~cls:"submenu menu vertical" ~attrs:["data-submenu",""]
                         (list (List.map link_of_page pages))
                     ]);
                   li (list [
                       a ~href:(Uri.of_string "#") (string "Support");
                       tag "ul" ~cls:"submenu menu vertical" ~attrs:["data-submenu",""]
                         (list [
                             li (a ~href:(Uri.of_string "contact.html") (string "Mailing list"));
                             li (a ~href:(Uri.of_string "contact.html") (string "Issue tracker"));
                             li (a ~href:(Uri.of_string "contact.html") (string "IRC"));
                           ])
                     ]);
                   li ~cls:"active" (a ~href:(Uri.of_string "getstarted.html") (string "Get Started"));
                 ])
            )
        ])
  ]

let index_html oc pages =
  let header =
    tag "header"
      (list [
          div ~cls:"row" (
            div ~cls:"large-12 columns"
              (list [
                  h1 (string "Xapi storage interface");
                  h3 ~cls:"subheader"
                    (list [ string "An easy way to connect ";
                            a ~href:(Uri.of_string "http://www.xenproject.org/developers/teams/xapi.html") (string "Xapi");
                            string " to any storage type";
                          ]);
                  tag "hr" (string "");
                  h2 (string "Who is this for?");
                  p (string "This is for anyone who has a storage system which is not supported by xapi out-of-the-box.");
                ]);
          );
          div ~cls:"row" (list [
              div ~cls:"large-6 columns"
                (img ~alt:"Your bit here" (Uri.of_string "img/your-bit-here.svg"));
              div ~cls:"large-6 columns"
                (list [
                    p (list [
                        string "This is also for anyone who wants to manage their storage in a customized way. If you can make your volumes appear as Linux block devices ";
                        tag "i" (string "or");
                        string "you can refer to the volumes via URIs of the form ";
                        tag "tt" (string "iscsi://");
                        tag "tt" (string "nfs://");
                        string "or";
                        tag "tt" (string "rbd://");
                        string "then this documentation is for you.";]);
                    p (tag "b" (string "No Xapi or Xen specific knowledge is required."))]);
            ]);
          div ~cls:"row"
            (div ~cls:"large-12 columns panel callout"
               (list [
                   h2 (string "Status of this documentation");
                   p (string "This documentation is a draft intended for discussion only. Please:");
                   tag "ul" (list [
                       li (list [
                           string "view the";
                           a ~href:(Uri.of_string "https://github.com/djs55/xapi-storage/issues") (string "issues on github");
                           string "or"]);
                       li (list [
                           string "join the";
                           a ~href:(Uri.of_string "https://lists.xenproject.org/mailman/listinfo/xen-api") (string "mailing list");
                         ])
                     ])
                 ])
            )
        ])
  in
  print_file_to oc ("doc/static/header.html");
  output_string oc (Cow.Html.to_string (topbar pages));
  output_string oc (Cow.Html.to_string header);
  print_file_to oc ("doc/static/footer.html")

let placeholder_html oc pages body =
  let header =
    div ~cls:"row" (div ~cls:"large-12 columns panel callout" (p (string "This is a placeholder")))
  in
  print_file_to oc ("doc/static/header.html");
  output_string oc (Cow.Html.to_string (topbar pages));
  if Sys.file_exists body
  then print_file_to oc body
  else output_string oc (Cow.Html.to_string header);
  print_file_to oc ("doc/static/footer.html")

let page_of_api api = {
  name = api.Codegen.Interfaces.name;
  title = api.Interfaces.title;
  path = "doc/gen/" ^ api.Interfaces.name ^ ".md";
  filename = api.Interfaces.name ^ ".md";
  description = String.concat "" api.Interfaces.description;
  api = api;
}

let write apis =
  let pages = List.map page_of_api apis in

  List.iter
    (fun page ->
       with_output_file page.path
         (fun oc ->
            output_string oc (Markdowngen.to_string page.api);
         );
    ) pages;
  with_output_file "doc/index.html"
    (fun oc ->
       index_html oc pages
    );
  List.iter
    (fun placeholder ->
       let out_filename = Printf.sprintf "doc/gen/%s" placeholder in
       let in_filename = Printf.sprintf "doc/templates/%s.body" placeholder in
      with_output_file out_filename
        (fun oc ->
          placeholder_html oc pages in_filename
        )
    ) [
      "contact.html";
      "concepts.html";
      "getstarted.html";
      "features.html";
      "faq.html";
      "learn.html";
      "architecture.html";
    ]

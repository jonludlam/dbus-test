from xapi import *
import traceback
class Unimplemented(Rpc_light_failure):
    def __init__(self, arg_0):
        Rpc_light_failure.__init__(self, "Unimplemented", [ arg_0 ])
        if type(arg_0) <> type("") and type(arg_0) <> type(u""):
            raise (TypeError("string", repr(arg_0)))
        self.arg_0 = arg_0
class Task_server_dispatcher:
    """The task interface is for querying the status of asynchronous tasks. All long-running
        operations are associated with tasks, including copying and mirroring of data."""
    def __init__(self, impl):
        """impl is a proxy object whose methods contain the implementation"""
        self._impl = impl
    def stat(self, args):
        """type-check inputs, call implementation, type-check outputs and return"""
        if type(args) <> type({}):
            raise (UnmarshalException('arguments', 'dict', repr(args)))
        if not(args.has_key('dbg')):
            raise UnmarshalException('argument missing', 'dbg', '')
        dbg = args["dbg"]
        if type(dbg) <> type("") and type(dbg) <> type(u""):
            raise (TypeError("string", repr(dbg)))
        if not(args.has_key('id')):
            raise UnmarshalException('argument missing', 'id', '')
        id = args["id"]
        if type(id) <> type("") and type(id) <> type(u""):
            raise (TypeError("string", repr(id)))
        results = self._impl.stat(dbg, id)
        if type(results['id']) <> type("") and type(results['id']) <> type(u""):
            raise (TypeError("string", repr(results['id'])))
        if type(results['debug_info']) <> type("") and type(results['debug_info']) <> type(u""):
            raise (TypeError("string", repr(results['debug_info'])))
        if type(results['ctime']) <> type(1.1):
            raise (TypeError("float", repr(results['ctime'])))
        if results['state'][0] not in ["Pending","Completed","Failed"]:
            raise (TypeError("| Pending (float) (** the task is in progress, with progress info from 0..1 *) | Completed ({ duration: float; result: | Unit (unit) (**  *) | Volume ({ key: string; uuid: string option; name: string; description: string; read_write: bool; virtual_size: int64; physical_utilisation: int64; uri: string list; keys: (string * string) list; }) (**  *) option; }) (**  *) | Failed (string) (**  *)", repr(results['state'])))
        if results['state'][0] == 'Pending':
            if type(results['state'][1]) <> type(1.1):
                raise (TypeError("float", repr(results['state'][1])))
        elif results['state'][0] == 'Completed':
            if type(results['state'][1]['duration']) <> type(1.1):
                raise (TypeError("float", repr(results['state'][1]['duration'])))
            if results['state'][1]['result'] <> None:
                if results['state'][1]['result'][0] not in ["Unit","Volume"]:
                    raise (TypeError("| Unit (unit) (**  *) | Volume ({ key: string; uuid: string option; name: string; description: string; read_write: bool; virtual_size: int64; physical_utilisation: int64; uri: string list; keys: (string * string) list; }) (**  *)", repr(results['state'][1]['result'])))
                if results['state'][1]['result'][0] == 'Volume':
                    if type(results['state'][1]['result'][1]['key']) <> type("") and type(results['state'][1]['result'][1]['key']) <> type(u""):
                        raise (TypeError("string", repr(results['state'][1]['result'][1]['key'])))
                    if results['state'][1]['result'][1]['uuid'] <> None:
                        if type(results['state'][1]['result'][1]['uuid']) <> type("") and type(results['state'][1]['result'][1]['uuid']) <> type(u""):
                            raise (TypeError("string", repr(results['state'][1]['result'][1]['uuid'])))
                    if type(results['state'][1]['result'][1]['name']) <> type("") and type(results['state'][1]['result'][1]['name']) <> type(u""):
                        raise (TypeError("string", repr(results['state'][1]['result'][1]['name'])))
                    if type(results['state'][1]['result'][1]['description']) <> type("") and type(results['state'][1]['result'][1]['description']) <> type(u""):
                        raise (TypeError("string", repr(results['state'][1]['result'][1]['description'])))
                    if type(results['state'][1]['result'][1]['read_write']) <> type(True):
                        raise (TypeError("bool", repr(results['state'][1]['result'][1]['read_write'])))
                    if not(is_long(results['state'][1]['result'][1]['virtual_size'])):
                        raise (TypeError("int64", repr(results['state'][1]['result'][1]['virtual_size'])))
                    if not(is_long(results['state'][1]['result'][1]['physical_utilisation'])):
                        raise (TypeError("int64", repr(results['state'][1]['result'][1]['physical_utilisation'])))
                    if type(results['state'][1]['result'][1]['uri']) <> type([]):
                        raise (TypeError("string list", repr(results['state'][1]['result'][1]['uri'])))
                    for tmp_30 in results['state'][1]['result'][1]['uri']:
                        if type(tmp_30) <> type("") and type(tmp_30) <> type(u""):
                            raise (TypeError("string", repr(tmp_30)))
                    if type(results['state'][1]['result'][1]['keys']) <> type({}):
                        raise (TypeError("(string * string) list", repr(results['state'][1]['result'][1]['keys'])))
                    for tmp_29 in results['state'][1]['result'][1]['keys'].keys():
                        if type(tmp_29) <> type("") and type(tmp_29) <> type(u""):
                            raise (TypeError("string", repr(tmp_29)))
                    for tmp_29 in results['state'][1]['result'][1]['keys'].values():
                        if type(tmp_29) <> type("") and type(tmp_29) <> type(u""):
                            raise (TypeError("string", repr(tmp_29)))
        elif results['state'][0] == 'Failed':
            if type(results['state'][1]) <> type("") and type(results['state'][1]) <> type(u""):
                raise (TypeError("string", repr(results['state'][1])))
        return results
    def cancel(self, args):
        """type-check inputs, call implementation, type-check outputs and return"""
        if type(args) <> type({}):
            raise (UnmarshalException('arguments', 'dict', repr(args)))
        if not(args.has_key('dbg')):
            raise UnmarshalException('argument missing', 'dbg', '')
        dbg = args["dbg"]
        if type(dbg) <> type("") and type(dbg) <> type(u""):
            raise (TypeError("string", repr(dbg)))
        if not(args.has_key('id')):
            raise UnmarshalException('argument missing', 'id', '')
        id = args["id"]
        if type(id) <> type("") and type(id) <> type(u""):
            raise (TypeError("string", repr(id)))
        results = self._impl.cancel(dbg, id)
        return results
    def destroy(self, args):
        """type-check inputs, call implementation, type-check outputs and return"""
        if type(args) <> type({}):
            raise (UnmarshalException('arguments', 'dict', repr(args)))
        if not(args.has_key('dbg')):
            raise UnmarshalException('argument missing', 'dbg', '')
        dbg = args["dbg"]
        if type(dbg) <> type("") and type(dbg) <> type(u""):
            raise (TypeError("string", repr(dbg)))
        if not(args.has_key('id')):
            raise UnmarshalException('argument missing', 'id', '')
        id = args["id"]
        if type(id) <> type("") and type(id) <> type(u""):
            raise (TypeError("string", repr(id)))
        results = self._impl.destroy(dbg, id)
        return results
    def ls(self, args):
        """type-check inputs, call implementation, type-check outputs and return"""
        if type(args) <> type({}):
            raise (UnmarshalException('arguments', 'dict', repr(args)))
        if not(args.has_key('dbg')):
            raise UnmarshalException('argument missing', 'dbg', '')
        dbg = args["dbg"]
        if type(dbg) <> type("") and type(dbg) <> type(u""):
            raise (TypeError("string", repr(dbg)))
        results = self._impl.ls(dbg)
        if type(results) <> type([]):
            raise (TypeError("string list", repr(results)))
        for tmp_31 in results:
            if type(tmp_31) <> type("") and type(tmp_31) <> type(u""):
                raise (TypeError("string", repr(tmp_31)))
        return results
    def _dispatch(self, method, params):
        """type check inputs, call implementation, type check outputs and return"""
        args = params[0]
        if method == "Task.stat":
            return success(self.stat(args))
        elif method == "Task.cancel":
            return success(self.cancel(args))
        elif method == "Task.destroy":
            return success(self.destroy(args))
        elif method == "Task.ls":
            return success(self.ls(args))
class Task_skeleton:
    """The task interface is for querying the status of asynchronous tasks. All long-running
        operations are associated with tasks, including copying and mirroring of data."""
    def __init__(self):
        pass
    def stat(self, dbg, id):
        """The task interface is for querying the status of asynchronous tasks. All long-running
        operations are associated with tasks, including copying and mirroring of data."""
        raise Unimplemented("Task.stat")
    def cancel(self, dbg, id):
        """The task interface is for querying the status of asynchronous tasks. All long-running
        operations are associated with tasks, including copying and mirroring of data."""
        raise Unimplemented("Task.cancel")
    def destroy(self, dbg, id):
        """The task interface is for querying the status of asynchronous tasks. All long-running
        operations are associated with tasks, including copying and mirroring of data."""
        raise Unimplemented("Task.destroy")
    def ls(self, dbg):
        """The task interface is for querying the status of asynchronous tasks. All long-running
        operations are associated with tasks, including copying and mirroring of data."""
        raise Unimplemented("Task.ls")
class Task_test:
    """The task interface is for querying the status of asynchronous tasks. All long-running
        operations are associated with tasks, including copying and mirroring of data."""
    def __init__(self):
        pass
    def stat(self, dbg, id):
        """The task interface is for querying the status of asynchronous tasks. All long-running
        operations are associated with tasks, including copying and mirroring of data."""
        result = {}
        result["result"] = { "id": "string", "debug_info": "string", "ctime": 1.1, "state": None }
        return result
    def cancel(self, dbg, id):
        """The task interface is for querying the status of asynchronous tasks. All long-running
        operations are associated with tasks, including copying and mirroring of data."""
        result = {}
        return result
    def destroy(self, dbg, id):
        """The task interface is for querying the status of asynchronous tasks. All long-running
        operations are associated with tasks, including copying and mirroring of data."""
        result = {}
        return result
    def ls(self, dbg):
        """The task interface is for querying the status of asynchronous tasks. All long-running
        operations are associated with tasks, including copying and mirroring of data."""
        result = {}
        result["task_list"] = [ "string", "string" ]
        return result
import argparse, traceback
import xapi
class Task_commandline():
    """Parse command-line arguments and call an implementation."""
    def __init__(self, impl):
        self.impl = impl
        self.dispatcher = Task_server_dispatcher(self.impl)
    def _parse_stat(self):
        """[stat task_id] returns the status of the task"""
        # in --json mode we don't have any other arguments
        if ('--json' in sys.argv or '-j' in sys.argv):
            jsondict = json.loads(sys.stdin.readline(),)
            jsondict['json'] = True
            return jsondict
        parser = argparse.ArgumentParser(description='[stat task_id] returns the status of the task')
        parser.add_argument('-j', '--json', action='store_const', const=True, default=False, help='Read json from stdin, print json to stdout', required=False)
        parser.add_argument('dbg', action='store', help='Debug context from the caller')
        parser.add_argument('id', action='store', help='Unique identifier for a task')
        return vars(parser.parse_args())
    def _parse_cancel(self):
        """[cancel task_id] performs a best-effort cancellation of an ongoing task. The effect of this should leave the system in one of two states: Either that the task has completed successfully, or that it had never been made at all. The call should return immediately and the status of the task can the be queried via the [stat] call."""
        # in --json mode we don't have any other arguments
        if ('--json' in sys.argv or '-j' in sys.argv):
            jsondict = json.loads(sys.stdin.readline(),)
            jsondict['json'] = True
            return jsondict
        parser = argparse.ArgumentParser(description='[cancel task_id] performs a best-effort cancellation of an ongoing task. The effect of this should leave the system in one of two states: Either that the task has completed successfully, or that it had never been made at all. The call should return immediately and the status of the task can the be queried via the [stat] call.')
        parser.add_argument('-j', '--json', action='store_const', const=True, default=False, help='Read json from stdin, print json to stdout', required=False)
        parser.add_argument('dbg', action='store', help='Debug context from the caller')
        parser.add_argument('id', action='store', help='Unique identifier for a task')
        return vars(parser.parse_args())
    def _parse_destroy(self):
        """[destroy task_id] should remove all traces of the task_id. This call should fail if the task is currently in progress."""
        # in --json mode we don't have any other arguments
        if ('--json' in sys.argv or '-j' in sys.argv):
            jsondict = json.loads(sys.stdin.readline(),)
            jsondict['json'] = True
            return jsondict
        parser = argparse.ArgumentParser(description='[destroy task_id] should remove all traces of the task_id. This call should fail if the task is currently in progress.')
        parser.add_argument('-j', '--json', action='store_const', const=True, default=False, help='Read json from stdin, print json to stdout', required=False)
        parser.add_argument('dbg', action='store', help='Debug context from the caller')
        parser.add_argument('id', action='store', help='Unique identifier for a task')
        return vars(parser.parse_args())
    def _parse_ls(self):
        """[ls] should return a list of all of the tasks the plugin is aware of"""
        # in --json mode we don't have any other arguments
        if ('--json' in sys.argv or '-j' in sys.argv):
            jsondict = json.loads(sys.stdin.readline(),)
            jsondict['json'] = True
            return jsondict
        parser = argparse.ArgumentParser(description='[ls] should return a list of all of the tasks the plugin is aware of')
        parser.add_argument('-j', '--json', action='store_const', const=True, default=False, help='Read json from stdin, print json to stdout', required=False)
        parser.add_argument('dbg', action='store', help='Debug context from the caller')
        return vars(parser.parse_args())
    def stat(self):
        use_json = False
        try:
            request = self._parse_stat()
            use_json = 'json' in request and request['json']
            results = self.dispatcher.stat(request)
            print json.dumps(results)
        except Exception, e:
            if use_json:
                xapi.handle_exception(e)
            else:
                traceback.print_exc()
                raise e
    def cancel(self):
        use_json = False
        try:
            request = self._parse_cancel()
            use_json = 'json' in request and request['json']
            results = self.dispatcher.cancel(request)
            print json.dumps(results)
        except Exception, e:
            if use_json:
                xapi.handle_exception(e)
            else:
                traceback.print_exc()
                raise e
    def destroy(self):
        use_json = False
        try:
            request = self._parse_destroy()
            use_json = 'json' in request and request['json']
            results = self.dispatcher.destroy(request)
            print json.dumps(results)
        except Exception, e:
            if use_json:
                xapi.handle_exception(e)
            else:
                traceback.print_exc()
                raise e
    def ls(self):
        use_json = False
        try:
            request = self._parse_ls()
            use_json = 'json' in request and request['json']
            results = self.dispatcher.ls(request)
            print json.dumps(results)
        except Exception, e:
            if use_json:
                xapi.handle_exception(e)
            else:
                traceback.print_exc()
                raise e
class task_server_dispatcher:
    """Demux calls to individual interface server_dispatchers"""
    def __init__(self, Task = None):
        self.Task = Task
    def _dispatch(self, method, params):
        try:
            log("method = %s params = %s" % (method, repr(params)))
            if method.startswith("Task") and self.Task:
                return self.Task._dispatch(method, params)
            raise UnknownMethod(method)
        except Exception, e:
            log("caught %s" % e)
            traceback.print_exc()
            try:
                # A declared (expected) failure will have a .failure() method
                log("returning %s" % (repr(e.failure())))
                return e.failure()
            except:
                # An undeclared (unexpected) failure is wrapped as InternalError
                return (InternalError(str(e)).failure())
class task_server_test(task_server_dispatcher):
    """Create a server which will respond to all calls, returning arbitrary values. This is intended as a marshal/unmarshal test."""
    def __init__(self):
        task_server_dispatcher.__init__(self, Task_server_dispatcher(Task_test()))
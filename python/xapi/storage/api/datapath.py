from xapi import *
import traceback
class Unimplemented(Rpc_light_failure):
    def __init__(self, arg_0):
        Rpc_light_failure.__init__(self, "Unimplemented", [ arg_0 ])
        if type(arg_0) <> type("") and type(arg_0) <> type(u""):
            raise (TypeError("string", repr(arg_0)))
        self.arg_0 = arg_0
class Data_server_dispatcher:
    """This interface is used for long-running data operations such as copying the contents of volumes or mirroring volumes to remote destinations"""
    def __init__(self, impl):
        """impl is a proxy object whose methods contain the implementation"""
        self._impl = impl
    def copy(self, args):
        """type-check inputs, call implementation, type-check outputs and return"""
        if type(args) <> type({}):
            raise (UnmarshalException('arguments', 'dict', repr(args)))
        if not(args.has_key('dbg')):
            raise UnmarshalException('argument missing', 'dbg', '')
        dbg = args["dbg"]
        if type(dbg) <> type("") and type(dbg) <> type(u""):
            raise (TypeError("string", repr(dbg)))
        if not(args.has_key('uri')):
            raise UnmarshalException('argument missing', 'uri', '')
        uri = args["uri"]
        if type(uri) <> type("") and type(uri) <> type(u""):
            raise (TypeError("string", repr(uri)))
        if not(args.has_key('domain')):
            raise UnmarshalException('argument missing', 'domain', '')
        domain = args["domain"]
        if type(domain) <> type("") and type(domain) <> type(u""):
            raise (TypeError("string", repr(domain)))
        if not(args.has_key('remote')):
            raise UnmarshalException('argument missing', 'remote', '')
        remote = args["remote"]
        if type(remote) <> type("") and type(remote) <> type(u""):
            raise (TypeError("string", repr(remote)))
        if not(args.has_key('blocklist')):
            raise UnmarshalException('argument missing', 'blocklist', '')
        blocklist = args["blocklist"]
        if type(blocklist['blocksize']) <> type(0):
            raise (TypeError("int", repr(blocklist['blocksize'])))
        if type(blocklist['ranges']) <> type([]):
            raise (TypeError("(int64 * int64) list", repr(blocklist['ranges'])))
        for tmp_27 in blocklist['ranges']:
            if (type(tmp_27) is tuple) and tmp_27.length==2:
                if not(is_long(tmp_27[0])):
                    raise (TypeError("int64", repr(tmp_27[0])))
                if not(is_long(tmp_27[1])):
                    raise (TypeError("int64", repr(tmp_27[1])))
        results = self._impl.copy(dbg, uri, domain, remote, blocklist)
        if results[0] not in ["Copy","Mirror"]:
            raise (TypeError("| Copy ((string * string)) (** Copy (src,dst) represents an on-going copy operation from the [src] URI to the [dst] URI *) | Mirror ((string * string)) (** Mirror (src,dst) represents an on-going mirror operation from the [src] URI to the [dst] URI *)", repr(results)))
        if results[0] == 'Copy':
            if (type(results[1]) is tuple) and results[1].length==2:
                if type(results[1][0]) <> type("") and type(results[1][0]) <> type(u""):
                    raise (TypeError("string", repr(results[1][0])))
                if type(results[1][1]) <> type("") and type(results[1][1]) <> type(u""):
                    raise (TypeError("string", repr(results[1][1])))
        elif results[0] == 'Mirror':
            if (type(results[1]) is tuple) and results[1].length==2:
                if type(results[1][0]) <> type("") and type(results[1][0]) <> type(u""):
                    raise (TypeError("string", repr(results[1][0])))
                if type(results[1][1]) <> type("") and type(results[1][1]) <> type(u""):
                    raise (TypeError("string", repr(results[1][1])))
        return results
    def mirror(self, args):
        """type-check inputs, call implementation, type-check outputs and return"""
        if type(args) <> type({}):
            raise (UnmarshalException('arguments', 'dict', repr(args)))
        if not(args.has_key('dbg')):
            raise UnmarshalException('argument missing', 'dbg', '')
        dbg = args["dbg"]
        if type(dbg) <> type("") and type(dbg) <> type(u""):
            raise (TypeError("string", repr(dbg)))
        if not(args.has_key('uri')):
            raise UnmarshalException('argument missing', 'uri', '')
        uri = args["uri"]
        if type(uri) <> type("") and type(uri) <> type(u""):
            raise (TypeError("string", repr(uri)))
        if not(args.has_key('domain')):
            raise UnmarshalException('argument missing', 'domain', '')
        domain = args["domain"]
        if type(domain) <> type("") and type(domain) <> type(u""):
            raise (TypeError("string", repr(domain)))
        if not(args.has_key('remote')):
            raise UnmarshalException('argument missing', 'remote', '')
        remote = args["remote"]
        if type(remote) <> type("") and type(remote) <> type(u""):
            raise (TypeError("string", repr(remote)))
        results = self._impl.mirror(dbg, uri, domain, remote)
        if results[0] not in ["Copy","Mirror"]:
            raise (TypeError("| Copy ((string * string)) (** Copy (src,dst) represents an on-going copy operation from the [src] URI to the [dst] URI *) | Mirror ((string * string)) (** Mirror (src,dst) represents an on-going mirror operation from the [src] URI to the [dst] URI *)", repr(results)))
        if results[0] == 'Copy':
            if (type(results[1]) is tuple) and results[1].length==2:
                if type(results[1][0]) <> type("") and type(results[1][0]) <> type(u""):
                    raise (TypeError("string", repr(results[1][0])))
                if type(results[1][1]) <> type("") and type(results[1][1]) <> type(u""):
                    raise (TypeError("string", repr(results[1][1])))
        elif results[0] == 'Mirror':
            if (type(results[1]) is tuple) and results[1].length==2:
                if type(results[1][0]) <> type("") and type(results[1][0]) <> type(u""):
                    raise (TypeError("string", repr(results[1][0])))
                if type(results[1][1]) <> type("") and type(results[1][1]) <> type(u""):
                    raise (TypeError("string", repr(results[1][1])))
        return results
    def stat(self, args):
        """type-check inputs, call implementation, type-check outputs and return"""
        if type(args) <> type({}):
            raise (UnmarshalException('arguments', 'dict', repr(args)))
        if not(args.has_key('dbg')):
            raise UnmarshalException('argument missing', 'dbg', '')
        dbg = args["dbg"]
        if type(dbg) <> type("") and type(dbg) <> type(u""):
            raise (TypeError("string", repr(dbg)))
        if not(args.has_key('operation')):
            raise UnmarshalException('argument missing', 'operation', '')
        operation = args["operation"]
        if operation[0] not in ["Copy","Mirror"]:
            raise (TypeError("| Copy ((string * string)) (** Copy (src,dst) represents an on-going copy operation from the [src] URI to the [dst] URI *) | Mirror ((string * string)) (** Mirror (src,dst) represents an on-going mirror operation from the [src] URI to the [dst] URI *)", repr(operation)))
        if operation[0] == 'Copy':
            if (type(operation[1]) is tuple) and operation[1].length==2:
                if type(operation[1][0]) <> type("") and type(operation[1][0]) <> type(u""):
                    raise (TypeError("string", repr(operation[1][0])))
                if type(operation[1][1]) <> type("") and type(operation[1][1]) <> type(u""):
                    raise (TypeError("string", repr(operation[1][1])))
        elif operation[0] == 'Mirror':
            if (type(operation[1]) is tuple) and operation[1].length==2:
                if type(operation[1][0]) <> type("") and type(operation[1][0]) <> type(u""):
                    raise (TypeError("string", repr(operation[1][0])))
                if type(operation[1][1]) <> type("") and type(operation[1][1]) <> type(u""):
                    raise (TypeError("string", repr(operation[1][1])))
        results = self._impl.stat(dbg, operation)
        if type(results['failed']) <> type(True):
            raise (TypeError("bool", repr(results['failed'])))
        if results['progress'] <> None:
            if type(results['progress']) <> type(1.1):
                raise (TypeError("float", repr(results['progress'])))
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
        if not(args.has_key('operation')):
            raise UnmarshalException('argument missing', 'operation', '')
        operation = args["operation"]
        print("operation='%s'" % str(operation))
        print("operation[0]='%s'" % str (operation[0]))
        if operation[0] not in ["Copy","Mirror"]:
            raise (TypeError("| Copy ((string * string)) (** Copy (src,dst) represents an on-going copy operation from the [src] URI to the [dst] URI *) | Mirror ((string * string)) (** Mirror (src,dst) represents an on-going mirror operation from the [src] URI to the [dst] URI *)", repr(operation)))
        if operation[0] == 'Copy':
            if (type(operation[1]) is tuple) and operation[1].length==2:
                if type(operation[1][0]) <> type("") and type(operation[1][0]) <> type(u""):
                    raise (TypeError("string", repr(operation[1][0])))
                if type(operation[1][1]) <> type("") and type(operation[1][1]) <> type(u""):
                    raise (TypeError("string", repr(operation[1][1])))
        elif operation[0] == 'Mirror':
            if (type(operation[1]) is tuple) and operation[1].length==2:
                if type(operation[1][0]) <> type("") and type(operation[1][0]) <> type(u""):
                    raise (TypeError("string", repr(operation[1][0])))
                if type(operation[1][1]) <> type("") and type(operation[1][1]) <> type(u""):
                    raise (TypeError("string", repr(operation[1][1])))
        results = self._impl.cancel(dbg, operation)
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
        if not(args.has_key('operation')):
            raise UnmarshalException('argument missing', 'operation', '')
        operation = args["operation"]
        if operation[0] not in ["Copy","Mirror"]:
            raise (TypeError("| Copy ((string * string)) (** Copy (src,dst) represents an on-going copy operation from the [src] URI to the [dst] URI *) | Mirror ((string * string)) (** Mirror (src,dst) represents an on-going mirror operation from the [src] URI to the [dst] URI *)", repr(operation)))
        if operation[0] == 'Copy':
            if (type(operation[1]) is tuple) and operation[1].length==2:
                if type(operation[1][0]) <> type("") and type(operation[1][0]) <> type(u""):
                    raise (TypeError("string", repr(operation[1][0])))
                if type(operation[1][1]) <> type("") and type(operation[1][1]) <> type(u""):
                    raise (TypeError("string", repr(operation[1][1])))
        elif operation[0] == 'Mirror':
            if (type(operation[1]) is tuple) and operation[1].length==2:
                if type(operation[1][0]) <> type("") and type(operation[1][0]) <> type(u""):
                    raise (TypeError("string", repr(operation[1][0])))
                if type(operation[1][1]) <> type("") and type(operation[1][1]) <> type(u""):
                    raise (TypeError("string", repr(operation[1][1])))
        results = self._impl.destroy(dbg, operation)
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
            raise (TypeError("| Copy ((string * string)) (** Copy (src,dst) represents an on-going copy operation from the [src] URI to the [dst] URI *) | Mirror ((string * string)) (** Mirror (src,dst) represents an on-going mirror operation from the [src] URI to the [dst] URI *) list", repr(results)))
        for tmp_28 in results:
            if tmp_28[0] not in ["Copy","Mirror"]:
                raise (TypeError("| Copy ((string * string)) (** Copy (src,dst) represents an on-going copy operation from the [src] URI to the [dst] URI *) | Mirror ((string * string)) (** Mirror (src,dst) represents an on-going mirror operation from the [src] URI to the [dst] URI *)", repr(tmp_28)))
            if tmp_28[0] == 'Copy':
                if (type(tmp_28[1]) is tuple) and tmp_28[1].length==2:
                    if type(tmp_28[1][0]) <> type("") and type(tmp_28[1][0]) <> type(u""):
                        raise (TypeError("string", repr(tmp_28[1][0])))
                    if type(tmp_28[1][1]) <> type("") and type(tmp_28[1][1]) <> type(u""):
                        raise (TypeError("string", repr(tmp_28[1][1])))
            elif tmp_28[0] == 'Mirror':
                if (type(tmp_28[1]) is tuple) and tmp_28[1].length==2:
                    if type(tmp_28[1][0]) <> type("") and type(tmp_28[1][0]) <> type(u""):
                        raise (TypeError("string", repr(tmp_28[1][0])))
                    if type(tmp_28[1][1]) <> type("") and type(tmp_28[1][1]) <> type(u""):
                        raise (TypeError("string", repr(tmp_28[1][1])))
        return results
    def _dispatch(self, method, params):
        """type check inputs, call implementation, type check outputs and return"""
        args = params[0]
        if method == "Data.copy":
            return success(self.copy(args))
        elif method == "Data.mirror":
            return success(self.mirror(args))
        elif method == "Data.stat":
            return success(self.stat(args))
        elif method == "Data.cancel":
            return success(self.cancel(args))
        elif method == "Data.destroy":
            return success(self.destroy(args))
        elif method == "Data.ls":
            return success(self.ls(args))
class Data_skeleton:
    """This interface is used for long-running data operations such as copying the contents of volumes or mirroring volumes to remote destinations"""
    def __init__(self):
        pass
    def copy(self, dbg, uri, domain, remote, blocklist):
        """This interface is used for long-running data operations such as copying the contents of volumes or mirroring volumes to remote destinations"""
        raise Unimplemented("Data.copy")
    def mirror(self, dbg, uri, domain, remote):
        """This interface is used for long-running data operations such as copying the contents of volumes or mirroring volumes to remote destinations"""
        raise Unimplemented("Data.mirror")
    def stat(self, dbg, operation):
        """This interface is used for long-running data operations such as copying the contents of volumes or mirroring volumes to remote destinations"""
        raise Unimplemented("Data.stat")
    def cancel(self, dbg, operation):
        """This interface is used for long-running data operations such as copying the contents of volumes or mirroring volumes to remote destinations"""
        raise Unimplemented("Data.cancel")
    def destroy(self, dbg, operation):
        """This interface is used for long-running data operations such as copying the contents of volumes or mirroring volumes to remote destinations"""
        raise Unimplemented("Data.destroy")
    def ls(self, dbg):
        """This interface is used for long-running data operations such as copying the contents of volumes or mirroring volumes to remote destinations"""
        raise Unimplemented("Data.ls")
class Data_test:
    """This interface is used for long-running data operations such as copying the contents of volumes or mirroring volumes to remote destinations"""
    def __init__(self):
        pass
    def copy(self, dbg, uri, domain, remote, blocklist):
        """This interface is used for long-running data operations such as copying the contents of volumes or mirroring volumes to remote destinations"""
        result = {}
        result["operation"] = None
        return result
    def mirror(self, dbg, uri, domain, remote):
        """This interface is used for long-running data operations such as copying the contents of volumes or mirroring volumes to remote destinations"""
        result = {}
        result["operation"] = None
        return result
    def stat(self, dbg, operation):
        """This interface is used for long-running data operations such as copying the contents of volumes or mirroring volumes to remote destinations"""
        result = {}
        result["status"] = { "failed": True, "progress": None }
        return result
    def cancel(self, dbg, operation):
        """This interface is used for long-running data operations such as copying the contents of volumes or mirroring volumes to remote destinations"""
        result = {}
        return result
    def destroy(self, dbg, operation):
        """This interface is used for long-running data operations such as copying the contents of volumes or mirroring volumes to remote destinations"""
        result = {}
        return result
    def ls(self, dbg):
        """This interface is used for long-running data operations such as copying the contents of volumes or mirroring volumes to remote destinations"""
        result = {}
        result["operations"] = [ None, None ]
        return result
import argparse, traceback
import xapi

class JsonArg(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, json.loads(values))
                
class Data_commandline():
    """Parse command-line arguments and call an implementation."""
    def __init__(self, impl):
        self.impl = impl
        self.dispatcher = Data_server_dispatcher(self.impl)
    def _parse_copy(self):
        """[copy uri domain remote blocks] copies [blocks] from the local disk to a remote URI. This may be called as part of a Volume Mirroring operation, and hence may need to cooperate with whatever process is currently mirroring writes to ensure data integrity is maintained"""
        # in --json mode we don't have any other arguments
        if ('--json' in sys.argv or '-j' in sys.argv):
            jsondict = json.loads(sys.stdin.readline(),)
            jsondict['json'] = True
            return jsondict
        parser = argparse.ArgumentParser(description='[copy uri domain remote blocks] copies [blocks] from the local disk to a remote URI. This may be called as part of a Volume Mirroring operation, and hence may need to cooperate with whatever process is currently mirroring writes to ensure data integrity is maintained')
        parser.add_argument('-j', '--json', action='store_const', const=True, default=False, help='Read json from stdin, print json to stdout', required=False)
        parser.add_argument('dbg', action='store', help='Debug context from the caller')
        parser.add_argument('uri', action='store', help='A URI which represents how to access the volume disk data.')
        parser.add_argument('domain', action='store', help='An opaque string which represents the Xen domain.')
        parser.add_argument('remote', action='store', help='A URI which represents how to access a remote volume disk data.')
        parser.add_argument('blocklist', action=JsonArg, help='List of blocks for copying')
        return vars(parser.parse_args())
    def _parse_mirror(self):
        """[mirror uri domain remote] starts mirroring new writes to the volume to a remote URI (usually NBD). This is called as part of a volume mirroring process"""
        # in --json mode we don't have any other arguments
        if ('--json' in sys.argv or '-j' in sys.argv):
            jsondict = json.loads(sys.stdin.readline(),)
            jsondict['json'] = True
            return jsondict
        parser = argparse.ArgumentParser(description='[mirror uri domain remote] starts mirroring new writes to the volume to a remote URI (usually NBD). This is called as part of a volume mirroring process')
        parser.add_argument('-j', '--json', action='store_const', const=True, default=False, help='Read json from stdin, print json to stdout', required=False)
        parser.add_argument('dbg', action='store', help='Debug context from the caller')
        parser.add_argument('uri', action='store', help='A URI which represents how to access the volume disk data.')
        parser.add_argument('domain', action='store', help='An opaque string which represents the Xen domain.')
        parser.add_argument('remote', action='store', help='A URI which represents how to access a remote volume disk data.')
        return vars(parser.parse_args())
    def _parse_stat(self):
        """[stat operation] returns the current status of [operation]. For a copy operation, this will contain progress information."""
        # in --json mode we don't have any other arguments
        if ('--json' in sys.argv or '-j' in sys.argv):
            jsondict = json.loads(sys.stdin.readline(),)
            jsondict['json'] = True
            return jsondict
        parser = argparse.ArgumentParser(description='[stat operation] returns the current status of [operation]. For a copy operation, this will contain progress information.')
        parser.add_argument('-j', '--json', action='store_const', const=True, default=False, help='Read json from stdin, print json to stdout', required=False)
        parser.add_argument('dbg', action='store', help='Debug context from the caller')
        parser.add_argument('operation', action=JsonArg, help='The primary key for referring to a long-running operation')
        return vars(parser.parse_args())
    def _parse_cancel(self):
        """[cancel operation] cancels a long-running operation. Note that the call may return before the operation has finished."""
        # in --json mode we don't have any other arguments
        if ('--json' in sys.argv or '-j' in sys.argv):
            jsondict = json.loads(sys.stdin.readline(),)
            jsondict['json'] = True
            return jsondict
        parser = argparse.ArgumentParser(description='[cancel operation] cancels a long-running operation. Note that the call may return before the operation has finished.')
        parser.add_argument('-j', '--json', action='store_const', const=True, default=False, help='Read json from stdin, print json to stdout', required=False)
        parser.add_argument('dbg', action='store', help='Debug context from the caller')
        parser.add_argument('operation', action=JsonArg, help='The primary key for referring to a long-running operation')
        return vars(parser.parse_args())
    def _parse_destroy(self):
        """[destroy operation] destroys the information about a long-running operation. This should fail when run against an operation that is still in progress."""
        # in --json mode we don't have any other arguments
        if ('--json' in sys.argv or '-j' in sys.argv):
            jsondict = json.loads(sys.stdin.readline(),)
            jsondict['json'] = True
            return jsondict
        parser = argparse.ArgumentParser(description='[destroy operation] destroys the information about a long-running operation. This should fail when run against an operation that is still in progress.')
        parser.add_argument('-j', '--json', action='store_const', const=True, default=False, help='Read json from stdin, print json to stdout', required=False)
        parser.add_argument('dbg', action='store', help='Debug context from the caller')
        parser.add_argument('operation', action=JsonArg, help='The primary key for referring to a long-running operation')
        return vars(parser.parse_args())
    def _parse_ls(self):
        """[ls] returns a list of all current operations"""
        # in --json mode we don't have any other arguments
        if ('--json' in sys.argv or '-j' in sys.argv):
            jsondict = json.loads(sys.stdin.readline(),)
            jsondict['json'] = True
            return jsondict
        parser = argparse.ArgumentParser(description='[ls] returns a list of all current operations')
        parser.add_argument('-j', '--json', action='store_const', const=True, default=False, help='Read json from stdin, print json to stdout', required=False)
        parser.add_argument('dbg', action='store', help='Debug context from the caller')
        return vars(parser.parse_args())
    def copy(self):
        use_json = False
        try:
            request = self._parse_copy()
            use_json = 'json' in request and request['json']
            results = self.dispatcher.copy(request)
            print json.dumps(results)
        except Exception, e:
            if use_json:
                xapi.handle_exception(e)
            else:
                traceback.print_exc()
                raise e
    def mirror(self):
        use_json = False
        try:
            request = self._parse_mirror()
            use_json = 'json' in request and request['json']
            results = self.dispatcher.mirror(request)
            print json.dumps(results)
        except Exception, e:
            if use_json:
                xapi.handle_exception(e)
            else:
                traceback.print_exc()
                raise e
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
class Datapath_server_dispatcher:
    """Xapi will call the functions here on VM start/shutdown/suspend/resume/migrate. Every function is idempotent. Every function takes a domain parameter which allows the implementation to track how many domains are currently using the volume."""
    def __init__(self, impl):
        """impl is a proxy object whose methods contain the implementation"""
        self._impl = impl
    def open(self, args):
        """type-check inputs, call implementation, type-check outputs and return"""
        if type(args) <> type({}):
            raise (UnmarshalException('arguments', 'dict', repr(args)))
        if not(args.has_key('dbg')):
            raise UnmarshalException('argument missing', 'dbg', '')
        dbg = args["dbg"]
        if type(dbg) <> type("") and type(dbg) <> type(u""):
            raise (TypeError("string", repr(dbg)))
        if not(args.has_key('uri')):
            raise UnmarshalException('argument missing', 'uri', '')
        uri = args["uri"]
        if type(uri) <> type("") and type(uri) <> type(u""):
            raise (TypeError("string", repr(uri)))
        if not(args.has_key('persistent')):
            raise UnmarshalException('argument missing', 'persistent', '')
        persistent = args["persistent"]
        if type(persistent) <> type(True):
            raise (TypeError("bool", repr(persistent)))
        results = self._impl.open(dbg, uri, persistent)
        return results
    def attach(self, args):
        """type-check inputs, call implementation, type-check outputs and return"""
        if type(args) <> type({}):
            raise (UnmarshalException('arguments', 'dict', repr(args)))
        if not(args.has_key('dbg')):
            raise UnmarshalException('argument missing', 'dbg', '')
        dbg = args["dbg"]
        if type(dbg) <> type("") and type(dbg) <> type(u""):
            raise (TypeError("string", repr(dbg)))
        if not(args.has_key('uri')):
            raise UnmarshalException('argument missing', 'uri', '')
        uri = args["uri"]
        if type(uri) <> type("") and type(uri) <> type(u""):
            raise (TypeError("string", repr(uri)))
        if not(args.has_key('domain')):
            raise UnmarshalException('argument missing', 'domain', '')
        domain = args["domain"]
        if type(domain) <> type("") and type(domain) <> type(u""):
            raise (TypeError("string", repr(domain)))
        results = self._impl.attach(dbg, uri, domain)
        if type(results['domain_uuid']) <> type("") and type(results['domain_uuid']) <> type(u""):
            raise (TypeError("string", repr(results['domain_uuid'])))
        if results['implementation'][0] not in ["Blkback","Qdisk","Tapdisk3"]:
            raise (TypeError("| Blkback (string) (** use kernel blkback with the given 'params' key *) | Qdisk (string) (** use userspace qemu qdisk with the given 'params' key *) | Tapdisk3 (string) (** use userspace tapdisk3 with the given 'params' key *)", repr(results['implementation'])))
        if results['implementation'][0] == 'Blkback':
            if type(results['implementation'][1]) <> type("") and type(results['implementation'][1]) <> type(u""):
                raise (TypeError("string", repr(results['implementation'][1])))
        elif results['implementation'][0] == 'Qdisk':
            if type(results['implementation'][1]) <> type("") and type(results['implementation'][1]) <> type(u""):
                raise (TypeError("string", repr(results['implementation'][1])))
        elif results['implementation'][0] == 'Tapdisk3':
            if type(results['implementation'][1]) <> type("") and type(results['implementation'][1]) <> type(u""):
                raise (TypeError("string", repr(results['implementation'][1])))
        return results
    def activate(self, args):
        """type-check inputs, call implementation, type-check outputs and return"""
        if type(args) <> type({}):
            raise (UnmarshalException('arguments', 'dict', repr(args)))
        if not(args.has_key('dbg')):
            raise UnmarshalException('argument missing', 'dbg', '')
        dbg = args["dbg"]
        if type(dbg) <> type("") and type(dbg) <> type(u""):
            raise (TypeError("string", repr(dbg)))
        if not(args.has_key('uri')):
            raise UnmarshalException('argument missing', 'uri', '')
        uri = args["uri"]
        if type(uri) <> type("") and type(uri) <> type(u""):
            raise (TypeError("string", repr(uri)))
        if not(args.has_key('domain')):
            raise UnmarshalException('argument missing', 'domain', '')
        domain = args["domain"]
        if type(domain) <> type("") and type(domain) <> type(u""):
            raise (TypeError("string", repr(domain)))
        results = self._impl.activate(dbg, uri, domain)
        return results
    def deactivate(self, args):
        """type-check inputs, call implementation, type-check outputs and return"""
        if type(args) <> type({}):
            raise (UnmarshalException('arguments', 'dict', repr(args)))
        if not(args.has_key('dbg')):
            raise UnmarshalException('argument missing', 'dbg', '')
        dbg = args["dbg"]
        if type(dbg) <> type("") and type(dbg) <> type(u""):
            raise (TypeError("string", repr(dbg)))
        if not(args.has_key('uri')):
            raise UnmarshalException('argument missing', 'uri', '')
        uri = args["uri"]
        if type(uri) <> type("") and type(uri) <> type(u""):
            raise (TypeError("string", repr(uri)))
        if not(args.has_key('domain')):
            raise UnmarshalException('argument missing', 'domain', '')
        domain = args["domain"]
        if type(domain) <> type("") and type(domain) <> type(u""):
            raise (TypeError("string", repr(domain)))
        results = self._impl.deactivate(dbg, uri, domain)
        return results
    def detach(self, args):
        """type-check inputs, call implementation, type-check outputs and return"""
        if type(args) <> type({}):
            raise (UnmarshalException('arguments', 'dict', repr(args)))
        if not(args.has_key('dbg')):
            raise UnmarshalException('argument missing', 'dbg', '')
        dbg = args["dbg"]
        if type(dbg) <> type("") and type(dbg) <> type(u""):
            raise (TypeError("string", repr(dbg)))
        if not(args.has_key('uri')):
            raise UnmarshalException('argument missing', 'uri', '')
        uri = args["uri"]
        if type(uri) <> type("") and type(uri) <> type(u""):
            raise (TypeError("string", repr(uri)))
        if not(args.has_key('domain')):
            raise UnmarshalException('argument missing', 'domain', '')
        domain = args["domain"]
        if type(domain) <> type("") and type(domain) <> type(u""):
            raise (TypeError("string", repr(domain)))
        results = self._impl.detach(dbg, uri, domain)
        return results
    def close(self, args):
        """type-check inputs, call implementation, type-check outputs and return"""
        if type(args) <> type({}):
            raise (UnmarshalException('arguments', 'dict', repr(args)))
        if not(args.has_key('dbg')):
            raise UnmarshalException('argument missing', 'dbg', '')
        dbg = args["dbg"]
        if type(dbg) <> type("") and type(dbg) <> type(u""):
            raise (TypeError("string", repr(dbg)))
        if not(args.has_key('uri')):
            raise UnmarshalException('argument missing', 'uri', '')
        uri = args["uri"]
        if type(uri) <> type("") and type(uri) <> type(u""):
            raise (TypeError("string", repr(uri)))
        results = self._impl.close(dbg, uri)
        return results
    def _dispatch(self, method, params):
        """type check inputs, call implementation, type check outputs and return"""
        args = params[0]
        if method == "Datapath.open":
            return success(self.open(args))
        elif method == "Datapath.attach":
            return success(self.attach(args))
        elif method == "Datapath.activate":
            return success(self.activate(args))
        elif method == "Datapath.deactivate":
            return success(self.deactivate(args))
        elif method == "Datapath.detach":
            return success(self.detach(args))
        elif method == "Datapath.close":
            return success(self.close(args))
class Datapath_skeleton:
    """Xapi will call the functions here on VM start/shutdown/suspend/resume/migrate. Every function is idempotent. Every function takes a domain parameter which allows the implementation to track how many domains are currently using the volume."""
    def __init__(self):
        pass
    def open(self, dbg, uri, persistent):
        """Xapi will call the functions here on VM start/shutdown/suspend/resume/migrate. Every function is idempotent. Every function takes a domain parameter which allows the implementation to track how many domains are currently using the volume."""
        raise Unimplemented("Datapath.open")
    def attach(self, dbg, uri, domain):
        """Xapi will call the functions here on VM start/shutdown/suspend/resume/migrate. Every function is idempotent. Every function takes a domain parameter which allows the implementation to track how many domains are currently using the volume."""
        raise Unimplemented("Datapath.attach")
    def activate(self, dbg, uri, domain):
        """Xapi will call the functions here on VM start/shutdown/suspend/resume/migrate. Every function is idempotent. Every function takes a domain parameter which allows the implementation to track how many domains are currently using the volume."""
        raise Unimplemented("Datapath.activate")
    def deactivate(self, dbg, uri, domain):
        """Xapi will call the functions here on VM start/shutdown/suspend/resume/migrate. Every function is idempotent. Every function takes a domain parameter which allows the implementation to track how many domains are currently using the volume."""
        raise Unimplemented("Datapath.deactivate")
    def detach(self, dbg, uri, domain):
        """Xapi will call the functions here on VM start/shutdown/suspend/resume/migrate. Every function is idempotent. Every function takes a domain parameter which allows the implementation to track how many domains are currently using the volume."""
        raise Unimplemented("Datapath.detach")
    def close(self, dbg, uri):
        """Xapi will call the functions here on VM start/shutdown/suspend/resume/migrate. Every function is idempotent. Every function takes a domain parameter which allows the implementation to track how many domains are currently using the volume."""
        raise Unimplemented("Datapath.close")
class Datapath_test:
    """Xapi will call the functions here on VM start/shutdown/suspend/resume/migrate. Every function is idempotent. Every function takes a domain parameter which allows the implementation to track how many domains are currently using the volume."""
    def __init__(self):
        pass
    def open(self, dbg, uri, persistent):
        """Xapi will call the functions here on VM start/shutdown/suspend/resume/migrate. Every function is idempotent. Every function takes a domain parameter which allows the implementation to track how many domains are currently using the volume."""
        result = {}
        return result
    def attach(self, dbg, uri, domain):
        """Xapi will call the functions here on VM start/shutdown/suspend/resume/migrate. Every function is idempotent. Every function takes a domain parameter which allows the implementation to track how many domains are currently using the volume."""
        result = {}
        result["backend"] = { "domain_uuid": "string", "implementation": None }
        return result
    def activate(self, dbg, uri, domain):
        """Xapi will call the functions here on VM start/shutdown/suspend/resume/migrate. Every function is idempotent. Every function takes a domain parameter which allows the implementation to track how many domains are currently using the volume."""
        result = {}
        return result
    def deactivate(self, dbg, uri, domain):
        """Xapi will call the functions here on VM start/shutdown/suspend/resume/migrate. Every function is idempotent. Every function takes a domain parameter which allows the implementation to track how many domains are currently using the volume."""
        result = {}
        return result
    def detach(self, dbg, uri, domain):
        """Xapi will call the functions here on VM start/shutdown/suspend/resume/migrate. Every function is idempotent. Every function takes a domain parameter which allows the implementation to track how many domains are currently using the volume."""
        result = {}
        return result
    def close(self, dbg, uri):
        """Xapi will call the functions here on VM start/shutdown/suspend/resume/migrate. Every function is idempotent. Every function takes a domain parameter which allows the implementation to track how many domains are currently using the volume."""
        result = {}
        return result
import argparse, traceback
import xapi
class Datapath_commandline():
    """Parse command-line arguments and call an implementation."""
    def __init__(self, impl):
        self.impl = impl
        self.dispatcher = Datapath_server_dispatcher(self.impl)
    def _parse_open(self):
        """[open uri persistent] is called before a disk is attached to a VM. If persistent is true then care should be taken to persist all writes to the disk. If persistent is false then the implementation should configure a temporary location for writes so they can be thrown away on [close]."""
        # in --json mode we don't have any other arguments
        if ('--json' in sys.argv or '-j' in sys.argv):
            jsondict = json.loads(sys.stdin.readline(),)
            jsondict['json'] = True
            return jsondict
        parser = argparse.ArgumentParser(description='[open uri persistent] is called before a disk is attached to a VM. If persistent is true then care should be taken to persist all writes to the disk. If persistent is false then the implementation should configure a temporary location for writes so they can be thrown away on [close].')
        parser.add_argument('-j', '--json', action='store_const', const=True, default=False, help='Read json from stdin, print json to stdout', required=False)
        parser.add_argument('dbg', action='store', help='Debug context from the caller')
        parser.add_argument('uri', action='store', help='A URI which represents how to access the volume disk data.')
        parser.add_argument('persistent', action='store', help='True means the disk data is persistent and should be preserved when the datapath is closed i.e. when a VM is shutdown or rebooted. False means the data should be thrown away when the VM is shutdown or rebooted.')
        return vars(parser.parse_args())
    def _parse_attach(self):
        """[attach uri domain] prepares a connection between the storage named by [uri] and the Xen domain with id [domain]. The return value is the information needed by the Xen toolstack to setup the shared-memory blkfront protocol. Note that the same volume may be simultaneously attached to multiple hosts for example over a migrate. If an implementation needs to perform an explicit handover, then it should implement [activate] and [deactivate]. This function is idempotent."""
        # in --json mode we don't have any other arguments
        if ('--json' in sys.argv or '-j' in sys.argv):
            jsondict = json.loads(sys.stdin.readline(),)
            jsondict['json'] = True
            return jsondict
        parser = argparse.ArgumentParser(description='[attach uri domain] prepares a connection between the storage named by [uri] and the Xen domain with id [domain]. The return value is the information needed by the Xen toolstack to setup the shared-memory blkfront protocol. Note that the same volume may be simultaneously attached to multiple hosts for example over a migrate. If an implementation needs to perform an explicit handover, then it should implement [activate] and [deactivate]. This function is idempotent.')
        parser.add_argument('-j', '--json', action='store_const', const=True, default=False, help='Read json from stdin, print json to stdout', required=False)
        parser.add_argument('dbg', action='store', help='Debug context from the caller')
        parser.add_argument('uri', action='store', help='A URI which represents how to access the volume disk data.')
        parser.add_argument('domain', action='store', help='An opaque string which represents the Xen domain.')
        return vars(parser.parse_args())
    def _parse_activate(self):
        """[activate uri domain] is called just before a VM needs to read or write its disk. This is an opportunity for an implementation which needs to perform an explicit volume handover to do it. This function is called in the migration downtime window so delays here will be noticeable to users and should be minimised. This function is idempotent."""
        # in --json mode we don't have any other arguments
        if ('--json' in sys.argv or '-j' in sys.argv):
            jsondict = json.loads(sys.stdin.readline(),)
            jsondict['json'] = True
            return jsondict
        parser = argparse.ArgumentParser(description='[activate uri domain] is called just before a VM needs to read or write its disk. This is an opportunity for an implementation which needs to perform an explicit volume handover to do it. This function is called in the migration downtime window so delays here will be noticeable to users and should be minimised. This function is idempotent.')
        parser.add_argument('-j', '--json', action='store_const', const=True, default=False, help='Read json from stdin, print json to stdout', required=False)
        parser.add_argument('dbg', action='store', help='Debug context from the caller')
        parser.add_argument('uri', action='store', help='A URI which represents how to access the volume disk data.')
        parser.add_argument('domain', action='store', help='An opaque string which represents the Xen domain.')
        return vars(parser.parse_args())
    def _parse_deactivate(self):
        """[deactivate uri domain] is called as soon as a VM has finished reading or writing its disk. This is an opportunity for an implementation which needs to perform an explicit volume handover to do it. This function is called in the migration downtime window so delays here will be noticeable to users and should be minimised. This function is idempotent."""
        # in --json mode we don't have any other arguments
        if ('--json' in sys.argv or '-j' in sys.argv):
            jsondict = json.loads(sys.stdin.readline(),)
            jsondict['json'] = True
            return jsondict
        parser = argparse.ArgumentParser(description='[deactivate uri domain] is called as soon as a VM has finished reading or writing its disk. This is an opportunity for an implementation which needs to perform an explicit volume handover to do it. This function is called in the migration downtime window so delays here will be noticeable to users and should be minimised. This function is idempotent.')
        parser.add_argument('-j', '--json', action='store_const', const=True, default=False, help='Read json from stdin, print json to stdout', required=False)
        parser.add_argument('dbg', action='store', help='Debug context from the caller')
        parser.add_argument('uri', action='store', help='A URI which represents how to access the volume disk data.')
        parser.add_argument('domain', action='store', help='An opaque string which represents the Xen domain.')
        return vars(parser.parse_args())
    def _parse_detach(self):
        """[detach uri domain] is called sometime after a VM has finished reading or writing its disk. This is an opportunity to clean up any resources associated with the disk. This function is called outside the migration downtime window so can be slow without affecting users. This function is idempotent. This function should never fail. If an implementation is unable to perform some cleanup right away then it should queue the action internally. Any error result represents a bug in the implementation."""
        # in --json mode we don't have any other arguments
        if ('--json' in sys.argv or '-j' in sys.argv):
            jsondict = json.loads(sys.stdin.readline(),)
            jsondict['json'] = True
            return jsondict
        parser = argparse.ArgumentParser(description='[detach uri domain] is called sometime after a VM has finished reading or writing its disk. This is an opportunity to clean up any resources associated with the disk. This function is called outside the migration downtime window so can be slow without affecting users. This function is idempotent. This function should never fail. If an implementation is unable to perform some cleanup right away then it should queue the action internally. Any error result represents a bug in the implementation.')
        parser.add_argument('-j', '--json', action='store_const', const=True, default=False, help='Read json from stdin, print json to stdout', required=False)
        parser.add_argument('dbg', action='store', help='Debug context from the caller')
        parser.add_argument('uri', action='store', help='A URI which represents how to access the volume disk data.')
        parser.add_argument('domain', action='store', help='An opaque string which represents the Xen domain.')
        return vars(parser.parse_args())
    def _parse_close(self):
        """[close uri] is called after a disk is detached and a VM shutdown. This is an opportunity to throw away writes if the disk is not persistent."""
        # in --json mode we don't have any other arguments
        if ('--json' in sys.argv or '-j' in sys.argv):
            jsondict = json.loads(sys.stdin.readline(),)
            jsondict['json'] = True
            return jsondict
        parser = argparse.ArgumentParser(description='[close uri] is called after a disk is detached and a VM shutdown. This is an opportunity to throw away writes if the disk is not persistent.')
        parser.add_argument('-j', '--json', action='store_const', const=True, default=False, help='Read json from stdin, print json to stdout', required=False)
        parser.add_argument('dbg', action='store', help='Debug context from the caller')
        parser.add_argument('uri', action='store', help='A URI which represents how to access the volume disk data.')
        return vars(parser.parse_args())
    def open(self):
        use_json = False
        try:
            request = self._parse_open()
            use_json = 'json' in request and request['json']
            results = self.dispatcher.open(request)
            print json.dumps(results)
        except Exception, e:
            if use_json:
                xapi.handle_exception(e)
            else:
                traceback.print_exc()
                raise e
    def attach(self):
        use_json = False
        try:
            request = self._parse_attach()
            use_json = 'json' in request and request['json']
            results = self.dispatcher.attach(request)
            print json.dumps(results)
        except Exception, e:
            if use_json:
                xapi.handle_exception(e)
            else:
                traceback.print_exc()
                raise e
    def activate(self):
        use_json = False
        try:
            request = self._parse_activate()
            use_json = 'json' in request and request['json']
            results = self.dispatcher.activate(request)
            print json.dumps(results)
        except Exception, e:
            if use_json:
                xapi.handle_exception(e)
            else:
                traceback.print_exc()
                raise e
    def deactivate(self):
        use_json = False
        try:
            request = self._parse_deactivate()
            use_json = 'json' in request and request['json']
            results = self.dispatcher.deactivate(request)
            print json.dumps(results)
        except Exception, e:
            if use_json:
                xapi.handle_exception(e)
            else:
                traceback.print_exc()
                raise e
    def detach(self):
        use_json = False
        try:
            request = self._parse_detach()
            use_json = 'json' in request and request['json']
            results = self.dispatcher.detach(request)
            print json.dumps(results)
        except Exception, e:
            if use_json:
                xapi.handle_exception(e)
            else:
                traceback.print_exc()
                raise e
    def close(self):
        use_json = False
        try:
            request = self._parse_close()
            use_json = 'json' in request and request['json']
            results = self.dispatcher.close(request)
            print json.dumps(results)
        except Exception, e:
            if use_json:
                xapi.handle_exception(e)
            else:
                traceback.print_exc()
                raise e
class datapath_server_dispatcher:
    """Demux calls to individual interface server_dispatchers"""
    def __init__(self, Data = None, Datapath = None):
        self.Data = Data
        self.Datapath = Datapath
    def _dispatch(self, method, params):
        try:
            log("method = %s params = %s" % (method, repr(params)))
            if method.startswith("Data") and self.Data:
                return self.Data._dispatch(method, params)
            elif method.startswith("Datapath") and self.Datapath:
                return self.Datapath._dispatch(method, params)
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
class datapath_server_test(datapath_server_dispatcher):
    """Create a server which will respond to all calls, returning arbitrary values. This is intended as a marshal/unmarshal test."""
    def __init__(self):
        datapath_server_dispatcher.__init__(self, Data_server_dispatcher(Data_test()), Datapath_server_dispatcher(Datapath_test()))

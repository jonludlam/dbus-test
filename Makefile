DESTDIR?=

INSTALL=install
MKDIR=mkdir
GIT=git
SED=sed
BZIP2=bzip2
CP=cp
OCAMLFIND=ocamlfind
MAKE=make

RPM_SPECSDIR?=$(shell rpm --eval='%_specdir')
RPM_SRPMSDIR?=$(shell rpm --eval='%_srcrpmdir')
RPM_SOURCESDIR?=$(shell rpm --eval='%_sourcedir')
RPMBUILD?=rpmbuild

default: build

idl: files.cmx types.cmx smapiv2.cmx xenops.cmx memory.cmx clocksource.cmx python.cmx ocaml.cmx html.cmx main.cmx
	${OCAMLFIND} ocamlopt -package xmlm -package unix -linkpkg -g -o idl files.cmx types.cmx smapiv2.cmx xenops.cmx memory.cmx clocksource.cmx python.cmx ocaml.cmx html.cmx main.cmx

toplevel: files.cmo types.cmo smapiv2.cmo xenops.cmo memory.cmo clocksource.cmo python.cmo ocaml.cmo html.cmo
	${OCAMLFIND} ocamlmktop -thread -package xmlm -linkpkg -g -o toplevel files.cmo types.cmo smapiv2.cmo xenops.cmo memory.cmo clocksource.cmo python.cmo ocaml.cmo html.cmo

%.cmx: %.ml
	${OCAMLFIND} ocamlopt -package xmlm -package unix -c -g -I . $<

%.cmo: %.ml
	${OCAMLFIND} ocamlc -package xmlm -c -g -I . $<

PYPATH=/usr/lib/xcp-sm-fs

.PHONY: build
build: idl
	mkdir -p ocaml/examples
	./idl
	${MAKE} -C ocaml

.PHONY: install
install: build
	${MKDIR} -p ${DESTDIR}${PYPATH}
	${INSTALL} python/fs.py ${DESTDIR}${PYPATH}
	${INSTALL} python/mount.py ${DESTDIR}${PYPATH}
	${INSTALL} python/storage.py ${DESTDIR}${PYPATH}
	${INSTALL} python/tapdisk.py ${DESTDIR}${PYPATH}
	${INSTALL} python/util.py ${DESTDIR}${PYPATH}
	${INSTALL} python/vhd.py ${DESTDIR}${PYPATH}
	${INSTALL} python/xcp.py ${DESTDIR}${PYPATH}
	${MKDIR} -p ${DESTDIR}/usr/bin
	${INSTALL} python/xcp-sm-fs ${DESTDIR}/usr/bin/xcp-sm-fs
	${MKDIR} -p ${DESTDIR}/etc
	${INSTALL} python/xcp-sm-fs.conf ${DESTDIR}/etc/xcp-sm-fs.conf
	${MKDIR} -p ${DESTDIR}/etc/rc.d/init.d
	${INSTALL} python/init.d-xcp-sm-fs ${DESTDIR}/etc/rc.d/init.d/xcp-sm-fs
	${MKDIR} -p ${DESTDIR}${PYPATH}/js/jQuery-Visualize/js
	${INSTALL} js/jQuery-Visualize/js/excanvas.js ${DESTDIR}${PYPATH}/js/jQuery-Visualize/js
	${INSTALL} js/jQuery-Visualize/js/visualize.jQuery.js ${DESTDIR}${PYPATH}/js/jQuery-Visualize/js
	${MKDIR} -p ${DESTDIR}${PYPATH}/js/jQuery-Visualize/css
	${INSTALL} js/jQuery-Visualize/css/visualize.css ${DESTDIR}/${PYPATH}/js/jQuery-Visualize/css
	${INSTALL} js/jQuery-Visualize/css/visualize-light.css ${DESTDIR}/${PYPATH}/js/jQuery-Visualize/css
	${INSTALL} js/mobile.html ${DESTDIR}/${PYPATH}/js

.PHONY: python/xcp-sm-fs.spec
python/xcp-sm-fs.spec: python/xcp-sm-fs.spec.in
	${SED} -e 's/@RPM_RELEASE@/$(shell git rev-list HEAD | wc -l)/g' < $< > $@

.PHONY: xcp-sm-fs-0.9.tar.bz2
xcp-sm-fs-0.9.tar.bz2:
	${GIT} archive --prefix=xcp-sm-fs-0.9/ --format=tar HEAD | ${BZIP2} -z > $@

.PHONY: srpm
srpm: python/xcp-sm-fs.spec xcp-sm-fs-0.9.tar.bz2
	${MKDIR} -p $(RPM_SOURCESDIR) $(RPM_SPECSDIR) $(RPM_SRPMSDIR)
	${CP} -f xcp-sm-fs-0.9.tar.bz2 $(RPM_SOURCESDIR)
	${CP} -f python/xcp-sm-fs.spec $(RPM_SPECSDIR)
	$(RPMBUILD) -bs --nodeps $(RPM_SPECSDIR)/xcp-sm-fs.spec

.PHONY: clean
clean:
	rm -f *.cmx *.cmo *.cmi idl toplevel
	${MAKE} -C ocaml clean
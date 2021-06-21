rpmbuild_src = $(shell rpmbuild --eval '%{_sourcedir}')
nginx_ver := 1.20.1

%.spec: %.spec.in
	sed -e 's/@NGINXVER@/$(nginx_ver)/g' $< > $@

.PHONY: prepare
prepare: $(spec)
	dnf -y install rpmdevtools rpm-build
	cp *.* $(rpmbuild_src)
	spectool -g -R $(spec)

.PHONY: srpm
srpm: prepare
	rpmbuild -bs --define "_srcrpmdir $(outdir)" $(spec)

.PHONY: rpm
rpm: prepare
	rpmbuild -bb --define "_rpmdir $(outdir)" $(spec)

## RHEL / CentOS 7 source for building python-nagiosplugin

### Usage:

1. Clone this repo
2. Copy SOURCES and SPECS to ~/rpmbuild/
3. Build the package (and source package if you wish):
```bash
cd ~/rpmbuild/SPECS
rpmbuild -ba python-nagiosplugin.spec
```

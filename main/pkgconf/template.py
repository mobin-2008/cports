pkgname = "pkgconf"
pkgver = "1.9.5"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
checkdepends = ["kyua"]
provides = [f"pc:libpkgconf={pkgver}"]
pkgdesc = "Provides compiler and linker configuration"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://pkgconf.org"
source = f"https://distfiles.dereferenced.org/pkgconf/pkgconf-{pkgver}.tar.xz"
sha256 = "1ac1656debb27497563036f7bffc281490f83f9b8457c0d60bcfb638fb6b6171"
hardening = ["!cfi"]  # TODO
# checkdepends not available yet
options = ["bootstrap", "!check"]


def post_install(self):
    self.install_license("COPYING")

    self.install_link("pkgconf", "usr/bin/pkg-config")
    self.install_link("pkgconf.1", "usr/share/man/man1/pkg-config.1")


@subpackage("libpkgconf")
def _lib(self):
    self.pkgdesc += " (runtime library)"
    return self.default_libs()


@subpackage("pkgconf-devel")
def _devel(self):
    self.options = ["!scanpkgconf"]
    # pkg.m4 must remain in main package
    return [
        "usr/include",
        "usr/lib/pkgconfig",
        "usr/lib/*.so",
        "usr/lib/*.a",
    ]

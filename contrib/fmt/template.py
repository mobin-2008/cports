pkgname = "fmt"
pkgver = "10.0.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
]
# FIXME: random musl issues
make_check_args = ["-E", "(chrono|format|unicode|xchar)"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "python",
]
pkgdesc = "Formatting library for C++"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://fmt.dev/latest/index.html"
source = (
    f"https://github.com/fmtlib/fmt/releases/download/{pkgver}/fmt-{pkgver}.zip"
)
sha256 = "4943cb165f3f587f26da834d3056ee8733c397e024145ca7d2a8a96bb71ac281"
# FIXME: cfi test failures
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE.rst")


@subpackage("fmt-devel")
def _devel(self):
    return self.default_devel()

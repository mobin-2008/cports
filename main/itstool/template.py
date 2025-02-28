pkgname = "itstool"
pkgver = "2.0.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["python", "libxml2-python"]
makedepends = list(hostmakedepends)
depends = list(makedepends)
pkgdesc = "ITS Tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://itstool.org"
source = f"http://files.itstool.org/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "6b9a7cd29a12bb95598f5750e8763cee78836a1a207f85b74d8b3275b27e87ca"
hardening = ["vis", "cfi"]

configure_gen = []

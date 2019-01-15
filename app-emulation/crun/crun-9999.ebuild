# Copyright 1999-2014 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2

EAPI=7

inherit eutils
inherit autotools

DESCRIPTION="A lightweight fully featured OCI runtime and C library for running containers"

HOMEPAGE="https://github.com/giuseppe/crun"
if [[ ${PV} == 9999 ]]; then
	inherit git-r3
	EGIT_REPO_URI="https://github.com/giuseppe/crun.git"
else
	SRC_URI="https://github.com/giuseppe/${PN}/archive/v${PV}.tar.gz"
fi
LICENSE="GPL-3"

SLOT="0"
KEYWORDS="amd64 x86 ~amd64-linux"
IUSE="python"
BDEPEND=""
RDEPEND="
dev-libs/yajl
"
src_prepare() {
	default
	eautoreconf
}
src_configure() {
	econf $(use_enable python with-python-bindings)
}

src_compile() {
	emake OPTIM="" DEBUG="" \
		CC="$(tc-getCC)" AR="$(tc-getAR)"
}

src_install() {
	emake DESTDIR="${ED}" PREFIX="/usr" \
		libdir="/usr/$(get_libdir)" install
	#TODO, going to bed: python_foreach_impl configure has PYTHON_VERSION
	dodoc README.md
	dodoc COPYING.libcrun
}

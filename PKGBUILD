pkgname=pokenux
pkgver=0.0.1
pkgrel=1
pkgdesc="Pokénux CLI"
arch=('any')
depends=('python')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')

package() {
  python -m installer --destdir="$pkgdir" "${startdir}/dist/pokenux-${pkgver}-py3-none-any.whl"
}

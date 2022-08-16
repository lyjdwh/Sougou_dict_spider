pkgname=fcitx5-pinyin-sougou
pkgver=20220817
_reponame=Sougou_dict_spider
pkgrel=1
pkgdesc="Fcitx 5 Pinyin Dictionary from https://pinyin.sogou.com/dict/"
arch=('any')
url="https://github.com/lyjdwh/Sougou_dict_spider"
license=('Unlicense' 'cc-by-nc-sa-3.0')
source=("https://github.com/lyjdwh/${_reponame}/releases/download/${pkgver}/sougou.dict")
sha256sums=('689c5016a37f0462dfdab70322ac5ab9b563fa78c2b5fb47d7e71d6ee530b8d4')

package() {
    install -Dm644 sougou.dict -t ${pkgdir}/usr/share/fcitx5/pinyin/dictionaries/
}

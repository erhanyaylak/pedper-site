# pedper.com

PedPer Publishing web sitesi, logo dosyaları ve marka kiti.

## Klasörler

| Klasör | İçerik |
|---|---|
| `docs/` | Yayına hazır site (6 sayfa). Sunucuya yüklenecek ya da GitHub/Cloudflare Pages ile yayınlanacak klasör budur. |
| `src/` | Siteyi ve logoları üreten kaynaklar. Sayfa içerikleri `src/build_site.py` içindedir. |
| `brand/` | Marka kiti (PDF + HTML) ve logolar (`brand/logo/`: SVG, `brand/logo/png/`: şeffaf PNG). |

## Siteyi yeniden üretmek

```bash
pip install fonttools          # yalnızca logoları yeniden üretmek için gerekir
python3 src/logos.py           # brand/logo/*.svg dosyalarını üretir
python3 src/build_site.py      # docs/ klasörünü üretir
```

`docs/` içindeki her HTML dosyası tek başına çalışır: stil ve logolar sayfanın içine gömülüdür.

## Yayın

Site Cloudflare Workers üzerinde yayınlanır (`wrangler.jsonc`, statik dosyalar `docs/` klasöründen). `main` dalına yapılan her gönderim siteyi otomatik olarak yeniden yayınlar.

## Sayfalar

`index.html` (ana sayfa), `about.html`, `journals.html`, `authors.html`, `policies.html`, `contact.html`

## İçerik kaynağı

Dergi bilgileri https://pedagogicalperspective.com/index.php/pub adresinden alınmıştır (Kasım 2026).

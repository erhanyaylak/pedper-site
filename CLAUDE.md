# Claude için talimatlar

Bu depo pedper.com sitesini içerir. Kullanıcı Türkçe yazar; yanıtlar Türkçe olmalı.

## Güncelleme kuralları

- `docs/` klasöründeki HTML dosyalarını **elle düzenleme**. İçerik `src/build_site.py` içindedir; değişikliği orada yap, sonra `python3 src/build_site.py` çalıştır.
- Logo geometrisi `src/faces_final.json` içindedir (izometrik çift P; kenarlar yalnızca 90°, 30° ve 150° yönlerinde olmalı). Logoyu değiştirdikten sonra `python3 src/logos.py`, ardından `python3 src/build_site.py` çalıştır.
- Marka: Montserrat; renkler Koyu Mor `#4A2E83`, Marka Moru `#6E52A3`, Logo Lavanta `#8C7BC4`, Lavanta `#A68CC8`, Açık Lavanta `#E6DEFA`, Gece Moru `#281A52`. Ayrıntılar `brand/PedPer-Marka-Kiti.pdf` içinde.
- Yayıncı iletişim e-postası her yerde `info@pedagogicalperspective.com` olmalı (`info@pedper.com` kullanılmaz).
- Dergi bilgileri (güncel sayı, sayı sayısı, indeksler, politikalar) için kaynak: https://pedagogicalperspective.com/index.php/pub — güncellemeden önce oradan doğrula, bilgi uydurma.
- Değişiklikten sonra sayfaların ekran görüntüsünü masaüstü (1440 px) ve mobil (390 px) boyutta alıp kontrol et.

## Sık yapılan güncellemeler

- **Yeni sayı:** `build_site.py` içinde ana sayfadaki "Current issue", istatistik bandındaki sayı adedi, `journals.html` bölümündeki `issues` listesi ve jcover üzerindeki "Vol. · No." etiketleri.
- **Yeni indeks:** ana sayfadaki "Indexed in" satırı, istatistik bandındaki indeks sayısı ve `journals.html` indeks kartları.

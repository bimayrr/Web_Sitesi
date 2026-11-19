# Bimayr | Apps & Data Studio

Bimayr’in kurumsal tanıtım sitesi: **https://www.bimayr.com**

Saf HTML, CSS ve JavaScript ile yazıldı. Kurulum veya derleme gerektirmez.

## Yayın

| Parça | Nerede |
| --- | --- |
| Alan adı | Hostinger (`bimayr.com`, otomatik yenileme açık) |
| Barındırma | Vercel, bu depoya bağlı |
| Kaynak kod | Bu depo, `main` dalı |

`main` dalına gönderilen her değişiklik birkaç dakika içinde Vercel tarafından otomatik olarak bimayr.com’da yayınlanır. Ayrıca bir işlem gerekmez.

## Klasör yapısı

```
Web_Sitesi/
├── index.html                    Ana sayfa: yapı ve içerik
├── kvkk.html                     KVKK Aydınlatma Metni sayfası
├── css/style.css                 Renkler, yazı stilleri, animasyonlar
├── js/main.js                    Açılış, mobil menü, kaydırma animasyonları, teklif formu
├── assets/                       Logo dosyaları (SVG) ve favicon
├── google7608ff42e5855037.html   Google Search Console doğrulama dosyası (silmeyin)
├── .nojekyll
└── README.md
```

## Yerelde çalıştırma

`index.html` dosyasını tarayıcıda açmanız yeterli. İsterseniz yerel sunucu da kullanabilirsiniz:

```bash
python -m http.server 8000
```

Ardından http://localhost:8000 adresini açın.

## Düzenleme rehberi

| Ne değişecek | Nerede |
| --- | --- |
| Metinler, projeler, SSS | `index.html` |
| Renkler | `css/style.css` içindeki `:root` değişkenleri |
| E-posta adresi | `index.html`, `kvkk.html` ve `js/main.js` içindeki `bimayrr@gmail.com` |
| Logo | `assets/` klasörü ve `index.html` içindeki `.mark` SVG’leri |
| KVKK metni | `kvkk.html` |

## Renkler

| Ad | Kod |
| --- | --- |
| Gece Siyahı | `#0C0607` |
| Bordo | `#7A1730` |
| Parlak Bordo | `#A62644` |
| Krem | `#F4EDE0` |

## Yazı tipleri

Hepsi Google Fonts üzerinden yüklenir.

- **Inter Tight:** başlıklar
- **Manrope:** metinler, menü ve düğmeler
- **Fraunces:** yalnızca “BMA” logo rozeti ve alt bölümdeki italik slogan vurgusu

## Notlar

- Teklif formu bir sunucuya veri göndermez. Ziyaretçi KVKK onay kutusunu işaretleyip “Gönder”e basınca kendi e-posta uygulaması hazır bir taslakla açılır. Formun doğrudan gelen kutusuna düşmesini isterseniz Formspree gibi bir form servisi bağlayabilirsiniz. Bu durumda `kvkk.html` içindeki aktarım bölümü de güncellenmelidir.
- `kvkk.html` genel bir şablondur. Veri sorumlusu olarak şirketin resmî unvanı ve adresi eklenmeli, metin bir hukukçuya kontrol ettirilmelidir.
- “Seçilmiş çalışmalar” bölümündeki projeler ve rakamlar örnek içeriktir. Gerçek projelerle değiştirilmelidir.
- Animasyonlar, işletim sisteminde “hareketi azalt” ayarı açık olan ziyaretçilerde otomatik olarak kapanır.

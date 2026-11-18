# Bimayr | Apps & Data Studio

Bimayr’in tanıtım sitesi. Saf HTML, CSS ve JavaScript ile yazıldı. Kurulum veya derleme gerektirmez.

## Klasör yapısı

```
bimayr-site/
├── index.html          Sayfa yapısı ve içerik
├── css/style.css       Renkler, yazı stilleri ve animasyonlar
├── js/main.js          Açılış perdesi, kaydırma animasyonları, teklif formu
├── assets/             Logo dosyaları (SVG) ve favicon
├── .nojekyll
└── README.md
```

## Yerelde çalıştırma

`index.html` dosyasını tarayıcıda açmanız yeterli. İsterseniz yerel sunucu da kullanabilirsiniz:

```bash
python3 -m http.server 8000
```

Ardından http://localhost:8000 adresini açın.

## GitHub Pages ile yayınlama

1. GitHub’da yeni bir depo (repository) oluşturun, örneğin `bimayr-site`.
2. Bu klasördeki tüm dosyaları depoya yükleyin.
3. **Settings → Pages** bölümünde **Source** olarak **Deploy from a branch** seçin.
4. Branch olarak `main`, klasör olarak `/ (root)` seçip kaydedin.
5. Birkaç dakika sonra site `https://KULLANICI_ADI.github.io/bimayr-site/` adresinde yayında olur.

Kendi alan adınızı bağlamak için aynı sayfadaki **Custom domain** alanını kullanın.

## Düzenleme rehberi

| Ne değişecek | Nerede |
| --- | --- |
| Metinler, projeler, SSS | `index.html` |
| Renkler | `css/style.css` içindeki `:root` değişkenleri |
| E-posta adresi | `index.html` içinde `bimayrr@gmail.com` ve `js/main.js` içindeki form kodu |
| Logo | `assets/` klasörü ve `index.html` içindeki `.mark` SVG’leri |

## Renkler

| Ad | Kod |
| --- | --- |
| Gece Siyahı | `#0C0607` |
| Bordo | `#7A1730` |
| Parlak Bordo | `#A62644` |
| Krem | `#F4EDE0` |

## Yazı tipleri

Başlıklar için **Fraunces**, metinler için **Manrope**. İkisi de Google Fonts üzerinden yüklenir.

## Notlar

- Teklif formu bir sunucuya veri göndermez. “Gönder” düğmesine basınca ziyaretçinin e-posta uygulaması hazır bir taslakla açılır. Formun doğrudan gelen kutusuna düşmesini isterseniz Formspree gibi bir form servisi bağlayabilirsiniz.
- “Seçilmiş çalışmalar” bölümündeki projeler ve rakamlar örnek içeriktir. Yayına almadan önce gerçek projelerinizle değiştirin.

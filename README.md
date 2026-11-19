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
├── assets/fonts/                 Siteye gömülü yazı tipleri (Google’a bağlantı yok)
├── projeler/                     6 ürün konseptinin detay sayfaları ve proje.css
├── araclar/projeler_uret.py      Proje kartlarını ve detay sayfalarını üreten betik
├── araclar/surumle.py            CSS/JS bağlantılarına sürüm ekler (önbellek için)
├── google7608ff42e5855037.html   Google Search Console doğrulama dosyası (silmeyin)
├── vercel.json                   Önbellek süreleri (CSS, JS, yazı tipleri 1 yıl)
├── .vercelignore                 araclar/ klasörünün yayına çıkmasını engeller
├── .nojekyll
└── README.md
```

## Proje sayfalarını düzenleme

Ana sayfadaki “Seçilmiş çalışmalar” kartları ve `projeler/` altındaki sayfalar elle değil, `araclar/projeler_uret.py` betiğiyle üretilir. Bir projenin metnini, rengini, özelliklerini veya ekran içeriğini değiştirmek için:

1. `araclar/projeler_uret.py` içinde ilgili projeyi bulun:
   - Proje bilgileri ve renkler: `P` listesi
   - Telefon ekranlarındaki isimler ve tutarlar: `EKRAN_VERI`
   - Kart ve giriş arka plan renkleri: `KART_TEMALARI["b"]`
2. Depo klasöründe şu komutu çalıştırın:

   ```bash
   python araclar/projeler_uret.py .
   ```

3. Ardından sürüm betiğini çalıştırın (aşağıya bakın).
4. Değişen dosyaları GitHub’a gönderin. Vercel siteyi otomatik günceller.

Betik `index.html` içindeki kart bölümünü ve `projeler/` klasörünü yeniden yazar. Bu alanlarda elle yapılan değişiklikler bir sonraki çalıştırmada kaybolur.

## Önemli: CSS veya JS değiştirdikten sonra

`css/style.css`, `js/main.js` ve `projeler/proje.css` ziyaretçinin tarayıcısında 1 yıl önbellekte tutulur (hız için). Değişikliğin herkese ulaşması için, bu dosyalardan birini değiştirdikten sonra şu komutu çalıştırın:

```bash
python araclar/surumle.py .
```

Betik, HTML’deki bağlantıların sonuna dosyanın içeriğine göre yeni bir `?v=...` sürümü yazar. Böylece tarayıcı yeni dosyayı indirir. Çalıştırılmazsa eski ziyaretçiler eski stili görmeye devam eder.

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

Yazı tipleri `assets/fonts/` klasöründen, sitenin kendi sunucusundan yüklenir (lisans: SIL OFL 1.1).

- **Inter Tight:** başlıklar
- **Manrope:** metinler, menü ve düğmeler
- **Fraunces:** yalnızca “BMA” logo rozeti ve alt bölümdeki italik slogan. Dosya boyutunu küçültmek için sadece bu harfleri içerir. Bu yazı tipiyle yeni bir metin yazılacaksa dosyanın yeniden üretilmesi gerekir.

## Notlar

- Teklif formu bir sunucuya veri göndermez. Ziyaretçi KVKK onay kutusunu işaretleyip “Gönder”e basınca kendi e-posta uygulaması hazır bir taslakla açılır. Formun doğrudan gelen kutusuna düşmesini isterseniz Formspree gibi bir form servisi bağlayabilirsiniz. Bu durumda `kvkk.html` içindeki aktarım bölümü de güncellenmelidir.
- `kvkk.html` genel bir şablondur. Veri sorumlusu olarak şirketin resmî unvanı ve adresi eklenmeli, metin bir hukukçuya kontrol ettirilmelidir.
- “Seçilmiş çalışmalar” bölümündeki projeler ve rakamlar örnek içeriktir. Gerçek projelerle değiştirilmelidir.
- Açılış perdesi korunmuştur. Başlık ve açıklama perdenin arkasında hemen çizilir, böylece Google’ın hız ölçümü (LCP) perdeyi beklemez.
- Animasyonlar, işletim sisteminde “hareketi azalt” ayarı açık olan ziyaretçilerde otomatik olarak kapanır.

"""Bimayr 'Seçilmiş çalışmalar' bölümü + proje detay sayfaları üretici.
Kullanım: python projeler_uret.py <site_klasoru>
"""
import sys, pathlib, html as H

ROOT = pathlib.Path(sys.argv[1])

P = [
 dict(slug="kumbara", ad="Kumbara", sektor="Finans", platform="iOS · Android · Web paneli", sure="14 hafta",
  tag="Harcamanı anla, birikimi otomatiğe bağla.",
  ozet="Kişisel bütçe uygulaması. Harcamaları otomatik kategorize eder, kişiye özel tasarruf hedefleri önerir.",
  renk=dict(ana="#0F3D2E", vurgu="#3DDC97", acik="#E8F7EF", koyu="#082419"), renk_ad=["Orman", "Nane", "Sis", "Gece"],
  logo="kumbara", ekran=["ozet", "liste", "hedef"],
  problem="Gençlerin çoğu ay sonunu nasıl getirdiğini bilmiyor. Banka uygulamaları işlemleri listeliyor ama yorumlamıyor; elle tutulan bütçe tabloları ise ikinci haftada bırakılıyor.",
  cozum="Kumbara, banka hareketlerini otomatik sınıflandırır, harcama alışkanlıklarını sade grafiklerle anlatır ve küçük, ulaşılabilir tasarruf hedefleri kurar. ‘Yuvarla ve biriktir’ özelliği her harcamayı en yakın 5 ₺’ye tamamlayıp farkı kumbaraya atar.",
  persona=dict(ad="Elif, 26", rol="Yazılım uzmanı, İstanbul", soz="Maaş yatıyor, iki hafta sonra nereye gittiğini bilmiyorum. Bana sadece ‘şunu azalt’ diyen biri lazım.", ten="#E8B894", sac="#3B2418"),
  ozellik=[("Otomatik kategori","Market, ulaşım, abonelik… İşlemler yapay zekâ ile sınıflanır."),("Yuvarla ve biriktir","Her harcamadaki küsurat otomatik olarak birikime aktarılır."),("Akıllı hedefler","Gelire göre gerçekçi aylık tasarruf hedefi önerilir."),("Abonelik avcısı","Unutulmuş abonelikleri bulur, iptal hatırlatması gönderir."),("Haftalık özet","Pazar akşamı tek ekranlık, anlaşılır bir rapor."),("Aile kumbarası","Ortak hedefler için paylaşımlı birikim hesabı.")],
  yolculuk=["Banka hesabını güvenle bağlar","İlk hafta harcama haritasını görür","İlk hedefini kurar","Yuvarlamayı açar","Ay sonunda ilk birikimini görür"],
  kpi=[("Haftalık aktif kullanıcı","%45"),("İlk hedef kurma oranı","%60"),("30. gün elde tutma","%40"),("Kullanıcı başı aylık birikim","₺750")],
  teknoloji=["React Native","Node.js","PostgreSQL","Açık bankacılık API","BigQuery","Mixpanel"],
  yol=[("MVP · 8 hafta","Hesap bağlama, otomatik kategori, haftalık özet"),("Sürüm 1 · 4 hafta","Hedefler, yuvarla ve biriktir, bildirimler"),("Büyüme · sürekli","Abonelik avcısı, aile kumbarası, A/B testleri")]),
 dict(slug="rota", ad="Rota", sektor="Seyahat", platform="iOS · Android · Web", sure="16 hafta",
  tag="Çok şehirli geziyi tek ekranda planla.",
  ozet="Çok şehirli gezi planlayıcı. Rezervasyon verisinden beslenen öneri motoruyla rotayı kişiye göre kurar.",
  renk=dict(ana="#12264F", vurgu="#FF6B4A", acik="#F6E7D2", koyu="#0A1733"), renk_ad=["Lacivert", "Mercan", "Kum", "Gece"],
  logo="rota", ekran=["harita", "liste", "ozet"],
  problem="Birden fazla şehri kapsayan bir gezi planlamak; uçak, tren, otel ve etkinlik için ayrı ayrı onlarca sekme açmak demek. Gezginler saatlerce plan yapıyor ve yine de aktarmaları kaçırıyor.",
  cozum="Rota, kullanıcının tarihlerini ve ilgi alanlarını alıp şehirler arası ulaşımı, konaklamayı ve günlük planı tek bir zaman çizelgesinde birleştirir. Gecikme olduğunda planı otomatik yeniden düzenler.",
  persona=dict(ad="Can, 31", rol="Pazarlama müdürü, Ankara", soz="Yılda iki kez Avrupa’ya gidiyorum. Planlamak, gezmekten daha yorucu.", ten="#C68B5E", sac="#1E1A17"),
  ozellik=[("Akıllı rota","Şehir sırasını süre ve bütçeye göre en iyi hâle getirir."),("Tek zaman çizelgesi","Uçuş, tren, otel ve etkinlik aynı akışta."),("Canlı yeniden planlama","Gecikmede aktarmaları ve rezervasyonları günceller."),("Yerel öneriler","Benzer gezginlerin beğendiği yerler."),("Ortak plan","Arkadaşlarla birlikte düzenleme ve oylama."),("Çevrim dışı mod","İnternet olmadan da plan ve biletler cepte.")],
  yolculuk=["Tarih ve şehirleri seçer","Önerilen rotayı inceler","Tek tıkla rezervasyon yapar","Gezide canlı bildirim alır","Dönüşte anılarını paylaşır"],
  kpi=[("Plan → rezervasyon dönüşümü","%18"),("Ortalama planlama süresi","< 20 dk"),("Gezi başı rezervasyon","3,5"),("Tekrar kullanım (12 ay)","%35")],
  teknoloji=["Flutter","Python","Rezervasyon API’leri","Mapbox","Snowflake","Öneri modeli"],
  yol=[("MVP · 9 hafta","Rota oluşturma, zaman çizelgesi, otel ve uçuş arama"),("Sürüm 1 · 4 hafta","Rezervasyon, canlı bildirimler, çevrim dışı mod"),("Büyüme · sürekli","Öneri motoru, ortak plan, ortaklık gelirleri")]),
 dict(slug="tempo", ad="Tempo", sektor="SaaS", platform="Web paneli · API", sure="12 hafta",
  tag="Abonelik işinin nabzını tek panelde tut.",
  ozet="Abonelik işletmeleri için gelir ve churn paneli. Veri hattı ve kayıp tahmin modeliyle birlikte teslim edilir.",
  renk=dict(ana="#23246B", vurgu="#7B61FF", acik="#EEF0FF", koyu="#14154A"), renk_ad=["Çivit", "Elektrik", "Buz", "Gece"],
  logo="tempo", ekran=["grafik", "ozet", "liste"],
  problem="Abonelik şirketleri MRR, churn ve LTV gibi temel ölçümleri farklı araçlardan elle derliyor. Kaybedilecek müşteri ancak iptal ettikten sonra fark ediliyor.",
  cozum="Tempo, ödeme sistemi ve ürün verisini otomatik bir veri hattında birleştirir. Gelir panelleri gerçek zamanlı güncellenir; tahmin modeli kaybedilme riski yüksek müşterileri haftalık listeler ve ekibe aksiyon önerir.",
  persona=dict(ad="Selin, 34", rol="Kurucu ortak, B2B SaaS", soz="Yatırımcı toplantısından önce rakamları üç farklı yerden topluyorum. Hep bir şey eksik kalıyor.", ten="#F1C7A3", sac="#6B3B1F"),
  ozellik=[("Gelir paneli","MRR, ARR, LTV ve büyüme tek ekranda."),("Kayıp tahmini","Riskli müşteriler, nedenleriyle birlikte."),("Kohort analizi","Hangi ay gelen müşteri ne kadar kalıyor?"),("Otomatik rapor","Haftalık yönetim raporu e-postaya gelir."),("Uyarılar","Ani düşüşlerde Slack bildirimi."),("Açık API","Verini kendi araçlarına aktar.")],
  yolculuk=["Ödeme sistemini bağlar","İlk paneli 10 dakikada görür","Riskli müşteri listesini inceler","Ekibiyle aksiyon planlar","Aylık churn düşüşünü takip eder"],
  kpi=[("Kurulum süresi","< 1 gün"),("Aylık churn azalması","−%20"),("Haftalık aktif ekip","%70"),("Raporlamada zaman tasarrufu","8 saat/hafta")],
  teknoloji=["Next.js","dbt","BigQuery","Stripe API","Python (ML)","Metabase"],
  yol=[("MVP · 6 hafta","Veri hattı, gelir paneli, temel ölçümler"),("Sürüm 1 · 3 hafta","Kohortlar, otomatik raporlar, uyarılar"),("Büyüme · sürekli","Kayıp tahmin modeli, API, entegrasyon pazarı")]),
 dict(slug="klinik", ad="Klinik+", sektor="Sağlık", platform="iOS · Android · Klinik paneli", sure="14 hafta",
  tag="Randevuya gelmeyen hasta kalmasın.",
  ozet="Randevu ve hatırlatma uygulaması. Gelmeme oranını düşüren bildirim akışı A/B testleriyle bulunur.",
  renk=dict(ana="#0E6E78", vurgu="#5FD3C6", acik="#E6F6F6", koyu="#08464D"), renk_ad=["Okyanus", "Su", "Köpük", "Derin"],
  logo="klinik", ekran=["takvim", "liste", "ozet"],
  problem="Özel kliniklerde randevuların yaklaşık beşte biri haber verilmeden boş kalıyor. Telefonla hatırlatma personelin zamanını alıyor, boşalan saat de çoğu zaman doldurulamıyor.",
  cozum="Klinik+, hastaya doğru zamanda doğru kanaldan hatırlatma gönderir, tek dokunuşla onay veya erteleme alır. İptal edilen saat bekleme listesindeki hastaya otomatik teklif edilir.",
  persona=dict(ad="Dr. Murat, 45", rol="Diş kliniği sahibi, İzmir", soz="Boş geçen her saat hem gelir kaybı hem de bekleyen başka bir hastanın mağduriyeti.", ten="#D9A47E", sac="#8A8A8A"),
  ozellik=[("Akıllı hatırlatma","SMS, bildirim veya WhatsApp; hastaya en uygun kanal."),("Tek dokunuşla onay","Onayla, ertele ya da iptal et."),("Bekleme listesi","Boşalan saat otomatik olarak teklif edilir."),("Klinik paneli","Günlük doluluk ve gelmeme oranı."),("Hasta geçmişi","Ziyaretler ve notlar tek yerde."),("KVKK uyumu","Sağlık verisi için şifreli saklama.")],
  yolculuk=["Hasta online randevu alır","24 saat önce hatırlatma gelir","Tek dokunuşla onaylar","Klinik paneli günü planlar","Ziyaret sonrası memnuniyet sorusu"],
  kpi=[("Gelmeme oranı","%20 → %8"),("Boşalan saati doldurma","%50"),("Hatırlatma onay oranı","%75"),("Personel zaman tasarrufu","6 saat/hafta")],
  teknoloji=["Swift / Kotlin","Go","PostgreSQL","Twilio","WhatsApp Business API","Amplitude"],
  yol=[("MVP · 8 hafta","Online randevu, hatırlatmalar, klinik paneli"),("Sürüm 1 · 4 hafta","Bekleme listesi, WhatsApp, hasta geçmişi"),("Büyüme · sürekli","Bildirim A/B testleri, çoklu şube, raporlama")]),
 dict(slug="sepet", ad="Sepet", sektor="E-ticaret", platform="iOS · Android", sure="15 hafta",
  tag="Beğendiğin parça, üç dokunuşta kapında.",
  ozet="Butik moda markaları için mobil mağaza. Sepet terk analiziyle sadeleştirilmiş, üç adımlı ödeme akışı.",
  renk=dict(ana="#161214", vurgu="#E8A9B8", acik="#FBEFF1", koyu="#0B090A"), renk_ad=["Kömür", "Gül", "Pudra", "Gece"],
  logo="sepet", ekran=["urun", "liste", "ozet"],
  problem="Butik moda markalarının mobil sitelerinde ziyaretçilerin %70’ten fazlası sepete ekledikten sonra ödemeyi tamamlamıyor. Uzun formlar ve sürpriz kargo ücretleri en büyük nedenler.",
  cozum="Sepet, markaya özel bir mobil uygulama ve sadeleştirilmiş üç adımlı ödeme sunar. Beden önerisi iade oranını düşürür; sepette unutulan ürünler için zamanlanmış, kişisel hatırlatmalar gönderilir.",
  persona=dict(ad="Deniz, 29", rol="Mimar, İstanbul", soz="Telefondan alışveriş yapıyorum ama ödeme sayfası açılınca vazgeçiyorum. Çok uzun.", ten="#F0C6A8", sac="#2A1B14"),
  ozellik=[("Üç adımlı ödeme","Adres, ödeme, onay. Hepsi bu."),("Beden asistanı","Önceki alışverişlere göre beden önerisi."),("Akıllı hatırlatma","Sepette kalan ürün için doğru zamanda bildirim."),("Stil kombinleri","Ürünle uyumlu parçalar."),("Kolay iade","Uygulama içinden tek tıkla iade kodu."),("Sadakat puanı","Her alışverişte biriken puanlar.")],
  yolculuk=["Yeni koleksiyonu keşfeder","Beden asistanıyla seçer","Sepete ekler","Üç adımda öder","Kargoyu canlı takip eder"],
  kpi=[("Sepet tamamlama oranı","%30 → %45"),("Mobil dönüşüm oranı","%3,5"),("İade oranı","−%25"),("Tekrar satın alma (90 gün)","%30")],
  teknoloji=["React Native","Shopify API","Node.js","Algolia","Firebase","GA4"],
  yol=[("MVP · 8 hafta","Katalog, sepet, üç adımlı ödeme"),("Sürüm 1 · 4 hafta","Beden asistanı, hatırlatmalar, iade"),("Büyüme · sürekli","Kombin önerileri, sadakat, A/B testleri")]),
 dict(slug="orbit", ad="Orbit", sektor="Kurumsal", platform="Web portalı · Mobil", sure="20 hafta",
  tag="Dağınık sistemleri tek merkezde topla.",
  ozet="Şirket içi operasyon portalı. ERP, CRM ve tablolardaki veriyi tek veri ambarında toplayıp raporlar.",
  renk=dict(ana="#1E293B", vurgu="#F59E0B", acik="#EEF2F6", koyu="#0F172A"), renk_ad=["Arduvaz", "Kehribar", "Bulut", "Gece"],
  logo="orbit", ekran=["grafik", "liste", "ozet"],
  problem="Orta ölçekli şirketlerde satış ERP’de, müşteri CRM’de, operasyon Excel’de duruyor. Yöneticiler haftalık raporu hazırlamak için günlerce veri topluyor ve rakamlar ekipten ekibe değişiyor.",
  cozum="Orbit, tüm kaynakları tek bir veri ambarına bağlar ve her ekibe kendi panelini sunar. Rakamların tek bir doğruluk kaynağı olur; raporlar otomatik hazırlanır, onay akışları da aynı portaldan yürür.",
  persona=dict(ad="Ayşe, 41", rol="Operasyon direktörü, üretim şirketi", soz="Her pazartesi aynı soruyu soruyorum: Hangi rakam doğru?", ten="#E3B08E", sac="#4A2E1E"),
  ozellik=[("Tek veri ambarı","ERP, CRM ve tablolar tek merkezde."),("Ekip panelleri","Satış, operasyon ve finans için ayrı görünümler."),("Otomatik rapor","Haftalık yönetim raporu kendiliğinden hazır."),("Onay akışları","Satın alma ve izin onayları portalda."),("Rol bazlı yetki","Herkes sadece görmesi gerekeni görür."),("Mobil erişim","Sahadaki ekip için hafif mobil arayüz.")],
  yolculuk=["Mevcut sistemler bağlanır","Veri sözlüğü birlikte kurulur","Ekip panelleri devreye alınır","Raporlar otomatikleşir","Onay akışları portala taşınır"],
  kpi=[("Raporlamada zaman tasarrufu","12 saat/hafta"),("Panel kullanan yönetici oranı","%85"),("Veri tutarsızlığı","−%90"),("Onay süreci süresi","−%50")],
  teknoloji=["Vue.js","Python","Airbyte","PostgreSQL","dbt","Apache Superset"],
  yol=[("MVP · 10 hafta","Veri ambarı, iki kaynak bağlantısı, yönetim paneli"),("Sürüm 1 · 6 hafta","Ekip panelleri, otomatik raporlar, yetkiler"),("Büyüme · sürekli","Onay akışları, mobil, yeni entegrasyonlar")]),
]

e = H.escape

# ---------------- logolar (64x64, ana renk zemin üzerinde açık renkli işaret) ----------------
def logo(kind, c, size=64, bg=True):
    a, v, l = c["ana"], c["vurgu"], c["acik"]
    g = {
     "kumbara": f'<rect x="13" y="26" width="38" height="26" rx="11" fill="none" stroke="{l}" stroke-width="4"/><rect x="26" y="23" width="12" height="4" rx="2" fill="{l}"/><circle cx="32" cy="13" r="6.5" fill="{v}"/><path d="M32 10v6" stroke="{a}" stroke-width="2" stroke-linecap="round"/><path d="M22 39h20" stroke="{v}" stroke-width="3.5" stroke-linecap="round" opacity=".9"/>',
     "rota": f'<path d="M14 48c8-2 8-14 18-14s10-14 18-16" fill="none" stroke="{l}" stroke-width="3.5" stroke-dasharray="1 6" stroke-linecap="round"/><circle cx="14" cy="48" r="4.5" fill="{l}"/><path d="M50 10a8 8 0 0 1 8 8c0 6-8 14-8 14s-8-8-8-14a8 8 0 0 1 8-8z" fill="{v}"/><circle cx="50" cy="18" r="3" fill="{a}"/>',
     "tempo": f'<rect x="13" y="34" width="7" height="16" rx="2" fill="{l}"/><rect x="24" y="24" width="7" height="26" rx="2" fill="{l}"/><rect x="35" y="30" width="7" height="20" rx="2" fill="{l}"/><rect x="46" y="14" width="7" height="36" rx="2" fill="{v}"/>',
     "klinik": f'<rect x="14" y="14" width="36" height="36" rx="11" fill="none" stroke="{l}" stroke-width="4"/><path d="M32 22v20M22 32h20" stroke="{v}" stroke-width="5" stroke-linecap="round"/>',
     "sepet": f'<path d="M18 24h28l-3 26H21z" fill="none" stroke="{l}" stroke-width="3.5" stroke-linejoin="round"/><path d="M25 24v-3a7 7 0 0 1 14 0v3" fill="none" stroke="{v}" stroke-width="3.5"/><text x="32" y="44" text-anchor="middle" font-family="Inter Tight,sans-serif" font-weight="700" font-size="13" fill="{v}">S</text>',
     "orbit": f'<ellipse cx="32" cy="32" rx="22" ry="9" fill="none" stroke="{l}" stroke-width="3" transform="rotate(-25 32 32)"/><circle cx="32" cy="32" r="8" fill="{v}"/><circle cx="51" cy="22" r="3.5" fill="{l}"/>',
    }[kind]
    back = f'<rect width="64" height="64" rx="16" fill="{a}"/>' if bg else ""
    return f'<svg viewBox="0 0 64 64" width="{size}" height="{size}" aria-hidden="true">{back}{g}</svg>'

# ---------------- avatar ----------------
def avatar(ten, sac, bg, size=56):
    return (f'<svg viewBox="0 0 56 56" width="{size}" height="{size}" aria-hidden="true"><circle cx="28" cy="28" r="28" fill="{bg}"/>'
            f'<path d="M10 54c2-11 9-16 18-16s16 5 18 16" fill="{sac}" opacity=".9"/>'
            f'<circle cx="28" cy="24" r="10" fill="{ten}"/><path d="M17 23c0-8 5-12 11-12s11 4 11 12c-3-4-7-5-11-5s-8 1-11 5z" fill="{sac}"/></svg>')

# ---------------- telefon ekranları (180x360, gerçekçi arayüz) ----------------
EKRAN_VERI = {
 "kumbara": dict(baslik="Merhaba Elif", ozet_et="Bu ay biriktirdin", ozet_deger="₺2.480", ozet_alt="Hedefin %72’si",
   liste_baslik="Son hareketler", sekme=["Tümü","Gider","Gelir"],
   liste=[("M","Migros","Market","−₺412",0),("S","Spotify","Abonelik","−₺60",0),("İ","İstanbulkart","Ulaşım","−₺35",0),("K","Kumbara","Yuvarlama","+₺18",1),("A","Maaş","Gelir","+₺42.000",1),("Y","Yemeksepeti","Yemek","−₺285",0)],
   hedef=("Tatil hedefi","%72","₺7.200 / ₺10.000")),
 "rota": dict(baslik="Avrupa turu", ozet_et="Toplam bütçe", ozet_deger="€1.840", ozet_alt="9 gün · 3 şehir",
   liste_baslik="Gezi planı", sekme=["Plan","Bilet","Otel"],
   liste=[("U","İstanbul → Paris","12 Haz · 08:40","THY",2),("O","Hôtel Marais","3 gece","€420",2),("T","Paris → Lyon","15 Haz · 10:15","TGV",2),("O","Lyon Centre","2 gece","€190",2),("T","Lyon → Nice","17 Haz · 09:05","SNCF",2),("U","Nice → İstanbul","20 Haz · 18:30","Pegasus",2)],
   harita=["Paris","Lyon","Nice"]),
 "tempo": dict(baslik="Gelir paneli", ozet_et="Aylık yinelenen gelir", ozet_deger="₺1,24M", ozet_alt="+%8,4 geçen aya göre",
   liste_baslik="Kayıp riski yüksek", sekme=["Risk","Yeni","Tümü"],
   liste=[("A","Atlas Lojistik","Kullanım −%40","%82",0),("N","Nova Medya","Ödeme gecikti","%74",0),("D","Delta Yapı","Destek talebi ↑","%61",0),("P","Pera Butik","Paket düşürdü","%55",0),("K","Kuzey Enerji","Giriş yok · 14 gün","%49",0),("M","Mavi Eğitim","Sözleşme bitiyor","%41",0)],
   grafik=("MRR","₺1,24M","Churn","%2,1","LTV","₺86K")),
 "klinik": dict(baslik="Bugün · 12 Kasım", ozet_et="Bugünkü doluluk", ozet_deger="%92", ozet_alt="24 randevu · 2 boş",
   liste_baslik="Randevular", sekme=["Bugün","Yarın","Hafta"],
   liste=[("09","Ayşe Kaya","Dolgu · 30 dk","Onaylı",1),("10","Mert Demir","Kontrol · 20 dk","Onaylı",1),("11","Zeynep Ak","İmplant · 60 dk","Bekliyor",2),("13","Burak Şen","Temizlik · 40 dk","Onaylı",1),("14","Elif Can","Kanal · 45 dk","Boş → teklif",0),("15","Okan Yıldız","Kontrol · 20 dk","Onaylı",1)]),
 "sepet": dict(baslik="Yeni sezon", ozet_et="Sepetin", ozet_deger="₺3.240", ozet_alt="3 ürün · ücretsiz kargo",
   liste_baslik="Siparişlerim", sekme=["Aktif","Geçmiş","İade"],
   liste=[("K","Keten gömlek","Beden M · Krem","₺890",2),("T","Triko hırka","Beden S · Gül","₺1.250",2),("Ç","Deri çanta","Tek beden · Siyah","₺1.100",2),("E","Etek","Beden 36 · Kömür","₺740",2),("A","Atkı","Yün · Pudra","₺420",2),("S","Spor ayakkabı","38 · Beyaz","₺1.690",2)],
   urun=[("Keten gömlek","₺890"),("Triko hırka","₺1.250"),("Deri çanta","₺1.100"),("Pileli etek","₺740")]),
 "orbit": dict(baslik="Operasyon", ozet_et="Haftalık ciro", ozet_deger="₺18,6M", ozet_alt="Hedefin %104’ü",
   liste_baslik="Onay bekleyenler", sekme=["Onay","Rapor","Ekip"],
   liste=[("S","Satın alma #482","Hammadde · Ahmet Y.","₺84.000",2),("İ","İzin talebi","3 gün · Selin K.","İzin",2),("F","Fatura #1290","Tedarikçi · Ege Metal","₺212.400",2),("S","Satın alma #483","Ofis · Can T.","₺6.300",2),("B","Bütçe revizyonu","Pazarlama · Q4","₺450.000",2),("T","Transfer","Depo → Şube 2","42 palet",2)],
   grafik=("Ciro","₺18,6M","Stok","%87","Sipariş","1.284")),
}

def ekran(kind, p, w=180, h=360):
    c = p["renk"]; a, v, l, k = c["ana"], c["vurgu"], c["acik"], c["koyu"]
    D = EKRAN_VERI[p["slug"]]; uid = p["slug"] + kind
    T = lambda x, y, s, size=9, wt=500, fill=k, op=1, anchor="start", fam="Manrope": (
        f'<text x="{x}" y="{y}" font-family="{fam},sans-serif" font-weight="{wt}" font-size="{size}" fill="{fill}" opacity="{op}" text-anchor="{anchor}">{e(str(s))}</text>')
    defs = (f'<defs><linearGradient id="g{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{k}"/></linearGradient>'
            f'<linearGradient id="f{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{v}" stop-opacity=".35"/><stop offset="1" stop-color="{v}" stop-opacity="0"/></linearGradient></defs>')
    top = (f'<rect width="{w}" height="{h}" fill="#F7F7F9"/>'
           + T(16, 18, "9:41", 8, 700) + f'<rect x="146" y="12" width="16" height="7" rx="2" fill="none" stroke="{k}" stroke-width="1"/><rect x="147.5" y="13.5" width="10" height="4" rx="1" fill="{k}"/>'
           + f'<g transform="translate(14 30)">{logo(p["logo"], c, 22)}</g>' + T(42, 40, p["ad"], 8, 700, k, .55) + T(42, 51, D["baslik"], 10.5, 700, k, 1, fam="Inter Tight")
           + f'<circle cx="157" cy="41" r="9" fill="{v}"/>' + T(157, 44.5, D["baslik"][0], 8, 700, a, 1, "middle"))
    def row(y, it, wv=152):
        ic, ad, alt, deger, tip = it
        col = {0: "#D64545", 1: "#1E9E62", 2: k}[tip]
        if p["slug"] == "tempo": col = "#D64545"
        bg_ic = [v, a, l][sum(map(ord, ad)) % 3] if tip != 2 else (v if sum(map(ord, ad)) % 2 else a)
        fg_ic = a if bg_ic in (v, l) else l
        s = f'<rect x="14" y="{y}" width="{wv}" height="34" rx="10" fill="#fff"/>'
        s += f'<rect x="20" y="{y+6}" width="22" height="22" rx="7" fill="{bg_ic}"/>' + T(31, y + 20.5, ic, 9 if len(ic) == 1 else 8, 700, fg_ic, 1, "middle")
        s += T(48, y + 15, ad, 8.5, 700) + T(48, y + 26, alt, 7, 500, k, .5)
        s += T(14 + wv - 7, y + 20, deger, 8, 700, col, 1, "end")
        return s
    def chips(y):
        s = ""; x = 14
        for i, t in enumerate(D["sekme"]):
            wd = 10 + len(t) * 5.2
            s += f'<rect x="{x}" y="{y}" width="{wd}" height="18" rx="9" fill="{a if i == 0 else "#fff"}"/>' + T(x + wd / 2, y + 12, t, 7.5, 700, l if i == 0 else k, 1 if i == 0 else .6, "middle")
            x += wd + 6
        return s
    def ozet_kart(y, hh=92):
        bars = [14, 22, 17, 28, 24, 34, 30]
        s = f'<rect x="14" y="{y}" width="152" height="{hh}" rx="16" fill="url(#g{uid})"/><circle cx="144" cy="{y+28}" r="22" fill="{v}" opacity=".16"/>'
        s += T(26, y + 20, D["ozet_et"], 8, 600, l, .75) + T(26, y + 44, D["ozet_deger"], 21 if len(D["ozet_deger"]) <= 7 else 17, 700, "#fff", 1, fam="Inter Tight")
        s += T(26, y + 58, D["ozet_alt"], 7.5, 600, v)
        for i, b in enumerate(bars):
            s += f'<rect x="{104 + i * 8}" y="{y + hh - 12 - b}" width="5" height="{b}" rx="2.5" fill="{v if i == 5 else l}" opacity="{1 if i == 5 else .35}"/>'
        return s
    body = ""
    if kind == "ozet":
        body = ozet_kart(64) + T(14, 176, D["liste_baslik"], 9.5, 700, fam="Inter Tight") + T(166, 176, "Tümü", 7.5, 700, v if v not in ("#E8A9B8",) else a, 1, "end") + "".join(row(184 + i * 40, it) for i, it in enumerate(D["liste"][:4]))
    elif kind == "liste":
        body = T(14, 80, D["liste_baslik"], 13, 700, fam="Inter Tight") + chips(88) + "".join(row(116 + i * 40, it) for i, it in enumerate(D["liste"][:6]))
    elif kind == "grafik":
        g = D["grafik"]
        body = (f'<rect x="14" y="64" width="152" height="122" rx="16" fill="#fff"/>' + T(26, 84, g[0], 8, 600, k, .55) + T(26, 104, g[1], 18, 700, k, 1, fam="Inter Tight")
                + f'<rect x="118" y="74" width="38" height="16" rx="8" fill="{v}" opacity=".18"/>' + T(137, 85, "+%8,4", 7.5, 700, a, 1, "middle")
                + f'<path d="M26 170 C44 164 52 150 68 152 S96 132 112 136 S140 112 156 108 V176 H26z" fill="url(#f{uid})"/>'
                + f'<path d="M26 170 C44 164 52 150 68 152 S96 132 112 136 S140 112 156 108" fill="none" stroke="{v}" stroke-width="2.6" stroke-linecap="round"/><circle cx="156" cy="108" r="4" fill="#fff" stroke="{v}" stroke-width="2.4"/>'
                + "".join(T(30 + i * 25, 182, m, 6.5, 600, k, .4) for i, m in enumerate(["Haz","Tem","Ağu","Eyl","Eki","Kas"]))
                + f'<rect x="14" y="196" width="73" height="54" rx="14" fill="url(#g{uid})"/>' + T(24, 214, g[2], 7.5, 600, l, .7) + T(24, 236, g[3], 15, 700, "#fff", 1, fam="Inter Tight")
                + f'<rect x="93" y="196" width="73" height="54" rx="14" fill="#fff"/>' + T(103, 214, g[4], 7.5, 600, k, .55) + T(103, 236, g[5], 15, 700, k, 1, fam="Inter Tight")
                + T(14, 272, D["liste_baslik"], 9.5, 700, fam="Inter Tight") + "".join(row(280 + i * 40, it) for i, it in enumerate(D["liste"][:2])))
    elif kind == "hedef":
        ad, yuzde, alt = D["hedef"]
        body = (f'<rect x="14" y="64" width="152" height="150" rx="18" fill="#fff"/>'
                f'<circle cx="90" cy="134" r="48" fill="none" stroke="{l}" stroke-width="12"/>'
                f'<circle cx="90" cy="134" r="48" fill="none" stroke="url(#g{uid})" stroke-width="12" stroke-dasharray="217 302" transform="rotate(-90 90 134)" stroke-linecap="round"/>'
                + T(90, 134, yuzde, 20, 700, k, 1, "middle", "Inter Tight") + T(90, 148, ad, 7.5, 600, k, .55, "middle") + T(90, 204, alt, 8, 700, a, 1, "middle")
                + T(14, 236, "Bu hafta", 9.5, 700, fam="Inter Tight") + "".join(row(244 + i * 40, it) for i, it in enumerate([D["liste"][3], D["liste"][0], D["liste"][1]])))
    elif kind == "harita":
        sehir = D["harita"]
        body = (f'<rect x="14" y="64" width="152" height="164" rx="18" fill="{l}"/>'
                + "".join(f'<rect x="{20 + (i * 37) % 130}" y="{72 + (i * 23) % 140}" width="{22 + (i * 7) % 20}" height="{14 + (i * 5) % 12}" rx="4" fill="#fff" opacity=".7"/>' for i in range(14))
                + f'<path d="M14 150 C60 140 80 180 166 160" stroke="#fff" stroke-width="7" fill="none" opacity=".9"/>'
                + f'<path d="M44 96 C70 110 66 150 92 160 S136 186 144 206" fill="none" stroke="{v}" stroke-width="3" stroke-dasharray="1 6" stroke-linecap="round"/>'
                + f'<circle cx="44" cy="96" r="6" fill="{a}" stroke="#fff" stroke-width="2"/><circle cx="92" cy="160" r="6" fill="{a}" stroke="#fff" stroke-width="2"/><circle cx="144" cy="206" r="7" fill="{v}" stroke="#fff" stroke-width="2"/>'
                + f'<rect x="52" y="84" width="34" height="14" rx="7" fill="{k}"/>' + T(69, 94, sehir[0], 7, 700, "#fff", 1, "middle")
                + f'<rect x="100" y="150" width="30" height="14" rx="7" fill="{k}"/>' + T(115, 160, sehir[1], 7, 700, "#fff", 1, "middle")
                + f'<rect x="104" y="188" width="30" height="14" rx="7" fill="{k}"/>' + T(119, 198, sehir[2], 7, 700, "#fff", 1, "middle")
                + "".join(row(240 + i * 40, it) for i, it in enumerate(D["liste"][:3])))
    elif kind == "takvim":
        gun = ["Pt","Sa","Ça","Pe","Cu","Ct","Pz"]
        cells = "".join(f'<rect x="{16 + i * 21.5}" y="68" width="18" height="34" rx="9" fill="{a if i == 2 else "#fff"}"/>' + T(25 + i * 21.5, 80, gun[i], 6.5, 600, l if i == 2 else k, .9 if i == 2 else .5, "middle") + T(25 + i * 21.5, 95, 10 + i, 9, 700, "#fff" if i == 2 else k, 1, "middle") for i in range(7))
        body = cells + ozet_kart(112, 76).replace(f'y="{112 + 76 - 12 - 34}"', f'y="{112 + 76 - 12 - 34}"') + T(14, 208, D["liste_baslik"], 9.5, 700, fam="Inter Tight") + "".join(row(216 + i * 40, it) for i, it in enumerate(D["liste"][:4]))
    elif kind == "urun":
        tiles = ""
        for i, (ad, fiyat) in enumerate(D["urun"]):
            x, y = 14 + (i % 2) * 78, 86 + (i // 2) * 118
            bg = [v, a, l, k][i]
            tiles += f'<rect x="{x}" y="{y}" width="74" height="110" rx="14" fill="#fff"/><rect x="{x+6}" y="{y+6}" width="62" height="68" rx="10" fill="{bg}" opacity="{.9 if bg != l else 1}"/>'
            if i in (0, 3): tiles += f'<path d="M{x+25} {y+22}l12-6 12 6v40h-24z" fill="#fff" opacity=".85"/>'
            elif i == 1: tiles += f'<path d="M{x+22} {y+20}h30l4 44h-38z" fill="#fff" opacity=".85"/>'
            else: tiles += f'<rect x="{x+22}" y="{y+34}" width="30" height="26" rx="5" fill="{a}"/><path d="M{x+29} {y+34}v-5a8 8 0 0 1 16 0v5" fill="none" stroke="{a}" stroke-width="3"/>'
            tiles += f'<circle cx="{x+60}" cy="{y+14}" r="7" fill="#fff"/>' + T(x + 60, y + 17, "♡", 8, 700, a, 1, "middle")
            tiles += T(x + 8, y + 88, ad, 7.5, 700) + T(x + 8, y + 101, fiyat, 8.5, 700, a, 1, fam="Inter Tight")
        body = T(14, 78, D["baslik"], 13, 700, fam="Inter Tight") + tiles + f'<rect x="14" y="326" width="152" height="26" rx="13" fill="{k}"/>' + T(90, 343, "Sepete git · " + D["ozet_deger"], 8.5, 700, "#fff", 1, "middle")
    return f'<svg viewBox="0 0 {w} {h}" aria-hidden="true">{defs}{top}{body}</svg>'

def telefon(kind, p, cls=""):
    return f'<div class="tel {cls}"><div class="tel-i">{ekran(kind, p)}</div></div>'

# ---------------- kart / giriş renk teması ----------------
import os
KART_TEMALARI = {
 "a": {k: ("#1A0C10", "#F4EDE0") for k in ["kumbara","rota","tempo","klinik","sepet","orbit"]},
 "b": {"kumbara": ("#DDEBE2", "#12382A"), "rota": ("#DCE5F3", "#12264F"), "tempo": ("#E6E3F8", "#23246B"),
       "klinik": ("#D8EFEE", "#0E4F56"), "sepet": ("#F6E3E7", "#2A1A1F"), "orbit": ("#ECE7DD", "#1E293B")},
 "c": {k: ("#EAE0CE", "#15090C") for k in ["kumbara","rota","tempo","klinik","sepet","orbit"]},
}
TEMA = os.environ.get("KART_TEMA", "b")
def kart_renk(p):
    t = KART_TEMALARI.get(TEMA, {}).get(p["slug"])
    return t if t else (p["renk"]["ana"], p["renk"]["acik"])

# ---------------- ana sayfa kart görseli ----------------
def kart_gorsel(p):
    c = p["renk"]; v = c["vurgu"]; a, l = kart_renk(p)
    lc = dict(ana=a, vurgu=(c["ana"] if TEMA in ("b", "c") and v in ("#E8A9B8", "#5FD3C6", "#3DDC97") else v), acik=l, koyu=c["koyu"])
    av = "".join(f'<g transform="translate({22+i*26} 144)">{avatar(t, s, b, 40)}</g>' for i, (t, s, b) in enumerate([
        (p["persona"]["ten"], p["persona"]["sac"], v), ("#8D5A3B", "#151010", l), ("#F3D2B6", "#B5651D", "#ffffff")]))
    return (f'<svg viewBox="0 0 300 220" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="300" height="220" fill="{a}"/>'
            f'<circle cx="250" cy="10" r="120" fill="{v}" opacity="{.14 if TEMA not in ("b","c") else .28}"/>'
            f'<g transform="translate(22 24)">{logo(p["logo"], lc, 52, bg=False)}</g>'
            f'<text x="24" y="104" font-family="Inter Tight,sans-serif" font-weight="700" font-size="24" fill="{l}">{e(p["ad"])}</text>'
            f'<text x="24" y="124" font-family="Manrope,sans-serif" font-size="10" fill="{l}" opacity=".75">{e(p["sektor"])} · {e(p["platform"].split(" · ")[0])}</text>'
            f'{av}'
            f'<g transform="translate(178 22) rotate(6)"><rect width="104" height="200" rx="18" fill="#0b0b0b"/><g transform="translate(6 6) scale(.511)">{ekran(p["ekran"][0], p).replace("<svg ", "<svg width=\"180\" height=\"360\" ",1)}</g></g>'
            f'</svg>')

# ---------------- CSS ----------------
PROJE_CSS = """:root{--bg:#F4EDE0;--surface:#FFFAF0;--ink:#15090C;--muted:#6B5A5C;--line:#DDD0BC;--wine:#7A1730;--wine2:#A62644;--dk:#0C0607;--cream:#F4EDE0;--cm:#B9A9A0}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:400 17px/1.65 Manrope,system-ui,sans-serif;overflow-x:hidden}
h1,h2,h3{font-family:"Inter Tight",system-ui,sans-serif;margin:0;letter-spacing:-.022em;line-height:1.08}
p{margin:0}a{color:inherit}
:focus-visible{outline:3px solid var(--wine2);outline-offset:3px}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px}
header{position:sticky;top:0;z-index:20;background:rgba(12,6,7,.92);backdrop-filter:blur(12px);color:var(--cream)}
.nav{display:flex;align-items:center;justify-content:space-between;height:68px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none}.mark{width:42px;height:42px;fill:none;stroke:currentColor;stroke-width:1.6;overflow:visible}.mark text{fill:currentColor;stroke:none}.acc{fill:var(--wine2);stroke:none}
.logo span{font:700 .9rem Manrope,sans-serif;letter-spacing:.34em}
.back{text-decoration:none;font-size:.92rem;opacity:.85}.back:hover{opacity:1}
.ph{background:var(--hb,var(--pa));color:var(--hf,var(--pl));position:relative;overflow:hidden;padding:72px 0 0}
.ph::before{content:"";position:absolute;width:720px;height:720px;right:-220px;top:-260px;border-radius:50%;background:var(--pv);opacity:.16}
.ph .wrap{position:relative;display:grid;grid-template-columns:1.05fr .95fr;gap:40px;align-items:end}
.ph-l{padding-bottom:72px}
.badge{display:inline-flex;align-items:center;gap:8px;font:700 .72rem Manrope,sans-serif;letter-spacing:.18em;text-transform:uppercase;border:1px solid currentColor;border-radius:99px;padding:6px 12px;opacity:.85}
.ph h1{font-size:clamp(2.8rem,6vw,4.6rem);font-weight:600;margin:22px 0 14px;display:flex;align-items:center;gap:18px}
.ph h1 svg{flex:none;border-radius:18px;box-shadow:0 0 0 1px rgba(255,255,255,.18)}
.ph .tag{font-size:clamp(1.2rem,2vw,1.5rem);opacity:.9;max-width:28ch}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:28px}.chips span{font-size:.85rem;border-radius:99px;padding:7px 14px;background:color-mix(in srgb,currentColor 10%,transparent)}
.phones{display:flex;justify-content:center;gap:18px;align-items:flex-end}
.tel{width:200px;flex:none;background:#0b0b0b;border-radius:30px;padding:9px;box-shadow:0 30px 70px -20px rgba(0,0,0,.6)}
.tel-i{border-radius:22px;overflow:hidden;line-height:0}.tel-i svg{width:100%;height:auto}
.phones .tel:nth-child(1){transform:translateY(40px) rotate(-4deg)}.phones .tel:nth-child(3){transform:translateY(60px) rotate(4deg)}
.phones .tel:nth-child(2){margin-bottom:-30px}
section{padding:88px 0}
.k{font:700 .75rem Manrope,sans-serif;letter-spacing:.22em;text-transform:uppercase;color:var(--wine2);margin-bottom:12px;display:block}
h2{font-size:clamp(1.8rem,3.4vw,2.6rem);font-weight:600}
.two{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:36px}
.box{background:var(--surface);border:1px solid var(--line);border-radius:22px;padding:34px}
.box h3{font-size:1.25rem;margin-bottom:10px}.box p{color:var(--muted)}
.persona{display:grid;grid-template-columns:auto 1fr;gap:26px;align-items:center;margin-top:36px;background:var(--dk);color:var(--cream);border-radius:22px;padding:34px}
.persona b{font:600 1.3rem "Inter Tight",sans-serif;display:block}.persona small{color:var(--cm)}
.persona q{display:block;margin-top:14px;font:italic 400 1.25rem/1.5 Fraunces,Georgia,serif;color:var(--cream)}
.feat{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:36px}
.feat div{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:24px}
.feat i{display:grid;place-items:center;width:38px;height:38px;border-radius:11px;background:var(--pa);color:var(--pl);font:700 .9rem "Inter Tight",sans-serif;font-style:normal;margin-bottom:14px}
.feat b{font:600 1.08rem "Inter Tight",sans-serif;display:block;margin-bottom:6px}.feat span{color:var(--muted);font-size:.93rem}
.journey{display:grid;grid-template-columns:repeat(5,1fr);margin-top:40px;padding:0;position:relative;list-style:none}
.journey::before{content:"";position:absolute;left:0;right:0;top:15px;height:2px;background:var(--line)}
.journey li{position:relative;padding-right:16px;font-size:.95rem}
.journey li::before{counter-increment:j;content:counter(j);display:grid;place-items:center;width:32px;height:32px;border-radius:50%;background:var(--pa);color:var(--pl);font:700 .85rem "Inter Tight",sans-serif;margin-bottom:14px;position:relative}
.journey{counter-reset:j}
.dark{background:var(--dk);color:var(--cream)}.dark .k{color:#E07A92}
.kpi{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:36px}
.kpi div{border:1px solid #33191f;border-radius:18px;padding:24px;background:#140a0d}
.kpi b{display:block;font:600 2rem "Inter Tight",sans-serif;color:var(--pv)}.kpi span{color:var(--cm);font-size:.9rem}
.note{color:var(--cm);font-size:.85rem;margin-top:16px}
.tech{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}.tech span{border:1px solid var(--line);border-radius:99px;padding:8px 16px;font-size:.92rem;background:var(--surface)}
.road{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:36px}
.road div{border-top:3px solid var(--pa);padding-top:16px}.road b{font:600 1.05rem "Inter Tight",sans-serif;display:block;margin-bottom:6px}.road span{color:var(--muted);font-size:.95rem}
.brand{display:grid;grid-template-columns:1fr 1.2fr;gap:22px;margin-top:36px;align-items:stretch}
.logos{display:flex;gap:18px;align-items:center;justify-content:center;background:var(--surface);border:1px solid var(--line);border-radius:22px;padding:30px}
.sw{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.sw div{border-radius:18px;padding:16px;min-height:150px;display:flex;flex-direction:column;justify-content:flex-end;font-size:.85rem;border:1px solid rgba(0,0,0,.06)}
.sw b{font:600 1rem "Inter Tight",sans-serif}
.cta{background:var(--wine);color:var(--cream);text-align:center}
.cta h2{max-width:20ch;margin:0 auto 16px}.cta p{color:#E7D3CF;max-width:52ch;margin:0 auto 28px}
.btn{display:inline-block;background:var(--cream);color:var(--dk);padding:14px 26px;border-radius:999px;font-weight:700;text-decoration:none;transition:transform .3s}.btn:hover{transform:translateY(-2px)}
.pn{display:grid;grid-template-columns:1fr 1fr;gap:18px;padding:40px 0}
.pn a{display:flex;align-items:center;gap:14px;text-decoration:none;background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:18px 20px;transition:border-color .3s}.pn a:hover{border-color:var(--wine2)}
.pn a:last-child{justify-content:flex-end;text-align:right}.pn small{display:block;color:var(--muted);font-size:.8rem}.pn b{font:600 1.1rem "Inter Tight",sans-serif}
footer{background:var(--dk);color:var(--cm);padding:26px 0;font-size:.85rem}footer .wrap{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}footer a{color:var(--cream);text-decoration:none}
@media (max-width:900px){.ph .wrap,.two,.brand{grid-template-columns:1fr}.ph-l{padding-bottom:20px}.feat,.kpi{grid-template-columns:1fr 1fr}.journey{grid-template-columns:1fr;gap:18px}.journey::before{display:none}.road{grid-template-columns:1fr}.phones{padding-bottom:30px}.tel{width:150px}.phones .tel:nth-child(3){display:none}}
@media (max-width:560px){.feat,.kpi,.sw{grid-template-columns:1fr 1fr}.persona{grid-template-columns:1fr}.pn{grid-template-columns:1fr}.tel{width:140px}.ph h1 svg{width:52px;height:52px}}
"""

MARK = '<svg class="mark" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="30"/><text x="32" y="37" text-anchor="middle" font-family="Fraunces,Georgia,serif" font-weight="600" font-size="19" letter-spacing="1">BMA</text><path class="acc" d="M32 43l3.2 3.5L32 50l-3.2-3.5z"/></svg>'
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;1,9..144,400&family=Inter+Tight:wght@500;600;700&family=Manrope:wght@400;500;700&display=swap" rel="stylesheet">'

def sayfa(i, p):
    c = p["renk"]; n = len(P); onc, son = P[(i - 1) % n], P[(i + 1) % n]
    feat = "".join(f'<div><i>{j+1:02d}</i><b>{e(t)}</b><span>{e(d)}</span></div>' for j, (t, d) in enumerate(p["ozellik"]))
    jour = "".join(f"<li>{e(s)}</li>" for s in p["yolculuk"])
    kpi = "".join(f'<div><b>{e(v)}</b><span>{e(t)}</span></div>' for t, v in p["kpi"])
    tech = "".join(f"<span>{e(t)}</span>" for t in p["teknoloji"])
    road = "".join(f'<div><b>{e(t)}</b><span>{e(d)}</span></div>' for t, d in p["yol"])
    sw_cols = [(c["ana"], c["acik"]), (c["vurgu"], c["koyu"]), (c["acik"], c["koyu"]), (c["koyu"], c["acik"])]
    sw = "".join(f'<div style="background:{bg};color:{fg}"><b>{e(ad)}</b>{bg.upper()}</div>' for (bg, fg), ad, in zip(sw_cols, p["renk_ad"]))
    pe = p["persona"]
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(p["ad"])} · Ürün konsepti | Bimayr</title>
<meta name="description" content="{e(p["ozet"])}">
<meta name="theme-color" content="{c["ana"]}">
<link rel="canonical" href="https://www.bimayr.com/projeler/{p["slug"]}.html">
<link rel="icon" type="image/svg+xml" href="../assets/favicon.svg">
{FONTS}
<link rel="stylesheet" href="proje.css">
</head>
<body style="--pa:{c["ana"]};--pv:{c["vurgu"]};--pl:{c["acik"]};--hb:{kart_renk(p)[0]};--hf:{kart_renk(p)[1]}">
<header><div class="wrap nav"><a class="logo" href="../" aria-label="Bimayr ana sayfa">{MARK}<span>BIMAYR</span></a><a class="back" href="../#calismalar">← Tüm çalışmalar</a></div></header>
<main>
<div class="ph"><div class="wrap">
<div class="ph-l"><span class="badge">Ürün konsepti · {e(p["sektor"])}</span>
<h1>{logo(p["logo"], c, 72)}{e(p["ad"])}</h1>
<p class="tag">{e(p["tag"])}</p>
<div class="chips"><span>{e(p["platform"])}</span><span>Tahmini süre: {e(p["sure"])}</span><span>Tasarım + geliştirme + veri</span></div></div>
<div class="phones">{telefon(p["ekran"][1], p)}{telefon(p["ekran"][0], p)}{telefon(p["ekran"][2], p)}</div>
</div></div>

<section><div class="wrap">
<span class="k">Genel bakış</span><h2>{e(p["ozet"])}</h2>
<div class="two"><div class="box"><h3>Problem</h3><p>{e(p["problem"])}</p></div><div class="box"><h3>Çözüm</h3><p>{e(p["cozum"])}</p></div></div>
<div class="persona">{avatar(pe["ten"], pe["sac"], c["vurgu"], 96)}<div><b>{e(pe["ad"])}</b><small>{e(pe["rol"])} · Hedef kullanıcı</small><q>{e(pe["soz"])}</q></div></div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<span class="k">Temel özellikler</span><h2>Ürünü ne yapar?</h2>
<div class="feat">{feat}</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<span class="k">Kullanıcı yolculuğu</span><h2>İlk günden alışkanlığa</h2>
<ol class="journey">{jour}</ol>
</div></section>

<section class="dark"><div class="wrap">
<span class="k">Ölçüm planı</span><h2>Başarıyı nasıl ölçeceğiz?</h2>
<div class="kpi">{kpi}</div>
<p class="note">Değerler, ürünün ilk 6 ayı için belirlenen hedeflerdir.</p>
</div></section>

<section><div class="wrap">
<span class="k">Yol haritası</span><h2>Adım adım teslim</h2>
<div class="road">{road}</div>
<div style="margin-top:44px"><span class="k">Teknoloji</span><div class="tech">{tech}</div></div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<span class="k">Marka</span><h2>Logo ve renk paleti</h2>
<div class="brand"><div class="logos">{logo(p["logo"], c, 96)}<div style="background:{c["acik"]};border-radius:22px;padding:4px">{logo(p["logo"], dict(ana=c["acik"], vurgu=c["vurgu"], acik=c["ana"], koyu=c["koyu"]), 88)}</div></div><div class="sw">{sw}</div></div>
</div></section>

<section class="cta"><div class="wrap">
<h2>Benzer bir ürün mü düşünüyorsunuz?</h2>
<p>Fikrinizi birlikte kapsamlayalım. Ekranları, teknolojiyi ve ölçüm planını size özel çıkaralım.</p>
<a class="btn" href="../#iletisim">Projenizi anlatın</a>
</div></section>

<div class="wrap pn"><a href="{onc["slug"]}.html"><span>←</span><span><small>Önceki</small><b>{e(onc["ad"])}</b></span></a><a href="{son["slug"]}.html"><span><small>Sonraki</small><b>{e(son["ad"])}</b></span><span>→</span></a></div>
</main>
<footer><div class="wrap"><span>© 2026 Bimayr · Apps &amp; Data Studio</span><a href="../kvkk.html">KVKK Aydınlatma Metni</a></div></footer>
</body>
</html>
"""

# ---------------- dosyaları yaz ----------------
(ROOT / "projeler").mkdir(exist_ok=True)
(ROOT / "projeler" / "proje.css").write_text(PROJE_CSS, encoding="utf-8")
for i, p in enumerate(P):
    (ROOT / "projeler" / f'{p["slug"]}.html').write_text(sayfa(i, p), encoding="utf-8")

# ana sayfa kartları
cards = []
for i, p in enumerate(P):
    d = ["", " d1", " d2"][i % 3]
    t, v = p["kpi"][0]
    cards.append(f'<a class="work rv{d}" href="projeler/{p["slug"]}.html"><div class="art">{kart_gorsel(p)}</div>'
                 f'<div class="wb"><small>{e(p["sektor"])} · {e(p["platform"])}</small><h3>{e(p["ad"])}</h3><p>{e(p["ozet"])}</p>'
                 f'<div class="met">{e(v)}<span>hedef · {e(t.lower())}</span></div><span class="more">Projeyi incele <b>→</b></span></div></a>')
idx = ROOT / "index.html"; s = idx.read_text(encoding="utf-8")
a = s.index('<div class="wk">'); b = s.index('</div></div></section>', a)
s = s[:a] + '<div class="wk">\n' + "\n".join(cards) + '\n</div>' + s[b + len('</div>'):]
s = s.replace('<h2 class="rv">Seçilmiş çalışmalar</h2>', '<h2 class="rv">Seçilmiş çalışmalar</h2>', 1)
old_lead = '<p class="lead rv d1" style="margin-top:16px">Farklı sektörlerde hem ürünü kurduğumuz hem de veriyle büyüttüğümüz projelerden örnekler.</p>'
new_lead = '<p class="lead rv d1" style="margin-top:16px">Stüdyomuzun farklı sektörler için tasarladığı ürün konseptleri. Her biri problemi, ekranları, ölçüm planı ve yol haritasıyla hazır. İncelemek için bir projeye tıklayın.</p>'
if old_lead in s: s = s.replace(old_lead, new_lead)
idx.write_text(s, encoding="utf-8")

css = ROOT / "css" / "style.css"; c = css.read_text(encoding="utf-8")
if "/* proje kartlari */" not in c:
    c += """/* proje kartlari */
a.work{display:block;text-decoration:none;color:inherit}
.art svg{display:block}
.wb small{display:block}
.met span{display:block;margin:2px 0 0}
.more{display:inline-flex;gap:6px;margin-top:16px;font-weight:700;font-size:.9rem;color:var(--wine2)}.more b{transition:transform .3s}a.work:hover .more b{transform:translateX(4px)}
"""
    css.write_text(c, encoding="utf-8")
print("tamam:", ", ".join(p["slug"] for p in P))

=== 1. Hoş geldin
# EloGlobal'e hoş geldin

EloGlobal, Discord ve diğer tüm sesli sohbetler için gerçek zamanlı bir çevirmendir. Her şey kendi bilgisayarında
çalışır: konuşma tanıma, çeviri ve sesler. Kimsenin söylediği ya da yazdığı hiçbir şey internete gönderilmez.

- **Diğerlerini kendi dilinde duyarsın.** Uygulama insanların Discord'da söylediklerini dinler, yazıya döker,
  çevirir, altyazı gösterir ve çeviriyi sana doğal bir sesle okuyabilir.
- **Onlar seni kendi dillerinde duyar.** Mikrofona konuşursun. Uygulama söylediğini çevirir ve sanal bir ses
  kablosu üzerinden Discord'a seslendirir.
- **Metin de.** Sunuculardaki, özel mesajlardaki ve başlıklardaki Discord mesajlarını, fareyle seçtiğin her metni ve
  ekrandaki metni OCR ile çevirir. Onların dilinde de yazabilirsin.
- **Ücretsiz ve gizli.** Hesap yok, abonelik yok, çevrim içi hizmet yok. Modeller bir kez indirilir, sonra internetsiz
  çalışır.

Bu kılavuzun on iki bölümü var. Sonraki ve Önceki düğmelerini kullan ya da listeden bir bölüme tıkla. Bölüm her
değiştiğinde anlatıcı eskisini bırakır ve yenisini okur. Anlatıcı, bilgisayarında çalışan bir sestir.

=== 2. İlk başlatma
# İlk başlatma

**Adım 1. Uygulamayı aç.** EloGlobal'i Başlat menüsünden ya da Steam'den başlat. İlk seferde uygulamanın dilini
seçersin. Her şey bu dilde gösterilir; rehber ve bu kılavuz da bu dilde sesli okunur. Sonra uygulama başkalarının
sesleri ve mesajlarıyla ne yaptığını açıklar: her şey bilgisayarında kalır. Ardından kısa bir rehberli tur ilk
adımları gösterir. Yalnızca bu ilk seferde açılır; bu sekmeden tekrar izleyebilirsin.

**Adım 2. Sanal ses kablosu kur.** VB-Audio Virtual Cable'ı kendi sitesinden kur ve bilgisayarı yeniden başlat. Onu
EloGlobal değil VB-Audio yapar ve kişisel kullanım için ücretsizdir. Windows sanal bir mikrofon oluşturmak için ona
ihtiyaç duyar.

**Adım 3. Discord'u ayarla.** Discord'u aç, sonra Kullanıcı Ayarları'na, sonra Ses ve Görüntü'ye git.

- Giriş Aygıtı: VB-Audio Virtual Cable'dan CABLE Output.
- Çıkış Aygıtı: kulaklığın.
- Gürültü Azaltma, Yankı Engelleme ve Otomatik Kazanç Kontrolü'nü kapat.

**Adım 4. Uygulamayı ayarla.** Standart, her şey bu bilgisayarda profilini koru. Çıkış sekmesinde çevrilmiş sesini
CABLE Input'a gönder. Giriş sekmesinde Yalnızca Discord uygulaması yöntemini koru ve gerçek mikrofonunu seç. Canlı
sekmesinde dilleri seç. Sonra Başlat'a ya da F5 tuşuna bas.

**Başlat'a ilk bastığında** uygulama gerekenleri yalnızca bir kez indirir: bilgisayarına göre 75 ile 1600 megabayt
arası konuşma tanıma modeli, her dil çifti için yaklaşık 280 megabaytlık bir çeviri modeli ve dillerinin sesleri.
Bundan sonra internetsiz çalışır.

**Görüşmendeki kişilere** çevirmen kullandığını söyle, örneğin: Bir çeviri uygulaması kullanıyorum, yalnızca
bilgisayarımda çalışıyor ve hiçbir şey kaydetmiyor.

=== 3. Ana pencere
# Ana pencere

En üstte profil kutusu var. Bir profil motor, dil ve aygıt ayarlarının hepsini saklar. Profilleri kaydedebilir,
farklı kaydedebilir, silebilir, içe ve dışa aktarabilirsin. Başlangıç profilleri: Standart, her şey bu bilgisayarda.
En hızlı, yavaş bilgisayarlar için. En iyi kalite, NVIDIA ekran kartlı bir bilgisayar için. Ve Ollama ile yapay zekâ
çevirisi.

Değişikliklerin yaklaşık bir saniye sonra otomatik kaydedilir. Bunu Ayarlar sekmesinden kapatabilirsin.

Profil kutusunun yanında üç düğme var:

- **Altyazılar** sürükleyebileceğin, fare tekerleğiyle boyutlandırabileceğin ve sağ tıkla ayarlayabileceğin yüzen
  bir altyazı penceresi gösterir.
- **Sohbet** Discord metin mesajlarının çevirisini açar.
- **Başlat** ses çevirmenini başlatır. F5 tuşu da aynısını yapar.

Sekmeler: Pano, Canlı, Metin, Giriş, Çıkış, Konuşma, Çeviri, Yapay zekâ modeli, Ses, Kurulum, Ayarlar, Kılavuz ve
Günlük. Sonraki bölümler en çok kullanacaklarını anlatır.

=== 4. Pano
# Pano

Pano senin kontrol merkezindir. İlk sekmedir ve her şeyi tek bakışta gösterir.

- **Ses çevirmeni kartı** canlı ses çevirisini başlatır ve durdurur, ne yaptığını gösterir: tanıma, çeviri ya da
  konuşma.
- **Sohbet çevirisi kartı** Discord mesajlarının çevirisini başlatır ve durdurur. Çevrilen mesajları sırayla ya da
  yeni bir mesajın okunanı bölmesine izin vererek sesli okuma seçeneği de vardır.
- **Sen kartı**, Discord adını ve yazdığın dili girdiğin yerdir.
- **Araçlar kartı**, seçerek çeviri, OCR ve altyazı penceresi için kısayollar içerir.
- **Kısayollar kartı** klavye kısayollarını hatırlatır.
- Altta Son çeviriler, son çevrilen satırları gösterir.

İki yerde görünen ayarlar, örneğin Pano'da ve Metin sekmesinde olanlar, her zaman eşit kalır.

=== 5. Canlı ses çevirisi
# Canlı ses çevirisi

Bu ana özelliktir. İki yönde çalışır ve her yön ayrı açılabilir.

**Gelen: onlar konuşur, sen duyarsın.** Uygulama sadece Discord uygulamasını dinler; bu yüzden kendi sesini,
oyununu ya da müziğini asla duymaz ve konuşurken dinlemeye devam eder. Konuşmayı tanır, çevirir, altyazı gösterir
ve istersen çeviriyi söyler. Onların konuştuğu dili ya da Otomatik algıla'yı seçersin. Dili seçmek,
bilgisayarındaki tanımayı yaklaşık iki kat hızlandırır.

**Giden: sen konuşursun, onlar duyar.** Uygulama mikrofonunu dinler, söylediğini çevirir ve sanal kablo üzerinden
Discord'da söyler. Kendi sesin Discord'a gönderilmez, yalnızca çeviri gider. Discord kablo yerine gerçek
mikrofonunu kullanırsa uygulama seni uyarır.

**İnsanları duy, F9 tuşu.** Varsayılan olarak sadece çevirileri duyarsın. Çevirmen çalışırken uygulama Discord'u
Windows ses karıştırıcısında kısar ve Durdur'a bastığında sesini geri verir. Onların kendi seslerini de duymak için
F9'a ya da İnsanları duy düğmesine bas. Tuşu Giriş sekmesinden değiştirebilirsin.

**Bir şey mi kaçırdın? Ctrl+Alt+R** son çeviriyi kulaklığında yeniden söyler. **Ctrl+Alt+L** onların konuştuğu dili
uygulamanın az önce duyduğu dile sabitler: tanıma hızlanır ve cevapların o dile gider. Başka bir gruba katıldığında
Otomatik algıla'ya dönmek için tekrar bas. İki tuşu da Giriş sekmesinden değiştirebilirsin; Canlı sekmesinde onlar
için düğmeler de var.

**Tek ses, sırayla.** Görüşme çevirileri ve sesli okunan sohbet mesajları tek bir sesi paylaşır, bu yüzden asla
birbirinin üstüne konuşmaz. Her şey söylendiği sırayla söylenir ve hiçbir şey atlanmaz: şu anki cümle çalarken
sonraki hazırlanır, cümleler birikince ses biraz daha hızlı konuşur.

**Kim konuşuyor.** Uygulamanın sesi kimin konuştuğunu söyleyebilir, örneğin adın ilk iki harfini ya da tam adı.
Bunu Çıkış sekmesinde, Uygulamanın sesi altında seç. Görüşmelerde adlar doğrudan Discord uygulamasından gelir:
Çıkış sekmesinde, Kim konuşuyor altında kendi Discord uygulamanı bir kez ekle. Sohbet mesajlarında her zaman
yazarın adı vardır.

**Canlı** sekmesinde iki yönün dillerini ayarlar, seviye göstergelerini izler ve dökümü okursun. Bir bas-konuş
düğmesi ve Söylemek için yaz kutusu kullanabilirsin: bir satır yazarsın, çevrilir ve Discord'da söylenir. Onların
konuştuğu dilde cevap ver seçeneği, çıkış dilinin karşı tarafta en son algılanan dili izlemesini sağlar.

**Giriş** sekmesinde neyin dinleneceğini ve mikrofonunun nasıl başlayacağını seçersin: ses etkinliği, bas-konuş ya
da aç-kapa. Bir hassasiyet ayarı da vardır. Uygulama, mikrofonun kendi sesini duyduğunda onu tanır ve yok sayar.

**Çıkış** sekmesinde çevirilerin nerede çalacağını, sesin için sanal kabloyu, uygulamanın sesini ve kimin
konuştuğunu seçersin.

Tüm ses aygıtları ayrıca tek bir yerde, Ayarlar sekmesindeki Ses aygıtları bölümünde toplanmıştır.

=== 6. Motorlar: konuşma, çeviri, yapay zekâ ve ses
# Motorlar

Çevirinin her adımı bilgisayarında çalışır ve ayarları istediğin zaman değiştirebilirsin. Profiline kaydedilirler.

- **Konuşma sekmesi.** Konuşmayı Whisper ile metne çevirir. auto model boyutu bilgisayarına göre seçilir: işlemcide
  küçük bir model, NVIDIA ekran kartında büyük ve isabetli bir model. Büyük model daha doğrudur ama daha yavaştır. Bu
  sekmede bir mikrofon testi var.
- **Çeviri sekmesi.** Helsinki Üniversitesi'nin OPUS-MT motoru cümle başına yaklaşık saniyenin onda birinde çevirir.
  Her dil çifti bir kez indirilir; doğrudan modeli olmayan diller İngilizce üzerinden çevrilir. Dillerimin
  modellerini şimdi indir düğmesi onları görüşmeden önce getirir. Tonu seçebilirsin; bir sözlük de adların ve oyun
  terimlerinin nasıl çevrileceğini belirler.
- **Yapay zekâ modeli sekmesi.** İsteğe bağlı. Bilgisayarına Ollama ya da LM Studio ve bir model kurarsan, Bu
  bilgisayardaki yapay zekâ modeli motoru onunla çevirir. Argoyu ve bağlamı daha iyi anlar ama hızlı bir bilgisayar
  ya da ekran kartı ister. Uygulama yalnızca kendi bilgisayarındaki veya yerel ağındaki yapay zekâ sunucularıyla
  konuşur.
- **Ses sekmesi.** Bu bilgisayarın sesleri: doğal Piper ve Kokoro sesleri ve Windows'un kendi sesleri. Auto her dil
  için bir ses seçer. Bir ses ilk kullanıldığında bir kez indirilir. Kokoro sesleri çok doğal ama hızlı bir
  bilgisayar ister. Daha fazla Windows sesi için Windows Ayarları, Saat ve dil, Konuşma, Ses ekle'yi aç. Her yön için
  hızı, perdeyi ve ses düzeyini ayarlayabilirsin.

Her sekmede bir Test düğmesi var; bir motoru kullanmadan önce deneyebilirsin.

=== 7. Gizlilik ve verilerin
# Gizlilik ve verilerin

EloGlobal yalnızca bilgisayarında çalışır. Görüşmede insanların söyledikleri, mikrofonun, sohbet mesajları ve
çevirdiğin metin bilgisayarından asla çıkmaz. Uygulamanın hesabı, kullanım istatistiği ve reklamı yoktur.

**Başkalarının sesleri.** Çevirmen çalışırken uygulama, senin için çevirmek üzere görüşmendeki kişilerin
söylediklerini duyar. Onlara çevirmen kullandığını söyle. Bazı ülkelerde onların onayı gerekir.

**Ne kaydedilir.** Ayarların ve profillerin, ayrıca insanların söylediklerini değil teknik mesajları içeren günlük
dosyaları. Görüşme dökümleri yalnızca sen açarsan kaydedilir: Ayarlar sekmesi, Gizlilik ve hakkında bölümü.

**Nerede.** Uygulamanın kaydettiği her şey kullanıcı klasöründe, App Data, Local, EloGlobal altındadır: profiller,
günlükler, dökümler ve indirilen modeller. Ayarlar sekmesinde veri klasörünü ve model klasörünü açan düğmeler var.

**İnternet.** Uygulama yalnızca model dosyalarını bir kez indirir. İsteğe bağlı Kim konuşuyor özelliği Discord'a
kendi Discord uygulamanla giriş yapar. Güncellemeler mağazadan gelir.

Ayarlar sekmesi gizlilik bildirimini de yeniden gösterir; Hakkında ve lisanslar penceresi EloGlobal'in dayandığı
tüm yazılımları ve modelleri listeler.

=== 8. Discord metnini çevirmek
# Discord metnini çevirmek

**Sohbet** düğmesine bas ya da Pano'daki sohbet kartını kullan. Uygulama, Discord uygulamasında gördüğün mesajları
bir ekran okuyucu gibi Windows erişilebilirlik özellikleriyle okur. Token ya da bot gerektirmez ve Discord'a hiçbir
şey göndermez.

Yeni mesajlar çevrilir ve doğrudan Discord'un içinde, özgün metnin üstünde ya da yanındaki küçük bir pencerede
gösterilir. Bunu Metin sekmesinde Çevirileri göster altında seçersin. Sunucularda, özel mesajlarda, gruplarda, alt
başlıklarda ve forum gönderilerinde, Discord arka plandayken bile çalışır. Zaten senin dilinde olan mesajlar ve
kendi mesajların atlanır. Çeviriler yalnızca Discord etkin pencereyken görünür, bu yüzden oyununu asla kapatmaz.

**Sesli okuma.** Sadece yeni mesajlar sesli okunur. Geri kaydırdığın mesajlar, düzenlenen ve eski mesajlar ekranda
çevrilir ama asla okunmaz. Sohbet mesajları uygulamanın sesini görüşme çevirileriyle paylaşır, bu yüzden ikisi asla
aynı anda konuşmaz.

Metin sekmesinde başka araçlar da var:

- **Seçerek çevir.** Bir metni seç ya da bir kelimeye çift tıkla; farenin yanında çevirinin olduğu bir pencere
  çıkar.
- **Ctrl+Alt+T** her uygulamada geçerli seçimi çevirir.
- **Ctrl+Alt+Y**, Discord'un mesaj kutusuna yazdığını o sohbette kullanılan dile çevrilmiş haliyle değiştirir.
- **Onların dilinde yaz.** Metin sekmesinde yaz, sonra kopyala, Discord'a yapıştır ya da gönder.
- **Ctrl+Alt+O** ekranın herhangi bir yerine bir çerçeve çizmeni sağlar. Uygulama metni OCR ile okur ve çeviriyi
  üstünde gösterir. Birkaç saniyede bir tekrar edebilir.
- **Kopyalanan metin.** İstersen kopyaladığın her şeyi çevirir.

Tüm kısayolları Metin sekmesinden değiştirebilirsin. Rusça ya da Japonca gibi başka alfabelerde OCR için o dili
Windows Ayarları'ndan ekle.

=== 9. Altyazılar ve dökümler
# Altyazılar ve dökümler

**Altyazı penceresi** oyunun ya da Discord'un üstünde durur. Taşımak için sürükle. Boyutlandırmak için fare
tekerleğini kullan. Kaç satır gösterileceği, orijinal metnin gösterilip gösterilmeyeceği ve arka plan gibi
seçenekler için sağ tıkla. Ayarlar'da metnin boyutunu ve yazı tipini değiştirirsin.

Bir konuşma **döküm** olarak kaydedilebilir. Dökümler başkalarının sözlerini içerdiği için bu varsayılan olarak
kapalıdır. Çıkış sekmesinden ya da Ayarlar'dan aç. Dökümler veri klasöründe, transcripts altında saklanır.

Günlük sekmesi uygulamanın ne yaptığını gerçek zamanlı gösterir. Günlükleri, dökümleri ve veri klasörünü açan
düğmeleri de vardır. Bir şey ters giderse önce günlüğe bak.

Alttaki durum çubuğu her aşamanın gecikmesini gösterir: konuşma tanıma, çeviri ve ses; böylece hangi adımın yavaş
olduğunu görürsün.

=== 10. Ayarlar ve hakkında
# Ayarlar ve hakkında

**Ayarlar** sekmesi uygulamanın dilini belirler. Değiştirdikten sonra uygulama yeni dilde yeniden başlar. Tüm ses
aygıtlarını da tek yerde toplar: uygulamanın neyi dinlediği, mikrofonun, çevirilerin nerede çaldığı ve çevrilmiş
sesinin nereye gittiği.

Uygulamanın görünüşünü yönetir: tema, koyu ya da açık, yazı tipi ve uygulamanın, Discord içinde, küçük sohbet
penceresinde ve açılır pencerelerde gösterilen çevirilerin metin boyutu. Ayrıca tüm kısayollar, pencereyi diğerlerinin
üstünde tutan bir anahtar ve pencereleri yerine koyan, veri, model ve günlük klasörlerini açan düğmeler burada.

Değişiklikleri otomatik kaydet anahtarı profilini her değişiklikten yaklaşık bir saniye sonra kaydeder. Varsayılan
olarak açıktır.

**Gizlilik ve hakkında.** Döküm anahtarı, gizlilik bildirimi ve EloGlobal'in lisansıyla kullandığı tüm bileşenlerin
listesini içeren Hakkında ve lisanslar penceresi.

**Güncellemeler** EloGlobal'i kurduğun mağazadan gelir: Microsoft Store ya da Steam. Ayarların, profillerin ve
indirilen modellerin korunur.

=== 11. Sorun giderme
# Sorun giderme

**Kimse çevirimi duymuyor.** Discord'da giriş aygıtı CABLE Output olmalı. Uygulamada Çıkış sekmesi CABLE Input'a
göndermeli. Discord'da Gürültü Azaltma'nın kapalı olduğunu kontrol et.

**Uygulama hiçbir şey duymuyor.** Giriş sekmesinde yöntemi kontrol et. Yalnızca Discord uygulaması seçiliyse Discord
açık olmalı. Loopback ile aygıt, Discord'un çaldığı aygıt olmalı. Canlı sekmesindeki seviye göstergelerine bak.
Kıpırdamıyorlarsa ayar yanlıştır.

**Çevirim iki kez duyuluyor ya da uygulama kendini çeviriyor.** Giriş sekmesinde Yalnızca Discord uygulaması
yöntemini kullan ve kulaklık tak.

**Discord sessiz.** Çevirmen çalışırken bu bilerek yapılır: insanları da duymak için F9'a bas. EloGlobal aniden
kapandıysa bir kez aç, Discord'un sesini geri verir; ya da Windows ses karıştırıcısında Discord'u aç.

**İnsanlar gerçek sesimi duyuyor.** Discord'da giriş aygıtı mikrofonun değil, CABLE Output olmalı. Discord gerçek
mikrofonunu kullandığında uygulama uyarı gösterir.

**Yavaş.** Canlı sekmesinde Otomatik algıla yerine onların konuştuğu dili seç. Konuşma sekmesinde daha küçük bir
model seç ya da NVIDIA ekran kartı kullan. Kokoro sesleri birçok işlemcide yavaştır: Ses sekmesinde bir Piper ya da
Windows sesi seç.

**Dilim için ses yok.** Bir Windows sesi ekle: Windows Ayarları, Saat ve dil, Konuşma, Ses ekle. Sonra Ses
sekmesinde Ses listesini yeniden yükle'ye bas.

**Bir indirme başarısız.** İnternet bağlantını kontrol et ve yeniden Başlat'a bas; indirme kaldığı yerden devam eder.

**Hâlâ takıldın mı?** Günlük sekmesini ve günlük klasörünü aç. Bir sorunu mağaza sayfası üzerinden bildirirken
günlük yardımcı olur.

=== 12. Bu kılavuz hakkında
# Bu kılavuz hakkında

EloGlobal'in içindeki kılavuzu okuyorsun. Anlatıcı, uygulamanın dilinde, bilgisayarında çalışan bir sestir.
Çevrim dışı çalışır ve hiçbir yere bir şey göndermez.

- **Sonraki ve Önceki** bölümler arasında geçer. Anlatıcı eski bölümü okumayı bırakır ve yenisine başlar; yeni metin
  aynı anda görünür.
- **Sesli oku** anlatıcıyı açar ya da kapatır. Kapalıyken kılavuz yalnızca metindir.
- **Yeniden oku** geçerli bölümü baştan başlatır.
- **Durdur** anlatıcıyı susturur.
- **Ses** ve **Hız** nasıl duyulduğunu değiştirir. Bu bilgisayarda dilinin herhangi bir sesini ya da indirilecek bir
  sesi seçebilirsin.
- **Rehberli turu tekrar izle** ilk adımları yeniden gösterir.

Bu sekmeden çıktığında anlatıcı susar ve sen çevirmeni kullanırken asla kendiliğinden başlamaz.

Kılavuzun sonu bu. EloGlobal'in tadını çıkar!

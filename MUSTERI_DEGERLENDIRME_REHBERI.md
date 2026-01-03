# Çözüm Koleji Veli Asistanı - Müşteri Değerlendirme Rehberi

Bu rehber, Çözüm Koleji Veli Asistanı demosunu canlı ortamda değerlendirirken izlemeniz gereken adımları ve dikkat etmeniz gereken noktaları içermektedir.

## 1. Demoyu Başlatma

Size iletilen uygulama bağlantısına (link) tıklayarak asistanı tarayıcınızda açabilirsiniz.

> **Not:** Uygulama bir süre işlem yapılmadığında uyku moduna geçebilir. Linke tıkladığınızda açılması 1-2 dakika sürebilir ("Waking up..." uyarısı görebilirsiniz). Lütfen açılmasını bekleyiniz.

## 2. Değerlendirme Öncesi Önemli Not ⚠️

**Bu asistan şu an için sadece sisteme yüklenmiş olan resmi okul dokümanları (Veli Bilgilendirme Metinleri, Ders Programları vb.) üzerinden cevap vermektedir.**

Bu nedenle, ilk testlerinizi yaparken **dokümanlarda yer alması muhtemel** (ders saatleri, etkinlikler, kulüpler vb.) konuları sormanızı rica ederiz. Asistanın genel dünya bilgisi veya sisteme yüklenmemiş konular hakkındaki sorulara cevap vermemesi (veya "bilgi yok" demesi) beklenen bir davranıştır.

## 3. Değerlendirme Senaryoları 

Asistanın yeteneklerini test etmek için aşağıdaki senaryoları deneyebilirsiniz:

### Senaryo 1: Temel İletişim ve Karşılama
**Amaç:** Asistanın doğal dil işleme yeteneğini ve nezaketini test etmek.
- **Soru:** "Merhaba" veya "Selam"
- **Beklenen:** Asistanın sizi selamlaması ve nasıl yardımcı olabileceğini sorması.

### Senaryo 2: Okul Bilgisi Sorgulama (RAG)
**Amaç:** Asistanın dokümanlardan doğru bilgiyi bulup getirip getirmediğini test etmek.
- **Hazırlık:** Sol menüden ilgili kademeyi (örn. Lise) seçin.
- **Soru:** "Lise ders saatleri nedir?" veya "İngilizce eğitimi hakkında bilgi verir misin?"
- **Beklenen:** Asistanın okulun resmi dokümanlarından ilgili bilgiyi bulup size sunması.

### Senaryo 3: Bağlamsal Takip (Context Awareness)
**Amaç:** Asistanın sohbet geçmişini hatırlayıp hatırlamadığını test etmek.
- **Soru 1:** "Lisede spor faaliyetleri neler?"
- **Soru 2:** "Peki yüzme var mı?" (Okul adını veya "spor" kelimesini tekrar etmeden)
- **Beklenen:** Asistanın "yüzme" sorusunun önceki spor faaliyetleri konusuyla ilgili olduğunu anlaması ve buna göre yanıt vermesi.

### Senaryo 4: Kademe Değişikliği
**Amaç:** Farklı okul kademeleri arasında geçişin doğruluğunu test etmek.
- **İşlem:** Sol menüden "Lise"yi kaldırıp "Anaokulu"nu seçin.
- **Soru:** "Eğitim saatleri nasıl?"
- **Beklenen:** Asistanın artık Lise değil, Anaokulu saatlerini vermesi.

## 4. Bilinen Sınırlamalar (Demo Sürümü)

Bu bir demo sürümü olduğu için bazı özellikler henüz tamamlanmamış olabilir:
- **Yanıt Hızı**: İlk yanıtlarda modelin yüklenmesi ("Cold Start") nedeniyle kısa bir gecikme olabilir.
- **Hafıza**: Sayfayı yenilediğinizde (F5) sohbet geçmişi sıfırlanır.
- **Hata Durumları**: Beklenmedik sorularda bazen genel yanıtlar verebilir.

## 5. Geri Bildirim

Değerlendirmeniz sırasında karşılaştığınız hataları veya önerilerinizi lütfen not ediniz. Özellikle:
- Yanıtın doğruluğu
- Yanıtın hızı
- Kullanım kolaylığı

**Ek olarak:** Asistanın cevaplamasını istediğiniz ancak şu an cevaplayamadığı (dokümanlarda olmayan) konular varsa, bunları da lütfen bize iletiniz. Bu konuları sisteme ekleyerek asistanı geliştirebiliriz.

## 6. Web sitesi etkinliklerine erişim

Asistan, "hangi etkinlikler yapıldı" gibi soruları yanıtlarken Çözüm Koleji web sitesindeki haberleri tarama yeteneğine sahiptir. Bu özellik şu an **BETA (Geliştirme)** aşamasındadır. Web sitesindeki haber formatlarının çeşitliliği nedeniyle bazen eksik veri çekebilir. Canlı sürüme geçişle birlikte bu modülün kararlılığı artırılacaktır. Şu anki demoda bu özelliği test ederken, asistanın bazen genel cevaplar verebileceğini göz önünde bulundurunuz.
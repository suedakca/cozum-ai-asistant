# Çözüm Koleji Veli Asistanı 


---

## 📖 İçindekiler

1. [Proje Özeti](#1-proje-özeti)
2. [Asistanın Yapabilecekleri](#2-asistanın-yapabilecekleri)
3. [Etkinlik ve Haber Bilgisi Senaryoları](#3-etkinlik-ve-haber-bilgisi-senaryoları)
4. [Kullanıcı Bilgileri ve Sohbet Geçmişi](#4-kullanıcı-bilgileri-ve-sohbet-geçmişi)
5. [Web Sitesi Entegrasyonu](#5-web-sitesi-entegrasyonu)
6. [Zaman Planı](#6-zaman-planı)
7. [Maliyet Tablosu](#7-maliyet-tablosu)

---

## 1. Proje Özeti

Çözüm Koleji Veli Asistanı, velilerin okul hakkındaki sorularını 7/24 yanıtlayan bir yapay zeka sohbet asistanıdır. Asistan, okulun resmi dokümanlarını ve güncel etkinlik bilgilerini kullanarak velilere doğru ve tutarlı bilgi sunar.

### Kullanım Alanları

- Web sitesinde sohbet balonu (widget) olarak
- Ayrı bir sayfa olarak (örn: cozumkoleji.com/asistan)
- İlerleyen dönemde WhatsApp veya mobil uygulama entegrasyonu

---

## 2. Asistanın Yapabilecekleri

### Temel Özellikler

| Özellik | Açıklama |
|---------|----------|
| **Okul Bilgisi Yanıtlama** | Ders saatleri, eğitim programları, spor faaliyetleri gibi sorulara okulun resmi dokümanlarından cevap verir. |
| **Kademe Bazlı Bilgi** | Anaokulu, ilkokul, ortaokul ve lise için ayrı ayrı doğru bilgi sunar. |
| **Takip Soruları** | "Peki ücretleri?" gibi devam sorularını bağlamında değerlendirir. |
| **Randevu Yönlendirme** | Gerekli durumlarda veli ile görüşme randevusu oluşturur. |

### Ücret Soruları Hakkında

Asistan, ücret sorularına doğrudan yanıt vermek yerine, velileri kayıt danışmanlarıyla görüşmeye yönlendirir:

```text
Veli: "Lise ücretleri ne kadar?"

Asistan: "Ücretler ve kayıt koşulları hakkında size en doğru bilgiyi 
         verebilmemiz için bir görüşme randevusu oluşturmamı ister misiniz?"
```

---

## 3. Etkinlik ve Haber Bilgisi Senaryoları

Veliler "hangi etkinlikler yapıldı?", "yaklaşan etkinlikler neler?" gibi sorular sorabilir. Bu bilgilere erişim için üç farklı yöntem mevcuttur:

---

### Senaryo A: Admin Panel ile Manuel Giriş

Okul personeliniz, sizin için hazırlayacağımız bir panel üzerinden etkinlik bilgilerini girer.

```text
[Personel] → [Admin Panel] → [Etkinlik Ekle] → [Asistan Bilgiyi Kullanır]
```

| Avantajlar | Dikkat Edilecekler |
|------------|--------------------|
| Bilgi her zaman doğru ve kontrollü | Personelin düzenli veri girmesi gerekir |
| Teknik bağımlılık yok | Haftalık 15-30 dakika zaman ayırma |

**Bakım Gereksinimi:** Az

---

### Senaryo B: Web Sitesinden Otomatik Çekme

Sistem, web sitenizdeki duyurular sayfasını düzenli aralıklarla tarar ve yeni içerikleri otomatik olarak işler.

```text
[Web Sitesi Duyurular] → [Otomatik Tarama] → [Asistan Bilgiyi Kullanır]
```

| Avantajlar | Dikkat Edilecekler |
|------------|--------------------|
| Manuel iş gerektirmez | Web sitesi yapısı değişirse güncelleme gerekir |
| Personel zamanı harcanmaz | Haber formatlarının tutarlı olması önemli |

**Bakım Gereksinimi:** Orta

---

### Senaryo C: Instagram Entegrasyonu

Asistan, okulun resmi Instagram hesabındaki paylaşım açıklamalarını (caption) okur ve bu bilgileri kullanır. Semantik arama teknolojisi sayesinde veli tam kelimeyi kullanmasa bile ilgili içeriği bulabilir.

```text
[Instagram Paylaşımı] → [Açıklama Metni Okunur] → [Asistan Bilgiyi Kullanır]
```

**Örnek:**
- **Paylaşım:** "8. sınıflarımızla LGS motivasyon pikniği yaptık."
- **Soru:** "Sınav stresiyle ilgili bir etkinlik var mı?"
- **Yanıt:** "Instagram paylaşımımıza göre 8. sınıflar için LGS motivasyon pikniği gerçekleştirildi."

| Avantajlar | Dikkat Edilecekler |
|------------|--------------------|
| Ek veri girişi gerektirmez | Instagram açıklamalarının açıklayıcı yazılması gerekir |
| Sosyal medya trafiğini artırır | Instagram API yapısındaki değişiklikler takip edilmelidir |

**Bakım Gereksinimi:** Çok

---

### Senaryo Karşılaştırması

| Özellik | Senaryo A (Panel) | Senaryo B (Web) | Senaryo C (Instagram) |
|---------|-------------------|-----------------|----------------------|
| Manuel İş | Var | Yok | Yok |
| Teknik Karmaşıklık | Düşük | Orta | Yüksek |
| Bakım Gereksinimi | Az | Orta | Çok |
| Kurulum Süresi | 2 gün | 3 gün | 4 gün |

---

## 4. Kullanıcı Bilgileri ve Sohbet Geçmişi

### Toplanabilecek Bilgiler

| Bilgi | Zorunlu mu? | Kullanım Amacı |
|-------|-------------|----------------|
| Telefon Numarası | Randevu için evet | Kayıt danışmanı iletişimi |
| Ad Soyad | Hayır | Kişiselleştirilmiş hitap |

Tüm veri toplama süreçlerinde KVKK aydınlatma metni ve açık rıza onayı alınacaktır.

---

### Sohbet Geçmişi Yönetimi

Velilerin önceki konuşmalarını hatırlamak için farklı yöntemler uygulanabilir:

| Yöntem | Nasıl Çalışır | Kullanıcı Deneyimi |
|--------|---------------|-------------------|
| **Anonim** | Her ziyarette yeni oturum | Geçmiş hatırlanmaz |
| **Çerez ile Hatırlama** | Tarayıcı çerezi kullanılır | Aynı cihazda geçmiş hatırlanır |
| **Telefon ile Giriş** | Telefon numarası ile tanıma | Farklı cihazlarda da geçmiş erişilebilir |

**Hibrit Yaklaşım:** Çerez ile başlayıp, randevu talep eden velilerden telefon numarası almak, hem kullanım kolaylığı hem de takip imkanı sağlar.

---

## 5. Web Sitesi Entegrasyonu

### Seçenek 1: Sohbet Balonu (Widget)
Web sitenizin sağ alt köşesinde bir sohbet balonu olarak yer alır. Tıklandığında asistan açılır.

### Seçenek 2: Ayrı Sayfa
Asistan, `cozumkoleji.com/veli-asistan` gibi ayrı bir sayfada tam ekran olarak çalışır.

---

## 6. Zaman Planı

### Faz 1: Belge Toplama (2 Hafta)

| Tarih | Görev | Sorumlu |
|-------|-------|---------|
| 15 Aralık | Teklif ve Eksik Belge Analiz Formu gönderimi | Biz |
| 15-29 Aralık | Form doldurma ve eksik belgelerin tamamlanması | Çözüm Koleji |

**Eksik Belge Analiz Formu Hakkında:**
Form, farklı kategorilerde (eğitim, sınav, sanat, spor vb.) sorular içermektedir. Her kategori için 5 soru bulunur. Mevcut dokümanlarda yanıtı olmayan sorular için ek doküman talep edilecektir.

> ⚠️ **Önemli:** Belgelerin **29 Aralık'a kadar** tamamlanması gerekmektedir.

---

### Faz 2: Geliştirme (3 Hafta)

| Tarih | Görev | Sorumlu | Süre |
|-------|-------|---------|------|
| 23-27 Aralık | Doküman işleme ve veri hazırlama | Biz | 5 gün |
| 28 Aralık - 5 Ocak | Temel asistan sistemi kurulumu | Biz | 9 gün |
| 6-12 Ocak | Etkinlik modülü geliştirme | Biz | 7 gün |

---

### Faz 3: Entegrasyon ve Test (2 Hafta)

| Tarih | Görev | Sorumlu | Süre |
|-------|-------|---------|------|
| 13-17 Ocak | Web sitesi entegrasyonu ve iç testler | Her iki taraf | 5 gün |
| 18-24 Ocak | Kapsamlı test ve düzeltmeler | Çözüm Koleji + Biz | 7 gün |
| **25-31 Ocak** | **🚀 Canlıya Alım** | Her iki taraf | 7 gün |

**Toplam Süre:** ~6 hafta (15 Aralık - 31 Ocak)

> **Not:** Belge teslimindeki gecikmeler, canlıya alım tarihini doğrudan etkiler.

---

## 7. Maliyet Tablosu

### Aylık İşletme Maliyeti

Aylık maliyet, kullanım yoğunluğuna göre değişmektedir.

#### Yapay Zeka API Maliyeti Hesaplaması

Sohbet geçmişi tutulduğunda, her yeni mesajda önceki konuşmalar da sisteme gönderilir:

**API Fiyatlandırması:**
- Input: $1.00 / 1M token
- Output: $2.50 / 1M token

| Mesaj # | Input Token | Output Token | Kümülatif Maliyet |
|---------|-------------|--------------|-------------------|
| 1 | 5.000 | 500 | 0,21 ₺ |
| 2 | 12.000 | 500 | 0,67 ₺ |
| 3 | 25.000 | 500 | 1,58 ₺ |
| 4 | 40.000 | 500 | 3,02 ₺ |
| 5 | 60.000 | 500 | 5,16 ₺ |
| 6 | 90.000 | 500 | 8,35 ₺ |
| 7 | 120.000 | 500 | 12,59 ₺ |

**Ortalama oturum (7 mesaj): ~12,59 ₺**

---

#### Aylık Kullanım Senaryoları

| Senaryo | Günlük Kullanıcı | Aylık Oturum | API Maliyeti | Sunucu | Bakım | **Aylık Toplam** |
|---------|------------------|--------------|--------------|--------|-------|------------------|
| **Düşük Kullanım** | 5-10 | ~200 | 2.520 ₺ | 1.000 ₺ | 500 ₺ | **4.020 ₺** |
| **Orta Kullanım** | 15-20 | ~500 | 6.295 ₺ | 1.250 ₺ | 750 ₺ | **8.295 ₺** |
| **Yoğun Kullanım** | 30-40 | ~1.000 | 12.590 ₺ | 1.500 ₺ | 1.000 ₺ | **15.090 ₺** |
| **Çok Yoğun** | 50+ | ~1.500 | 18.885 ₺ | 1.750 ₺ | 1.000 ₺ | **21.635 ₺** |

---

#### Maliyet Düşürme Seçenekleri

| Optimizasyon | Tasarruf | Açıklama |
|--------------|----------|----------|
| Geçmiş sınırlama (son 5 mesaj) | %40 | Token kullanımı azalır, oturum başı ~7,5 ₺ |
| Özet sistemi | %50 | Eski mesajlar özetlenerek saklanır, oturum başı ~6,3 ₺ |
| Anonim mod (geçmiş tutulmaz) | %70 | Her oturum bağımsız başlar, oturum başı ~3,8 ₺ |

---

## 💰 Mobil Uygulama Maliyetleri

### Mağaza Hesap Ücretleri

| Platform | Ücret | Ödeme Türü | Açıklama |
|----------|-------|------------|----------|
| **Google Play Store** | $25 (≈850 ₺) | Tek seferlik | Bir kez ödenir, süresiz geçerli |
| **Apple App Store** | $99/yıl (≈3.350 ₺) | Yıllık abonelik | Her yıl yenilenmesi gerekir |

**Toplam İlk Yıl:** ~4.200 ₺  
**Sonraki Yıllar:** ~3.350 ₺/yıl (sadece Apple)

---

### Mobil Uygulama Geliştirme Maliyeti

Veli asistanının mobil uygulama versiyonu için tahmini maliyet:

| Özellik | iOS | Android | Açıklama |
|---------|-----|---------|----------|
| **Temel Uygulama** | ✅ | ✅ | Sohbet arayüzü, bildirimler |
| **Push Notification** | ✅ | ✅ | Etkinlik/duyuru bildirimleri |
| **Offline Mod** | ⚠️ | ⚠️ | Sınırlı (önbellek) |
| **Biyometrik Giriş** | ✅ | ✅ | Face ID / Parmak izi |

**Geliştirme Süresi:** 4-6 hafta  
**Tahmini Maliyet:** 75.000 - 120.000 ₺

> **Not:** Mobil uygulama, web versiyonunun tamamlanmasından sonra ayrı bir proje olarak planlanabilir. İlk etapta web sitesi entegrasyonu önerilir.

---

## 📋 Karar Gerektiren Konular

Lütfen aşağıdaki konularda tercihinizi bildiriniz:

| # | Konu | Seçenekler |
|---|------|------------|
| 1 | Etkinlik Bilgisi Kaynağı | ☐ Senaryo A (Admin Panel) ☐ Senaryo B (Web) ☐ Senaryo C (Instagram) |
| 2 | Sohbet Geçmişi Yöntemi | ☐ Anonim ☐ Çerez ☐ Telefon ☐ Hibrit |
| 3 | Geçmiş Saklama Süresi | ☐ 30 Gün ☐ 90 Gün ☐ 1 Yıl |

---

## 📞 İletişim

Sorularınız için:

**[Adınız Soyadınız]**  
[Telefon Numaranız]  
[E-posta Adresiniz]

---

*Bu belge, proje süreci boyunca güncellenebilir.*
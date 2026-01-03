# 🗺️ Çözüm Koleji Veli Asistanı - Yol Haritası

> **Son Güncelleme:** 12 Aralık 2024  
> **Hedef Go-Live:** Ocak 2025 Sonu  
> **Proje Tipi:** RAG-based AI Chatbot API

---

## 📋 Executive Summary

Bu doküman, Çözüm Koleji Veli Asistanı projesinin teknik planlamasını, zaman çizelgesini ve bütçe tahminlerini içermektedir. Proje, bir **API servisi** olarak sunulacak ve web frontend başka bir ekip tarafından geliştirilecektir.

---

## 🔴 Mevcut Sorunlar ve Çözüm Önerileri

### Sorun 1: Bağlamsal Takip (Context Awareness)

**Problem:** İkinci soru sorulduğunda (örn: "Peki ücretleri?") sistem bunu yeni bir soru olarak algılıyor ve alakasız sonuçlar getiriyor veya hiç sonuç bulamıyor.

**Kök Neden:** 
- Intent detection "followup" sınıflandırması yetersiz
- Query rewriting mekanizması yok

**Çözüm: Hibrit Query Rewriting** ✅ ONAYLANDI
```
Kullanıcı: "Peki ücretleri?"
     ↓
[Intent: followup tespit edilirse]
     ↓
LLM ile sorguyu yeniden yaz: "Lise spor faaliyetlerinin ücretleri nedir?"
     ↓
Yeniden yazılmış sorgu ile retrieve yap
```

**Teknik Implementasyon:**
- [ ] `query_rewriter_node.py` oluştur
- [ ] Intent "followup" ise → rewriter node'a yönlendir
- [ ] Son 3 mesaj context olarak ver, tam soru çıkar
- [ ] Workflow'a conditional edge ekle

**Tahmini Süre:** 2-3 gün

---

### Sorun 2: Eksik Dokümanlar ve Kategori Sistemi

**Problem:** Mevcut dokümanlar yetersiz. Müşteriden kategori bazlı (eğitim, sanat, spor, sınav hazırlık) yeni içerik gelecek.

**Çözüm:**
1. Müşteriden gelen dokümanları işlemek için **batch processing script**
2. Kademe (anaokulu, ilkokul, ortaokul, lise) + kategori bazlı **metadata tagging**
3. Tek FAISS index, metadata filtering ile arama

**Chunk Yapısı (Önerilen):**
```json
{
  "id": "lise-spor-01",
  "level": "lise",
  "category": "spor",
  "title": "Voleybol Takımı",
  "content": "...",
  "embedding_hint": "..."
}
```

**Teknik Implementasyon:**
- [ ] `document_processor.py` script'i (docx/csv → JSON chunks)
- [ ] Kategori metadata sistemi
- [ ] Retriever'a kategori filter desteği
- [ ] Admin için basit CLI: `python process_docs.py --file yeni_dokuman.docx`

**Tahmini Süre:** 3-4 gün

---

### Sorun 3: Web & Instagram Etkinlik Bilgisi

**Problem:** Web sitesi ve Instagram'dan etkinlik çekme isteniyor ama senaryo belirsiz.

### 📋 MÜŞTERİYE SUNULACAK İKİ SENARYO

---

#### Senaryo A: Admin Panel Yaklaşımı ⭐ (Önerilen)

```
[Admin Panel] → [API Endpoint] → [FAISS Index]
     ↓
Etkinlik ekle: Başlık, Tarih, Açıklama, Görsel
     ↓
Otomatik indexleme (real-time veya batch)
```

| ✅ Avantajlar | ❌ Dezavantajlar |
|--------------|------------------|
| Güvenilir ve stabil | Manuel veri girişi gerekir |
| İçerik kontrolü müşteride | Personel zamanı harcar |
| Yasal sorunlar yok | İlk kurulum gerekir |
| Düşük bakım maliyeti | |

**Geliştirme Süresi:** 2-3 gün  
**Aylık Bakım:** Minimal (~1 saat/ay)  
**Maliyet:** 2.000-3.000 ₺

---

#### Senaryo B: Web Scraping + Instagram API

```
[Scheduler] → [Web Scraper] → [FAISS Index]
              ↓
         [Instagram API]
```

| ✅ Avantajlar | ❌ Dezavantajlar |
|--------------|------------------|
| Otomatik veri çekme | Site yapısı değişirse bozulur |
| Manuel iş yok | Instagram API approval süreci (2-4 hafta) |
| Gerçek zamanlı güncelleme | Yasal riskler (TOS ihlali) |
| | Yüksek bakım maliyeti |

**Geliştirme Süresi:** 4-5 gün  
**Aylık Bakım:** Orta-Yüksek (~3-5 saat/ay)  
**Maliyet:** 4.000-5.000 ₺ + bakım

---

> **📝 Not:** Müşteriden hangi senaryoyu tercih ettikleri sorulacak. Admin Panel yaklaşımı önerilmektedir.

---

## 📅 Proje Çizelgesi

### Aralık 2024 (Kalan ~3 Hafta)

| Hafta | Tarih | Görevler | Durum |
|-------|-------|----------|-------|
| **Hafta 1** | 12-15 Ara | Query Rewriting implementasyonu | 🔄 Planlandı |
| | | Müşteri dokümanları teslim alınır | ⏳ Bekleniyor |
| **Hafta 2** | 16-22 Ara | Doküman işleme pipeline'ı | 🔄 Planlandı |
| | | Yeni chunk'ların indexlenmesi | 🔄 Planlandı |
| | | Kategori sistemi implementasyonu | 🔄 Planlandı |
| **Hafta 3** | 23-31 Ara | Etkinlik modülü (Admin Panel yaklaşımı) | 🔄 Planlandı |
| | | API endpoint'lerinin finalizasyonu | 🔄 Planlandı |
| | | Internal testing | 🔄 Planlandı |

### Ocak 2025 (4 Hafta)

| Hafta | Tarih | Görevler | Durum |
|-------|-------|----------|-------|
| **Hafta 1** | 1-5 Oca | API dokumentasyonu (Swagger/OpenAPI) | 🔄 Planlandı |
| | | Web ekibiyle entegrasyon toplantısı | 🔄 Planlandı |
| **Hafta 2** | 6-12 Oca | Entegrasyon testleri | 🔄 Planlandı |
| | | Bug fixes | 🔄 Planlandı |
| **Hafta 3** | 13-19 Oca | Staging deployment | 🔄 Planlandı |
| | | Randevu sistemi API entegrasyonu | 🔄 Planlandı |
| **Hafta 4** | 20-26 Oca | Production deployment | 🔄 Planlandı |
| | | Monitoring setup | 🔄 Planlandı |
| **Go-Live** | 27-31 Oca | 🚀 Canlıya Alma | 🎯 Hedef |

---

## 💰 Bütçe Tahmini

### A. Geliştirme Maliyeti (One-Time)

**Günlük Ücret: 1.000 ₺**

| Modül | Tahmini Süre | Maliyet |
|-------|--------------|----------|
| Query Rewriting | 2-3 gün | 2.000-3.000 ₺ |
| Doküman Pipeline | 3-4 gün | 3.000-4.000 ₺ |
| Etkinlik Modülü* | 2-5 gün | 2.000-5.000 ₺ |
| API Finalizasyonu | 2-3 gün | 2.000-3.000 ₺ |
| Entegrasyon & Test | 3-4 gün | 3.000-4.000 ₺ |
| Deployment | 1-2 gün | 1.000-2.000 ₺ |
| **TOPLAM** | **13-21 gün** | **13.000-21.000 ₺** |

> *Etkinlik modülü müşteri tercihine göre değişir (Admin Panel: 2-3 gün, Scraping: 4-5 gün)

---

### B. API Maliyetleri (Aylık - Tahmini)

| Servis | Birim Fiyat | Tahmini Kullanım | Aylık Maliyet |
|--------|-------------|------------------|---------------|
| **Gemini 2.0 Flash** | | | |
| - Input tokens | $0.10 / 1M | ~3M tokens/ay | ~$0.30 |
| - Output tokens | $0.40 / 1M | ~1M tokens/ay | ~$0.40 |
| **Gemini Embeddings** | $0.00 (free tier) | ~100K/ay | $0.00 |
| **Hosting (VPS)** | ~$20-50/ay | 1 sunucu | ~$35 |
| **TOPLAM** | | | **~$35-50/ay** |

> **Notlar:**
> - Kullanım arttıkça API maliyeti artabilir
> - İlk aylar düşük, kullanıcı sayısı arttıkça yükselir
> - Production'da caching ile optimize edilebilir

---

### C. Bakım Maliyetleri (Aylık)

**Saatlik Ücret: 125 ₺** (1000 ₺ / 8 saat)

| Kalem | Açıklama | Tahmini Maliyet |
|-------|----------|-----------------|
| Bug fixes | Haftalık 2-4 saat | 1.000-2.000 ₺/ay |
| Yeni doküman ekleme | İstek üzerine | 250-500 ₺/doküman |
| Monitoring & alerting | Otomatik | Hosting içinde |
| Major updates | Çeyreklik | Ayrı fiyatlandırma |
| **Aylık Minimum Bakım** | 4-8 saat | **500-1.000 ₺/ay** |

---

## 🔧 Teknik Mimari (Final)

```
┌─────────────────────────────────────────────────────────────┐
│                        WEB FRONTEND                          │
│                    (Başka ekip tarafından)                   │
└─────────────────────────┬───────────────────────────────────┘
                          │ REST API
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                     CHATBOT API (Bizim)                      │
├─────────────────────────────────────────────────────────────┤
│  POST /chat                                                  │
│  ├── user_query: str                                        │
│  ├── thread_id: str (session tracking)                      │
│  ├── levels: list (kademe seçimi)                           │
│  └── categories: list (optional filter)                     │
│                                                              │
│  Response:                                                   │
│  ├── answer: str                                            │
│  ├── sources: list (kaynaklar)                              │
│  └── next_thread_id: str                                    │
├─────────────────────────────────────────────────────────────┤
│  POST /events (Admin Panel için)                            │
│  ├── title, date, description, image_url                    │
│  └── auto_index: bool                                       │
├─────────────────────────────────────────────────────────────┤
│  GET /health                                                 │
│  └── status, version, uptime                                │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    LANGGRAPH WORKFLOW                        │
├─────────────────────────────────────────────────────────────┤
│  Intent Detection → Router                                   │
│       ↓                                                      │
│  ┌────┼────┬────────┬──────────┐                            │
│  ↓    ↓    ↓        ↓          ↓                            │
│ Query Retrieve News  Price   Direct                         │
│ Rewrite  ↓    ↓       ↓        ↓                            │
│  ↓    Compress ← ← ← ←         │                            │
│  ↓       ↓                     │                            │
│  └──→ Answer ←─────────────────┘                            │
│          ↓                                                   │
│        END                                                   │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                      DATA LAYER                              │
├─────────────────────────────────────────────────────────────┤
│  FAISS Index (Vector DB)                                    │
│  ├── Kademe metadata (anaokulu, ilkokul, ortaokul, lise)   │
│  ├── Kategori metadata (eğitim, spor, sanat, sınav)        │
│  └── Etkinlik chunks (admin panel'den)                      │
├─────────────────────────────────────────────────────────────┤
│  Conversation Memory (Redis veya In-Memory)                 │
│  └── Thread-based session storage                           │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚠️ Riskler ve Azaltma Stratejileri

| Risk | Olasılık | Etki | Azaltma |
|------|----------|------|---------|
| Müşteri dokümanları gecikmesi | Orta | Yüksek | Paralel çalışma, placeholder data |
| Web ekibiyle entegrasyon sorunları | Orta | Orta | Erken API spec paylaşımı, mock server |
| Gemini API kesintileri | Düşük | Yüksek | Retry mekanizması, fallback mesajlar |
| Yetersiz chunk kalitesi | Orta | Orta | İteratif iyileştirme, müşteri feedback |

---

## 📝 Sonraki Adımlar (Hemen Yapılacaklar)

1. [ ] Müşteriden doküman teslimi (1-2 gün içinde)
2. [ ] Query Rewriting implementasyonuna başla
3. [ ] Web ekibiyle API spec toplantısı planla
4. [ ] Admin Panel vs Scraping kararını müşteriyle görüş
5. [ ] Günlük/saatlik ücret bilgisini bütçeye ekle

---

## 📎 Ekler

### Mevcut Teknik Borç (Technical Debt)
Detaylar için bkz: [eksik.md](./eksik.md), [yapılacaklar.md](./yapılacaklar.md)

### Randevu Sistemi Notu
Randevu sistemi backend'i web ekibi tarafından yapılacak. Bizim API'miz şu durumlarda randevu önerebilir:
- Kullanıcı "görüşme istiyorum" dediğinde
- Belirli intent'lerde (ücret, kayıt vb.) otomatik öneri

Entegrasyon için web ekibinden endpoint bilgisi alınacak.

---

*Bu doküman, proje ilerledikçe güncellenecektir.*

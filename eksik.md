# Eksik Listesi ve Geliştirme Önerileri

Bu dosya, mevcut projenin incelenmesi sonucunda tespit edilen eksiklikleri ve geliştirilmesi gereken noktaları içermektedir.

## 1. Kritik Teknik Eksiklikler

- [ ] **Test Altyapısı**: Projede şu anda birim test (unit test) veya entegrasyon testi bulunmamaktadır. Kritik fonksiyonların (`intent_detector.py`, `router_node.py` vb.) test edilmesi gerekmektedir.
- [ ] **Hata Yönetimi (Error Handling)**: Node'lar içerisinde kapsamlı hata yakalama mekanizmaları eksik. API çağrılarının başarısız olması durumunda sistemin nasıl davranacağı (retry, fallback vb.) net değil.
- [ ] **Loglama (Logging)**: Konuşma geçmişi ve sistem hataları için yapılandırılmış bir loglama sistemi yok. `print` ifadeleri yerine `logging` modülü kullanılmalı ve loglar dosyaya veya bir izleme servisine yazılmalı.
- [ ] **Konfigürasyon Yönetimi**: API anahtarları ve diğer ayarlar `.env` dosyasından okunuyor olsa da, bu ayarların doğrulanması ve yönetilmesi için daha sağlam bir yapı (örn. Pydantic settings) kurulabilir.

## 2. RAG ve AI İyileştirmeleri

- [ ] **Intent Detection Hassasiyeti**: `buyuk-sıkıntı.md` dosyasında belirtildiği gibi, intent detection bazen gereksiz yere retrieval yapıyor veya yanlış sınıflandırıyor. Özellikle bağlama dayalı (context-aware) soruların sınıflandırılması iyileştirilmeli.
- [ ] **Retrieval Optimizasyonu**: Her soruda retrieval yapmak yerine, sadece gerekli durumlarda (okul bilgisi gerektiren sorular) retrieval yapılmalı. "Merhaba", "Nasılsın" gibi sorularda retrieval atlanmalı.
- [ ] **Query Rewriting (Sorgu Yeniden Yazma)**: "Peki ya ücretleri?" veya "O ne zaman?" gibi bağlama dayalı soruların, geçmiş konuşma geçmişi kullanılarak "Lise eğitim ücretleri nedir?" şekline dönüştürülmesi (Condense Question) gereklidir. Mevcut yapıda bu eksiktir.
- [ ] **Hybrid Search & Reranking**: Sadece semantik arama yerine, anahtar kelime eşleşmesi (BM25) ve semantik aramanın birleşimi (Hybrid Search) kullanılmalı. Ayrıca sonuçların yeniden sıralanması (Reranking) doğruluğu artıracaktır.
- [ ] **Chunking Stratejisi**: Mevcut chunk'ların boyutu ve içeriği optimize edilebilir. Tabloların ve listelerin daha iyi işlenmesi gerekebilir.

## 3. Kullanıcı Deneyimi (UX) ve Arayüz

- [ ] **Streaming Responses**: Yanıtlar şu anda blok halinde geliyor. Kullanıcı deneyimini artırmak için yanıtların kelime kelime (streaming) akması sağlanmalı.
- [ ] **Yükleniyor Göstergeleri**: İşlem yapılırken kullanıcıya daha detaylı bilgi verilebilir (örn. "Dökümanlar taranıyor...", "Yanıt oluşturuluyor...").
- [ ] **Oturum Sürekliliği**: Sayfa yenilendiğinde sohbet geçmişi kayboluyor olabilir (Streamlit doğası gereği). `st.session_state` kullanımı mevcut ama kalıcı bir veritabanı (SQLite, PostgreSQL vb.) ile geçmişin saklanması daha iyi olur.

## 4. Dokümantasyon ve Deployment

- [ ] **API Dokümantasyonu**: Fonksiyonların ve modüllerin ne işe yaradığını, hangi parametreleri aldığını açıklayan docstring'ler ve ayrı bir API dokümanı eksik.
- [ ] **Deployment Hazırlığı**: Projenin canlıya alınması için gerekli `Dockerfile` ve deployment script'leri (Docker Compose, Kubernetes vb.) bulunmuyor.
- [ ] **Mimarisi Diyagramı**: Sistemin nasıl çalıştığını gösteren güncel bir mimari diyagramı (Mermaid veya görsel) dokümantasyona eklenmeli.

## 5. Güvenlik

- [ ] **Girdi Doğrulama**: Kullanıcı girdilerinin (prompt injection vb. saldırılara karşı) temizlenmesi ve doğrulanması.
- [ ] **Rate Limiting**: API'nin kötüye kullanımını engellemek için hız sınırlaması (rate limiting) eklenmeli.

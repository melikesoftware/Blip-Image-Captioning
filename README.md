Hazır Model Öğrenimi: BLIP Image Captioning

## Assignment: Hazır Model Ödev Teslimi

Bu proje, Transfer Learning kavramını uygulamak için Salesforce BLIP (Bootstrapping Language-Image Pre-training) modelini kullanarak görsel açıklama (image captioning) sistemi geliştirmeyi amaçlamaktadır.



## Ödev Bilgileri

- **Ders:** Yapay Zeka / Derin Öğrenme
- **Konu:** Transfer Learning ve Hazır Modeller
- **Model:** Salesforce BLIP Image Captioning Base
- **Tarih:** Mayıs 2026

---

## Transfer Learning Nedir?

Transfer Learning, önceden eğitilmiş bir modelin (pre-trained model) belirli bir görev için eğitilmiş ağırlıklarını alıp, farklı bir görevde kullanma tekniğidir. Bu yaklaşım:

- **Zaman tasarrufu** sağlar (sıfırdan eğitim yerine)
- **Daha az veri** ile yüksek performans elde edilir
- **Hesaplama kaynaklarından tasarruf** sağlar
- **Daha iyi genelleme** yeteneği sunar

---

## BLIP Modeli Hakkında

**BLIP (Bootstrapping Language-Image Pre-training)**, Salesforce tarafından geliştirilen bir görüntü-metin modelidir.

- **Model:** `Salesforce/blip-image-captioning-base`
- **Görev:** Görsel açıklama oluşturma (Image Captioning)
- **Framework:** Transformers (Hugging Face)
- **Dil:** İngilizce (Türkçe çeviri ile desteklenir)

### Model Özellikleri

- **Parametre Sayısı:** ~390M
- **Girdi:** Görsel (resim)
- **Çıktı:** Görsel açıklama (metin)
- **Eğitim Verisi:** COCO Captions, Visual Genome, vb.

---

## Proje Yapısı

```
PythonProject26/
├── blip_service.py          # BLIP model servisi
├── blip_web_app.py          # FastAPI web uygulaması
├── requirements.txt         # Python bağımlılıkları
├── static/
│   ├── blip_style.css       # Stil dosyası
│   └── blip_app.js          # JavaScript kodu
└── templates/
    └── blip_index.html     # HTML arayüzü
```

---

## Kurulum

### 1. Sanal Ortam Oluşturma

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Bağımlılıkları Yükleme

```bash
pip install -r requirements.txt
```

### 3. Uygulamayı Çalıştırma

```bash
python blip_web_app.py
```

Tarayıcıda açın: http://127.0.0.1:8001

---

## Kullanım

### Web Arayüzü

1. **Görsel Yükle:** Sürükle-bırak veya tıklayarak görsel seçin
2. **Açıklama Oluştur:** "Açıklama Oluştur" butonuna tıklayın
3. **Sonucu Gör:** Türkçe açıklama otomatik olarak oluşturulur
4. **Yeni Görsel:** "Yeni Resim Yükle" butonu ile başka görsel deneyin

### Özellikler

- ✅ Sürükle-bırak görsel yükleme
- ✅ Otomatik Türkçe çeviri
- ✅ Sayfa yenilemeden yeni görsel yükleme
- ✅ Detaylı açıklama (max_length=100, num_beams=5)
- ✅ Modern ve responsive arayüz

---

## Teknik Detaylar

### Model Konfigürasyonu

```python
# BLIP Model Parametreleri
max_length = 100          # Maksimum açıklama uzunluğu
num_beams = 5             # Beam search parametresi
early_stopping = True     # Erken durdurma
```

### Türkçe Çeviri

- **Kütüphane:** deep-translator
- **Kaynak Dil:** Otomatik (İngilizce)
- **Hedef Dil:** Türkçe

### Web Framework

- **Framework:** FastAPI
- **Template Engine:** Jinja2
- **Static Files:** CSS, JavaScript
- **Port:** 8001

---

## Transfer Learning Uygulaması

Bu projede transfer learning şu şekilde uygulanmıştır:

1. **Hazır Model Yükleme:** Hugging Face'den BLIP modeli indirildi
2. **Model Adaptasyonu:** Görsel açıklama görevi için kullanıldı
3. **Parametre Ayarları:** Model çıktısı optimize edildi
4. **Dil Adaptasyonu:** Türkçe çeviri katmanı eklendi

### Avantajlar

- ✅ Sıfırdan eğitime gerek yok
- ✅ COCO veri seti ile eğitilmiş ağırlıklar kullanıldı
- ✅ Yüksek performans (milyonlarca görsel üzerinde eğitildi)
- ✅ Hızlı implementasyon

---

## Performans

### Model Çıktı Örnekleri

| Görsel | İngilizce Açıklama | Türkçe Açıklama |
|--------|-------------------|-----------------|
| Pasta | "a close up of a pastry on a spoon" | "bir kaşık üzerindeki bir pastanın yakın çekimi" |
| Köpek | "a dog running in the grass" | "çimlerde koşan bir köpek" |

### Sistem Gereksinimleri

- **Python:** 3.8+
- **RAM:** 8 GB+ (CPU), 12 GB+ (GPU önerilir)
- **Disk:** ~2 GB (model cache)
- **İnternet:** İlk çalıştırmada model indirme için gerekli

---

## Öğrenme Kazanımları

Bu proje ile aşağıdaki konular öğrenildi:

1. **Transfer Learning** kavramı ve uygulaması
2. **Hugging Face Transformers** kullanımı
3. **Pre-trained Models** entegrasyonu
4. **FastAPI** ile web uygulaması geliştirme
5. **Model Fine-tuning** parametre optimizasyonu
6. **Dil Adaptasyonu** ve çeviri entegrasyonu



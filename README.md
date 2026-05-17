# Hazır Model Öğrenimi: BLIP Image Captioning

## Hazır Model ile Görsel Açıklama (BLIP Image Captioning)

Bu proje, Hugging Face üzerindeki hazır eğitilmiş (pre-trained) Salesforce BLIP modelini doğrudan kullanarak, yüklenen görsellere otomatik olarak İngilizce ve Türkçe açıklamalar (image captioning) üreten bir web uygulamasıdır. Proje mimarisi ve arayüzü Windsurf AI yardımıyla geliştirilmiştir.

---

## Özellikler

✅ **Sıfır Eğitim (Zero-Shot):** Model yeniden eğitilmeden, Hugging Face ağırlıklarıyla doğrudan tahmin yapar.

🖼️ **Sürükle-Bırak Arayüzü:** FastAPI ve modern JavaScript ile sayfa yenilenmeden dinamik görsel yükleme.

🌐 **Çok Dilli Destek:** deep-translator entegrasyonu ile anlık Türkçe çeviri.

⚙️ **Gelişmiş Çıkarım (Inference):** Beam search ($num\_beams=5$) ve uzunluk optimizasyonu ile kaliteli metin üretimi.

---

## Model Özeti

| Metrik / Özellik | Değer / Açıklama |
|------------------|------------------|
| Kullanılan Model | Salesforce/blip-image-captioning-base (Hugging Face) |
| Parametre Sayısı | ~390 Milyon |
| Görev (Task) | Image-to-Text (Görsel Açıklama Oluşturma) |
| Temel Teknolojiler | FastAPI, PyTorch, Transformers, Jinja2 |
| Model Çıkarım Parametreleri | max_length=100, num_beams=5, early_stopping=True |

---

## Proje Yapısı

```
PythonProject26/
├── blip_service.py       # Hugging Face model yükleme ve çıkarım (inference)
├── blip_web_app.py       # FastAPI backend ve API uç noktaları
├── requirements.txt      # Bağımlılık listesi
├── templates/
│   └── blip_index.html   # HTML arayüzü (Jinja2)
└── static/
    ├── blip_style.css    # Responsive CSS tasarımı
    └── blip_app.js       # Sürükle-bırak ve API isteklerini yöneten JS
```

---

## Kurulum

### 1. Sanal Ortam Oluşturma & Aktifleştirme

```bash
python -m venv .venv

# Windows için:
.venv\Scripts\activate
# macOS / Linux için:
source .venv/bin/activate
```

### 2. Bağımlılıkları Yükleme

```bash
pip install -r requirements.txt
```

---

## Kullanım

Uygulamayı başlatmak için terminalde şu komutu çalıştırın:

```bash
python blip_web_app.py
```

Tarayıcınızda şu adrese gidin: http://127.0.0.1:8001

💡 **Not:** İlk çalıştırmada ~390M parametrelik BLIP modeli Hugging Face hub üzerinden yerel bilgisayarınıza (~/.cache) otomatik olarak indirilir. Sonraki çalıştırmalarda internet gerekmez.

---

## Model Çıktı Örnekleri

| Girdi Görseli | Üretilen İngilizce Açıklama | Otomatik Türkçe Çeviri |
|---------------|----------------------------|------------------------|
| [Yüklenen Pasta Resmi] | "a close up of a pastry on a spoon" | "bir kaşık üzerindeki bir pastanın yakın çekimi" |
| [Yüklenen Köpek Resmi] | "a dog running in the grass" | "çimlerde koşan bir köpek" |

---

## Sistem Gereksinimleri

- **Python:** 3.8+
- **RAM:** En az 8 GB (CPU modu için) / 4 GB VRAM (GPU/CUDA modu için)
- **Depolama:** ~2 GB boş disk alanı (Model cache için)

# 🚦 Traffic Sign Recognition API

Bu proje, Almanya Trafik İşaretleri Veri Seti (GTSRB) kullanılarak eğitilmiş bir derin öğrenme modelini kullanarak trafik işaretlerini sınıflandıran bir FastAPI uygulamasıdır. **Bu API, trafik işaretlerinin türünü tahmin etmek için önceden eğitilmiş bir sinir ağını kullanır.**

---


## 🚀 Özellikler

- Görseller üzerinden trafik işareti sınıflandırması
- JSON formatında sonuç döndürme
- Kolay entegrasyon için CORS desteği

---

## 🛠 Gereksinimler

- Python 3.10+
- TensorFlow
- FastAPI
- scikit-image
- pillow
- uvicorn

### Kurulum için:

🚀 API Nasıl Çalıştırılır?
Sanal ortam oluştur (isteğe bağlı):

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate.bat  # Windows
```

Gereksinimleri yükle:

```bash
pip install -r requirements.txt   
```
API'yi başlat:

```bash
uvicorn main:app --reload
```
Varsayılan olarak http://localhost:8000 adresinde çalışır.

Link github :
### Anggota Kelompok
- **Nama:** Nisa Rianti(2208107010018)
- **Nama:** Akhsania Maisa Rahmah(2208107010017)
- **Nama:** Indriani Miza Alfiyanti (2208107010026)
- **Nama:** Zuwi Pertiwi (2208107010061)


# Animal Image Classification CNN

Proyek ini bertujuan untuk mengklasifikasikan gambar hewan (butterfly, cats, panda) menggunakan Convolutional Neural Network (CNN) dan membandingkan performa beberapa konfigurasi model untuk menentukan arsitektur terbaik.

Dataset dibagi menjadi tiga bagian:
- `train` (70%)
- `validation` (15%)
- `test` (15%)

Kelas gambar terdiri dari:
- `butterfly`
- `cats`
- `panda`

## 🧠 Arsitektur Model
Tiga model CNN diuji dengan konfigurasi berikut:

| Model    | Filters | Dropout |
|----------|---------|---------|
| model_1  | 32      | 0.3     |
| model_2  | 64      | 0.4     |
| model_3  | 128     | 0.5     |

### Layer Utama:
- Conv2D → MaxPooling2D (3x)
- Dropout untuk regularisasi
- Dense Layer (512 neuron)
- Output Layer (3 neuron + softmax)

## ⚙️ Training
- Optimizer: `Adam`
- Loss: `categorical_crossentropy`
- Augmentasi data untuk training menggunakan rotasi, zoom, flipping, dan shifting.
- Callbacks: `EarlyStopping` dan `ModelCheckpoint`.

## 📊 Hasil Evaluasi

| Model    | Accuracy | Precision | Recall | F1-Score |
|----------|----------|-----------|--------|----------|
| model_1  | **0.9207** | **0.9229**   | **0.9207** | **0.9205** |
| model_2  | 0.8592   | 0.8671    | 0.8592 | 0.8576   |
| model_3  | 0.8577   | 0.8745    | 0.8577 | 0.8555   |

Model terbaik adalah `model_1`.


## 🛠️ Tools & Library
- TensorFlow / Keras
- scikit-learn
- matplotlib & seaborn

# 🐾 Animal Image Classification Web App

Aplikasi web interaktif berbasis **Streamlit** untuk mengklasifikasikan gambar hewan ke dalam tiga kategori: **Butterfly (🦋)**, **Cat (🐱)**, dan **Panda (🐼)** menggunakan model deep learning berformat `.h5`.

## 📸 Tampilan Aplikasi

![demo](https://via.placeholder.com/800x400.png?text=Demo+Screenshot) <!-- Ganti dengan tangkapan layar -->

---

## 🚀 Fitur

- Upload gambar dalam format JPG/PNG
- Prediksi otomatis kelas gambar
- Menampilkan label hasil klasifikasi dan confidence score
- Tampilan UI sederhana dan responsif

---

## 🧠 Model

Model deep learning menggunakan arsitektur CNN yang telah dilatih dengan dataset citra hewan (minimal 100 gambar per kelas). File model disimpan dengan nama:

model_1.h5

java
Salin
Edit

Pastikan urutan kelas (`class_indices`) sesuai dengan urutan saat pelatihan model:

```python
class_indices = {'butterfly': 0, 'cats': 1, 'panda': 2}


## Jalankan aplikasi Streamlit:
python -m streamlit run app.py

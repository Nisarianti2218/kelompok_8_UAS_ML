import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# =====================
# Konfigurasi Awal
# =====================
st.set_page_config(page_title="Klasifikasi Gambar Hewan 🐾", layout="centered")
MODEL_PATH = "model_1.h5"  # Ganti jika kamu pakai model lain
model = load_model(MODEL_PATH)

# Label kelas (pastikan urutannya sesuai dengan model kamu)
class_indices = {'butterfly': 0, 'cats': 1, 'panda': 2}
class_labels = list(class_indices.keys())

# =====================
# Fungsi Prediksi
# =====================
def predict_image(img):
    img = img.resize((150, 150))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)[0]
    confidence = float(np.max(predictions))
    label_idx = np.argmax(predictions)
    predicted_label = class_labels[label_idx]

    return predicted_label, confidence

# =====================
# Sidebar
# =====================
with st.sidebar:
    st.title("📁 Navigasi")
    st.info("Upload gambar untuk mengklasifikasikan ke dalam:\n\n- 🦋 Butterfly\n- 🐱 Cat\n- 🐼 Panda")
    st.markdown("---")
    st.caption("Model: `model_1.h5`")

# =====================
# Header Aplikasi
# =====================
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>Klasifikasi Gambar Hewan 🐾</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# =====================
# Upload dan Prediksi
# =====================
uploaded_file = st.file_uploader("📤 Upload gambar JPG/PNG", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    
    st.image(image, caption="📸 Gambar yang diunggah", use_container_width=True)
    st.markdown("⏳ Mengklasifikasikan...")

    label, conf = predict_image(image)

    st.success(f"✅ Prediksi: **{label}** dengan confidence **{conf:.2f}**")

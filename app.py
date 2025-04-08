import streamlit as st
import cv2
import numpy as np
from PIL import Image as Image, ImageOps as ImagOps
from keras.models import load_model
import platform

# Carga del modelo
model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Estilos CSS personalizados
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }

        h1 {
            background: -webkit-linear-gradient(45deg, #00ff99, #ff69b4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 40px;
            text-align: center;
            margin-bottom: 30px;
        }

        h2, h3 {
            color: #00ff99;
        }

        .stButton>button {
            background-color: #ff69b4;
            color: white;
            border-radius: 20px;
            border: 2px solid #00ff99;
            padding: 0.5em 1.5em;
            font-size: 16px;
            margin: auto;
            display: block;
        }

        .camera-label {
            text-align: center;
            font-weight: bold;
            color: #ff69b4;
            margin-top: 20px;
        }

        .probabilidad {
            color: #00ff99;
            font-size: 24px;
        }
    </style>
""", unsafe_allow_html=True)

# Muestra versión de Python
st.caption(f"🐍 Versión de Python: {platform.python_version()}")

# Título
st.title("Reconocimiento de Imágenes")

# Imagen decorativa (puedes cambiar la ruta)
image = Image.open('nueva_imagen.jpg')  # cámbiala por tu propia imagen si quieres
st.image(image, width=350)

# Sidebar
with st.sidebar:
    st.markdown("### 🧠 Usa un modelo entrenado con [Teachable Machine](https://teachablemachine.withgoogle.com/) para identificar gestos desde la cámara.")

# Entrada de cámara
st.markdown("<div class='camera-label'>Toma una Foto</div>", unsafe_allow_html=True)
img_file_buffer = st.camera_input("")

# Procesamiento de imagen
if img_file_buffer is not None:
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    img = Image.open(img_file_buffer)
    img = img.resize((224, 224))
    img_array = np.array(img)

    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)

    if prediction[0][0] > 0.5:
        st.markdown(f"<div class='probabilidad'>🖐 Mano abierta, con probabilidad: {prediction[0][0]:.2f}</div>", unsafe_allow_html=True)

    if prediction[0][1] > 0.5:
        st.markdown(f"<div class='probabilidad'>✊ Mano cerrada, con probabilidad: {prediction[0][1]:.2f}</div>", unsafe_allow_html=True)






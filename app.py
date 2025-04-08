import streamlit as st
import cv2
import numpy as np
from PIL import Image as Image, ImageOps as ImagOps
from keras.models import load_model
import platform
import base64
import io

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
            animation: moveText 4s infinite alternate ease-in-out;
        }

        @keyframes moveText {
            0% { letter-spacing: 1px; transform: scale(1); }
            100% { letter-spacing: 4px; transform: scale(1.07); }
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
            text-align: center;
        }

        img {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
""", unsafe_allow_html=True)

# Muestra versión de Python
st.caption(f"🐍 Versión de Python: {platform.python_version()}")

# Título animado
st.title("Reconocimiento de Imágenes")

# Imagen centrada (mente.jpg)
image = Image.open("mente.jpg")
buffered = io.BytesIO()
image.save(buffered, format="PNG")
img_b64 = base64.b64encode(buffered.getvalue()).decode()
st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,{img_b64}' width='350'/>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.markdown("### 🧠 Usa un modelo entrenado con [Teachable Machine](https://teachablemachine.withgoogle.com/) para identificar gestos desde la cámara.")

# Entrada de cámara
st.markdown("<div class='camera-label'>📸 Toma una Foto</div






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
            background: linear-gradient(135deg, #ff69b420 25%, transparent 25%) -10px 0/ 20px 20px,
                        linear-gradient(225deg, #00ff9940 25%, transparent 25%) -10px 0/ 20px 20px,
                        linear-gradient(315deg, #69e0ff40 25%, transparent 25%) 0px 0/ 20px 20px,
                        linear-gradient(45deg, #ff69b420 25%, transparent 25%) 0px 0/ 20px 20px;
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

        .image-center {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Muestra versión de Python
st.caption(f"🐍 Versión de Python: {platform.python_version()}")

# Título
st.title("Reconocimiento de Imágenes")

# Imagen decorativa centrada




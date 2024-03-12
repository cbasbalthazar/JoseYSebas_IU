import streamlit as st
from PIL import Image

st.tittle ("Ciudades inteligentes")

st.header ("Este es un espacio para aprender sobre las ciudades inteligentes y su importancia")

image = image.open("Barcelona int.png")
st.image (image, caption = "Conexión IOT en barcelona")
st.write ("Hablar de inteligencia urbana es conectar a los ciudadanos con el entorno virtual para mejorar su calidad de vida")
st.write ("Ingresa al link para visualizar estos datos de la ciudad [lINK] (https://demo.thingsboard.io/dashboards/e2eb9330-e0a1-11ee-bc03-55147b89654f)")

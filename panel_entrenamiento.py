import streamlit as st
import json
import os
from services.firebase_service import guardar_respuesta

ruta_pendientes = "data/pendientes.json"

st.set_page_config(page_title="Panel de Entrenamiento", layout="centered")
st.title("🧠 Panel de Entrenamiento del Chatbot Bembos")

if os.path.exists(ruta_pendientes):
    with open(ruta_pendientes, "r", encoding="utf-8") as f:
        frases = json.load(f)
else:
    frases = []

if not frases:
    st.success("✅ No hay frases pendientes. ¡Tu chatbot está al día!")
else:
    st.info(f"Frases por entrenar: {len(frases)}")

    for frase in frases.copy():
        st.markdown(f"**🗨️ Cliente preguntó:** _{frase}_")
        nueva_respuesta = st.text_input(f"¿Qué debe responder el bot?", key=frase)

        if nueva_respuesta:
            guardar_respuesta(frase, nueva_respuesta)
            frases.remove(frase)
            st.success("Respuesta guardada con éxito.")
            with open(ruta_pendientes, "w", encoding="utf-8") as f:
                json.dump(frases, f, indent=2)
            st.rerun()

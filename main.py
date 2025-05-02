import streamlit as st
from core.chatbot import responder

st.set_page_config(page_title="BembosBot", layout="centered")
st.title("🤖 BembosBot - Atención Inteligente")
st.write("Pregunta lo que quieras sobre nuestros combos.")

msg = st.text_input("Tu mensaje:")

if msg:
    respuesta = responder(msg)
    st.markdown(f"**Bot:** {respuesta}")

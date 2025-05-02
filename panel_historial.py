import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Historial del Chatbot", layout="wide")
st.title("📜 Historial de Interacciones del Chatbot")

ruta = "data/historial.csv"

if os.path.exists(ruta):
    df = pd.read_csv(ruta)
    df = df.sort_values(by="fecha", ascending=False)

    if df.empty:
        st.info("No hay interacciones registradas aún.")
    else:
        st.dataframe(df, use_container_width=True)
        st.success(f"{len(df)} interacciones registradas.")

        # Exportar a Excel
        st.markdown("### 📁 Exportar historial")
        exportar = st.button("📥 Descargar en Excel")

        if exportar:
            ruta_excel = "historial_exportado.xlsx"
            df.to_excel(ruta_excel, index=False)
            with open(ruta_excel, "rb") as f:
                st.download_button(
                    label="Haz clic aquí para descargar el archivo Excel",
                    data=f,
                    file_name="historial_chatbot_bembos.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
else:
    st.warning("El archivo historial.csv no existe.")

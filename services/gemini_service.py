import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = None

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    except Exception as e:
        print(f"[ERROR] No se pudo configurar Gemini: {e}")


def responder_con_gemini(texto):
    if not model:
        return None
    try:
        respuesta = model.generate_content(texto)
        return respuesta.text.strip()
    except Exception as e:
        print(f"[ERROR] Gemini falló al responder: {e}")
        return None


def calcular_delivery_con_ia(distrito):
    if not model:
        return None
    try:
        prompt = (
            f"Calcular precio justo de delivery para el distrito '{distrito}' en Lima, Perú. "
            "Usa un mínimo de S/5.00 y ajusta el precio según la distancia desde el centro. "
            "Entrega solo el precio en soles, por ejemplo: 'S/7.50'"
        )
        respuesta = model.generate_content(prompt)
        texto = respuesta.text.strip()

        # Extraer valor en soles
        import re
        match = re.search(r"S/\s?(\d+(?:\.\d{1,2})?)", texto)
        if match:
            return f"S/{match.group(1)}"
        return None
    except Exception as e:
        print(f"[ERROR] Error al calcular delivery con Gemini: {e}")
        return None

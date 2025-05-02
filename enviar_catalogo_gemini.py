import os
from dotenv import load_dotenv
from twilio.rest import Client
from services.gemini_service import responder_con_gemini

# Cargar variables del archivo .env
load_dotenv()
sid = os.getenv("TWILIO_ACCOUNT_SID")
token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
cliente_number = os.getenv("MY_PHONE_NUMBER")

# Inicializar cliente de Twilio
client = Client(sid, token)

# Simular un mensaje que llega desde WhatsApp
mensaje_cliente = input("📥 Cliente dice por WhatsApp: ")

# Verificar si solicita el menú o catálogo
if "menú" in mensaje_cliente.lower() or "catalogo" in mensaje_cliente.lower() or "catálogo" in mensaje_cliente.lower():
    prompt = (
        f"El cliente ha escrito: '{mensaje_cliente}'. "
        "Responde de forma amable y profesional diciendo que le adjuntas el menú en PDF. "
        "Invítalo a explorar los combos y promociones."
    )
    respuesta = responder_con_gemini(prompt)

    print("\n✅ Enviando respuesta con catálogo...\n")

    # Enviar mensaje de texto con respuesta generada por Gemini
    client.messages.create(
        from_=twilio_number,
        to=cliente_number,
        body=respuesta
    )

    # Enviar el PDF (puedes usar un archivo tuyo o un link externo)
    pdf_url = "https://www.africau.edu/images/default/sample.pdf"  # reemplaza con tu URL
    client.messages.create(
        from_=twilio_number,
        to=cliente_number,
        media_url=[pdf_url]
    )

    print("✅ Catálogo enviado correctamente por WhatsApp.")
else:
    print("❌ El mensaje no contiene una solicitud de menú o catálogo.")

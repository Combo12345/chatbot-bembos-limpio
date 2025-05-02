from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from core.chatbot import responder
import os
from dotenv import load_dotenv

# Cargar variables del entorno
load_dotenv()

# Inicializar Flask
app = Flask(__name__)

# Ruta del webhook de WhatsApp
@app.route("/webhook", methods=["POST"])
def whatsapp_webhook():
    # Obtener el mensaje del usuario
    mensaje_entrante = request.form.get("Body")
    numero_cliente = request.form.get("From")
    print(f"📥 Mensaje de {numero_cliente}: {mensaje_entrante}")

    # Obtener respuesta del bot
    respuesta_bot = responder(mensaje_entrante)
    print(f"🤖 Respuesta del bot: {respuesta_bot}")

    # Crear respuesta de Twilio
    twilio_response = MessagingResponse()
    twilio_response.message(respuesta_bot)
    return str(twilio_response)

# Ejecutar el servidor local en el puerto 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

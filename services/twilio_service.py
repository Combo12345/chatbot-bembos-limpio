from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

# Leer credenciales desde .env
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
cliente_number = os.getenv("MY_PHONE_NUMBER")

client = Client(account_sid, auth_token)

def enviar_pdf_catalogo():
    client.messages.create(
        from_=twilio_number,
        to=cliente_number,
        body="📄 Aquí tienes el catálogo en PDF con nuestros combos y promociones.",
        media_url=["https://www.africau.edu/images/default/sample.pdf"]  # Reemplaza por tu URL real si tienes
    )

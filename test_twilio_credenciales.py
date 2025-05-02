from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

sid = os.getenv("TWILIO_ACCOUNT_SID")
token = os.getenv("TWILIO_AUTH_TOKEN")

try:
    client = Client(sid, token)
    account = client.api.accounts(sid).fetch()
    print("✅ Conexión exitosa con Twilio:")
    print(f"  - Nombre de cuenta: {account.friendly_name}")
    print(f"  - SID: {account.sid}")
except Exception as e:
    print("❌ Error autenticando con Twilio:")
    print(e)

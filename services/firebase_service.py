import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

# Leer las credenciales desde una variable de entorno segura
if not firebase_admin._apps:
    cred_data = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")
    cred_dict = json.loads(cred_data)
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()

def obtener_menus():
    try:
        ref = db.collection("menus")
        docs = ref.stream()
        menus = []
        for doc in docs:
            data = doc.to_dict()
            menus.append({
                "nombre": data.get("nombre", "Sin nombre"),
                "precio": data.get("precio", 0.0)
            })
        return menus
    except Exception as e:
        print("Error al obtener menús desde Firebase:", e)
        return []

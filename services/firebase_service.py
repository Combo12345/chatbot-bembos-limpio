import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-adminsdk.json")
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

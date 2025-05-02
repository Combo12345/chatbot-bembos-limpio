
import joblib
import os

modelo_path = "model/modelo_intencion.pkl"
vector_path = "model/vectorizador.pkl"

if os.path.exists(modelo_path) and os.path.exists(vector_path):
    modelo = joblib.load(modelo_path)
    vectorizador = joblib.load(vector_path)
else:
    modelo = None
    vectorizador = None

def predecir_intencion(texto):
    if modelo is None or vectorizador is None:
        return None
    X = vectorizador.transform([texto])
    return modelo.predict(X)[0]

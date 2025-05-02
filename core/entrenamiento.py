
import os
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dataset de ejemplo (puedes reemplazarlo por datos reales)
datos = {
    'texto': [
        'quiero pedir el combo clásico',
        'muéstrame los combos disponibles',
        'deseo ver promociones',
        'quiero cambiar mi pedido',
        'hola, buenos días',
        'cuál es el horario de atención'
    ],
    'intencion': [
        'hacer_pedido',
        'mostrar_combos',
        'mostrar_promociones',
        'modificar_pedido',
        'saludo',
        'consultar_horario'
    ]
}

df = pd.DataFrame(datos)

# Vectorización de texto
vectorizador = TfidfVectorizer()
X = vectorizador.fit_transform(df['texto'])
y = df['intencion']

# Entrenamiento
modelo = MultinomialNB()
modelo.fit(X, y)

# Guardar modelo y vectorizador
os.makedirs("model", exist_ok=True)
joblib.dump(modelo, "model/modelo_intencion.pkl")
joblib.dump(vectorizador, "model/vectorizador.pkl")

print("✅ Modelo entrenado y guardado correctamente.")

from services.gemini_service import responder_con_gemini, calcular_delivery_con_ia
from services.firebase_service import obtener_menus
from services.twilio_service import enviar_pdf_catalogo
import re

def responder(mensaje):
    mensaje = mensaje.lower()

    # Saludo inteligente
    if any(frase in mensaje for frase in ["hola", "buenas", "buenos días", "buenas tardes", "hey"]):
        return "👋 ¡Hola! Bienvenido a Bembos. ¿Deseas ver nuestros menús o hacer un pedido?"

    # Intención: mostrar menús
    if any(frase in mensaje for frase in ["menú", "menu", "combos", "lo que venden", "quiero ver", "mostrar", "catálogo", "ver opciones"]):
        try:
            menus = obtener_menus()
            if menus and isinstance(menus, list) and len(menus) > 0:
                respuesta = "🍔 Estos son nuestros combos disponibles:\n"
                for item in menus:
                    nombre = item.get("nombre", "Combo sin nombre")
                    precio = item.get("precio", "Precio no disponible")
                    respuesta += f"• {nombre} - S/ {precio}\n"
                respuesta += "\n¿Deseas que te envíe también el catálogo en PDF?"
                return respuesta
            else:
                enviar_pdf_catalogo()
                return "❗ No encontré los menús en Firebase, pero te estoy enviando el catálogo en PDF. 📄"
        except Exception as e:
            print(f"[ERROR] Menús no disponibles: {e}")
            enviar_pdf_catalogo()
            return "⚠️ Hubo un error al obtener los menús. Te estoy enviando el catálogo en PDF. 📄"

    # Intención: delivery
    if "delivery" in mensaje:
        match = re.search(r"delivery (?:a |en )?(\w+(?: \w+)*)", mensaje)
        if match:
            distrito = match.group(1)
            precio = calcular_delivery_con_ia(distrito)
            if precio:
                return f"🚚 El delivery a *{distrito.title()}* cuesta aproximadamente {precio}. ¿Deseas confirmar tu pedido?"
            else:
                return "❌ No pude calcular el costo del delivery por ahora. Intenta nuevamente en unos minutos."
        return "📍 ¿A qué distrito deseas el delivery?"

    # Intención: reserva
    match = re.search(r"(?:reservar|comer).*a las (\d{1,2})", mensaje)
    if match:
        hora = match.group(1)
        return f"📅 ¡Listo! Tu reserva ha sido generada para las {hora}:00 hrs. ¿Para cuántas personas será?"

    # Fallback → IA Gemini
    ia_respuesta = responder_con_gemini(mensaje)
    if ia_respuesta:
        return f"{ia_respuesta} 🤖"

    return "❌ Lo siento, aún no estoy entrenado para responder eso."

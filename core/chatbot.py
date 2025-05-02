from services.gemini_service import responder_con_gemini, calcular_delivery_con_ia
from services.firebase_service import obtener_menus
from services.twilio_service import enviar_pdf_catalogo
import re

def responder(mensaje):
    mensaje = mensaje.lower()

    # Saludo inteligente
    if mensaje in ["hola", "buenas", "buenos días", "hey"]:
        return "👋 ¡Hola! Bienvenido a Bembos. ¿Deseas ver nuestros menús o hacer un pedido?"

    # Detectar intención de menú (flexible)
    if "menú" in mensaje or "menu" in mensaje or "combos" in mensaje or "lo que venden" in mensaje or "quiero ver" in mensaje:
        try:
            menus = obtener_menus()
            if menus and isinstance(menus, list):
                respuesta = "🍔 Aquí tienes nuestros combos:\n"
                for item in menus:
                    nombre = item.get("nombre", "Combo sin nombre")
                    precio = item.get("precio", "Precio no disponible")
                    respuesta += f"• {nombre} - S/ {precio}\n"
                respuesta += "\n¿Deseas que te envíe también el catálogo en PDF?"
                return respuesta
            else:
                enviar_pdf_catalogo()
                return "No encontré los menús en Firebase, te estoy enviando el catálogo en PDF 📄."
        except Exception as e:
            print(f"[ERROR] No se pudieron obtener los menús: {e}")
            enviar_pdf_catalogo()
            return "📄 Te estoy enviando el catálogo en PDF por si acaso hubo un error al cargar los menús."

    # Detectar intención de delivery
    if "delivery" in mensaje:
        match = re.search(r"delivery (?:a |en )?(\w+(?: \w+)*)", mensaje)
        if match:
            distrito = match.group(1)
            precio = calcular_delivery_con_ia(distrito)
            if precio:
                return f"📦 El delivery a {distrito.title()} cuesta aproximadamente {precio}. ¿Deseas confirmar tu pedido?"
            return "No pude calcular el costo del delivery en este momento. 🤖"
        return "¿A qué distrito deseas el delivery? 😊"

    # Detectar intención de reserva
    match = re.search(r"reservar|comer.*a las (\d{1,2})", mensaje)
    if match:
        hora = match.group(1)
        return f"👌 Se ha generado tu reserva para las {hora}:00 hrs en nuestra tienda. ¿Para cuántas personas será?"

    # Fallback → usar IA de Gemini
    ia_respuesta = responder_con_gemini(mensaje)
    if ia_respuesta:
        return f"{ia_respuesta} 🤖 (respuesta generada por IA)"

    return "❌ Lo siento, aún no estoy entrenado para responder eso."
from services.gemini_service import responder_con_gemini

mensaje = input("Cliente: ")

if "catálogo" in mensaje.lower() or "menú" in mensaje.lower():
    prompt = (
        "El cliente está solicitando el menú o catálogo de productos de Bembos. "
        "Responde de forma profesional y amigable. "
        "Adjunta este enlace: https://www.bembos.com.pe/menu "
        "Y menciona que puede encontrar todas las opciones ahí. "
        "No inventes combos. Si deseas puedes invitarlo a preguntar por promociones."
    )
    respuesta = responder_con_gemini(prompt)
else:
    respuesta = responder_con_gemini(mensaje)

print("\n🤖 BembosBot responde:\n")
print(respuesta)

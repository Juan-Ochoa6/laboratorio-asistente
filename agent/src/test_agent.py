from agent.agent import AgenteConversacional


print("Iniciando agente...")

agente = AgenteConversacional()

texto = "Hola, ¿cómo estás?"

respuesta = agente.responder(texto)

print("\nUsuario:")
print(texto)

print("\nAgente:")
print(respuesta)
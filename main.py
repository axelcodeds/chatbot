from ollama import Client

client = Client()
SYSTEM_PROMPT = (
    "Eres un asistente conversacional. Responde de forma corta, natural y amistosa, "
    "como si chatearas por mensajería. No des respuestas largas. Si puedes, responde "
    "en 1 o 2 frases."
)
messages = [{"role": "system", "content": SYSTEM_PROMPT}]

while True:
    prompt = input("Escribe tu pregunta: ")
    if prompt == "x":
        break

    messages.append({"role": "user", "content": prompt})

    response = client.chat(
        model="llama3.2:latest",
        messages=messages,
    )

    assistant_reply = response.message.content or ""
    print(assistant_reply)

    messages.append({"role": "assistant", "content": assistant_reply})

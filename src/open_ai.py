import openai

# Configuración de la API de OpenAI
openai.api_key = "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"

def chat_with_gpt(user_query):
    try:
        # Formato de mensajes para el cliente de chat
        messages = [{"role": "user", "content": "You: " + user_query}]

        # Parámetros de la solicitud
        params = {
            "model": "gpt-3.5-turbo-0125",
            "messages": messages,
            "temperature": 1,
            "max_tokens": 150,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }

        # Solicitud al API de ChatGPT
        response = openai.ChatCompletion.create(**params)

        # Impresión de la respuesta obtenida
        print("chatGPT: " + response.choices[0].message.content)
    except Exception as e:
        print("Ocurrió un error al comunicarse con el modelo de ChatGPT:", str(e))

# Función principal del programa
def main():
    try:
        while True:
            # Solicitar entrada al usuario
            try:
                user_query = input("Ingrese su consulta (o 'exit' para salir): ")
            except KeyboardInterrupt:
                print("\nOperación interrumpida por el usuario.")
                break

            # Salir del bucle si el usuario ingresa 'exit'
            if user_query.lower() == "exit":
                break

            # Verificar si la consulta tiene texto
            if user_query.strip():
                print("Consulta del usuario:", user_query)
                # Llamar a la función para chatear con GPT
                chat_with_gpt(user_query)
            else:
                print("La consulta está vacía. Por favor, ingrese una consulta válida.")
    except Exception as e:
        print("Ocurrió un error durante la ejecución del programa:", str(e))

if __name__ == "__main__":
    main()

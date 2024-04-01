import sys
import openai

# Configuración de la API de OpenAI
openai.api_key = "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"

# Buffer para almacenar consultas no nulas
query_buffer = []

def chat_with_gpt():
    try:
        # Obtener la última consulta del buffer
        last_query = query_buffer[-1]

        # Formato de mensajes para el cliente de chat
        messages = [{"role": "user", "content": "You: " + last_query}]

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

        # Agregar la respuesta al buffer para ser reenviada en las próximas consultas
        query_buffer.append(response.choices[0].message.content)

        # Impresión de la respuesta obtenida
        print("chatGPT: " + response.choices[0].message.content)
    except Exception as e:
        print("Ocurrió un error al comunicarse con el modelo de ChatGPT:", str(e))

# Función principal del programa
def main():
    convers_mode = False

    # Verificar si se proporciona el argumento --convers
    if "--convers" in sys.argv:
        convers_mode = True

    if convers_mode:
        print("Modo de conversación activado. Puedes chatear con ChatGPT libremente.")
    else:
        print("Modo de conversación estándar. Ingrese su consulta.")

    try:
        while True:
            # Solicitar entrada al usuario
            try:
                user_query = input("You: ") if convers_mode else input("Ingrese su consulta (o 'exit' para salir): ")
            except KeyboardInterrupt:
                print("\nOperación interrumpida por el usuario.")
                break

            # Salir del bucle si el usuario ingresa 'exit'
            if user_query.lower() == "exit":
                break

            # Verificar si la consulta tiene texto
            if user_query.strip():
                print("Consulta del usuario:", user_query)
                # Agregar la consulta al buffer
                query_buffer.append(user_query)
                # Llamar a la función para chatear con GPT
                chat_with_gpt()
            else:
                print("La consulta está vacía. Por favor, ingrese una consulta válida.")
    except Exception as e:
        print("Ocurrió un error durante la ejecución del programa:", str(e))

if __name__ == "__main__":
    main()

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_response(prompt_text):
    response = client.chat.completions.create(
        # model="gpt-3.5-turbo-0125",
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_text},
        ],
        max_tokens=150,  # Limits how long the response can be
        temperature=0.7,  # A value between 0-1 that controls randomness
    )  # Ensure this line ends with the closing parenthesis
    texto_retorno = response.choices[0].message.content.strip()
    return texto_retorno


if __name__ == "__main__":
    prompt_text = "Qual é a capital da França."
    resposta = generate_response(prompt_text)
    print(resposta)

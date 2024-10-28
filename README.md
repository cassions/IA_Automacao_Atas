# Automação de atas com IA

Explorando automação de atas com IA. 

Recebe um arquivo mp4 e gera um resumo, seguindo os seguintes passos:

- Recebe arquivo MP4 via interface web no Streamlit
- Converte o arquivo MP4 em MP3 (apenas audio)
- Transcreve o audio MP3 com AssemblyAI
- Resume o texto transcrito a partir do MP3 com OpenAI
- Mostra resumo e transcrição

Solução publicado no Streamlit, pode ser acessada pelo link:

https://resumevideo.streamlit.app/


## Requisitos

- Crédito na conta OpenAI
    - A utilização da API da OpenAI pode gerar custos conforme a quantidade de requisições realizadas para transcrição e tradução de áudio. Certifique-se de verificar a [política de preços da OpenAI](https://openai.com/pricing) antes de usar o serviço para evitar cobranças inesperadas.
- Crédito na conta AssemblyAI, é possível utilizar crédito inicial de testes
    - https://www.assemblyai.com/pricing
- Conta no Streamlit 
    - https://streamlit.io/
- Para os pacotes verifique arquivo [requirements.txt](requirements.txt)

## Configuração

Criar arquivo .streamlit/secrets.toml contendo:

[openai]
api_key = 'SUA_CHAVE'

[assemblyai]
api_key = 'SUA_CHAVE'

## Sandbox

Pasta sandbox contém os testes e exploração que foram feitos antes de criar o projeto. Caso queria executar os script crie um arquivo .env contendo:

OPENAI_API_KEY = 'SUA_CHAVE'
ASSEMBLYAI_API_KEY = 'SUA_CHAVE'
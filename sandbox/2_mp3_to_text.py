import assemblyai as aai
import os
from dotenv import load_dotenv

load_dotenv()

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
transcriber = aai.Transcriber()

mp3_filename = r"3f504b9fe2c543feadbb731bbb2b83c4.mp3"

config = aai.TranscriptionConfig(
    speaker_labels=True, speakers_expected=2, language_code="pt"
)

transcriber = aai.Transcriber()
transcricao = transcriber.transcribe(mp3_filename, config=config)

for sentenca in transcricao.utterances:
    print(f"Pessoa {sentenca.speaker}: {sentenca.text}")

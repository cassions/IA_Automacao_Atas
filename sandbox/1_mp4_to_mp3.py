from moviepy.editor import *
import uuid


def mp4_to_mp3(mp4_filename, mp3_filename):
    arq_conv = AudioFileClip(mp4_filename)
    arq_conv.write_audiofile(mp3_filename)
    arq_conv.close()


if __name__ == "__main__":
    mp4_filename = "entrevista.mp4"
    mp3_filename = "{nome_arquivo}.mp3".format(nome_arquivo=uuid.uuid4().hex)
    mp4_to_mp3(mp4_filename, mp3_filename)

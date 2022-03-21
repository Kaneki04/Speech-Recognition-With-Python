import moviepy.editor as mp
from tkinter.filedialog import *
from tkinter import *
import speech_recognition as sr
from deep_translator import GoogleTranslator
import time
r = sr.Recognizer()


text = []
translatedTexts = []

videofile = askopenfilename()
video = mp.VideoFileClip(videofile)
audio = video.audio
audio.write_audiofile('video.wav')
audioFIle = sr.AudioFile('video.wav')

entry_lan = input('Source Language: ')
entry_tra = input('Target language: ')


def callback(r, audio):
    print('Text:\n')
    print(r.recognize_google(audio, language=entry_lan))
    print('------------------')
    print('Translation:\n')
    print(GoogleTranslator(source=entry_lan, target=entry_tra).translate(
        r.recognize_google(audio, language=entry_lan)))
    print('------------------')


with audioFIle as source:
    r.adjust_for_ambient_noise(source)
stop_listening = r.listen_in_background(audioFIle, callback)

for i in range(600):
    time.sleep(1)

stop_listening(wait_for_stop=False)

while True:
    time.sleep(0.1)

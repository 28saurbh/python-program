from gtts import gTTS
import os


f = open('text.txt')
x = f.read()
audio = gTTS(text = x, lang = 'en',slow=False)
audio.save("1.wav")
os.system("1.wav")

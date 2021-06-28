import pandas as pd
import speech_recognition as sr

# Read audio file
r = sr.Recognizer()
file_audio = sr.AudioFile('F_0101_10y4m_1.wav')

# Convert audio file to text
with file_audio as source:
   audio_text = r.record(source)

converted_text = r.recognize_google(audio_text)

# Print converted text from the audio file
print(converted_text)
print('Type of converted_text:', converted_text)
# Print audio_text
print(audio_text)
print('Type of audio_text:', type(audio_text))

import speech_recognition as sr

filename = "machine-learning_speech-recognition_16-122828-0002.wav"

r = sr.Recognizer()

with sr.AudioFile(filename) as source:
  # load audio into memory
  audio_data = r.record(source)
  # convert speech to text
  text = r.recognize_google(audio_data)
  print(text)



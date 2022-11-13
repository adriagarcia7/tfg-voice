from vosk import Model, KaldiRecognizer
import pyaudio
# Read the model
model = Model(r'C:\dev\python-vosk\vosk-model-small-en-us-0.15')
recognizer = KaldiRecognizer(model, 16000)

# Recognize from the microphone
cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    #if len(data) == 0:
    #    break

    if recognizer.AcceptWaveform(data):
        print(recognizer.Result())
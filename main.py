import speech_recognition as speech_r
import pyaudio
import wave
import librosa

CHUNK = 1024 
FRT = pyaudio.paInt16 
CHAN = 1 
RT = 44100 
REC_SEC = 5 
OUTPUT = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FRT,channels=CHAN,rate=RT,input=True,frames_per_buffer=CHUNK) 
print("rec")
frames = [] 
for i in range(0, int(RT / CHUNK * REC_SEC)):
    data = stream.read(CHUNK)
    frames.append(data)
print("done")

stream.stop_stream() 
stream.close()
p.terminate()

w = wave.open(OUTPUT, 'wb')
w.setnchannels(CHAN)
w.setsampwidth(p.get_sample_size(FRT))
w.setframerate(RT)
w.writeframes(b''.join(frames))
w.close()

r = speech_r.Recognizer()
sample = speech_r.WavFile('output.wav')
type(sample)

# Create audio data
with sample as source:
    audiodata = r.record(sample)
type(audiodata)

with sample as audio:
    content = r.record(audio)
    r.adjust_for_ambient_noise(audio)

# Extract text
text = r.recognize_google(audio_data=audiodata, language='ru-RU')

print(text)


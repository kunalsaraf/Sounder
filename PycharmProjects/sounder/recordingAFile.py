import sounddevice as sd
from scipy.io import wavfile

fs = 44100  # Sample rate
seconds = 1  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
wavfile.write('output.wav', fs, myrecording)  # Save as WAV file
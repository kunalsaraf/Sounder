from typing import List, Any

import numpy as np
import simpleaudio as sa

def makeMySound(freq,dur):
    frequency = freq  # Our played note will be 440 Hz
    fs = 44100  # 44100 samples per second
    seconds = dur  # Note duration of 3 seconds

    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * 2 * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    print(audio)
    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting
    play_obj.wait_done()
    return audio

values = []

for i in range(500,820,20):
    print(i)
    values.append(makeMySound(i,1))

keys = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
dictio = dict(zip(keys,values))
for k in dictio.keys():
    print(k)
for m in dictio.values():
    print(m)
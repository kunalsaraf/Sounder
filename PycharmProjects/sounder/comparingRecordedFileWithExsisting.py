import numpy as np
from scipy.io import wavfile

values = []
keys = []

for i in range(250,6601,50):
    keys.append(i)
    values.append(wavfile.read('New Audio Files/{}.wav'.format(i))[1])

filetest = wavfile.read('output.wav')[1]

my_dict = dict(zip(keys, values))

result_directSum = []
result_RMS = []

for i in my_dict:
    print(i)
    temp = (my_dict[i] - filetest)
    temp2 = abs(temp).sum()
    print(temp2)
    temp3 = np.sqrt((temp**2).mean())
    print(temp3)
    result_directSum.append((temp2,i))
    result_RMS.append((temp3,i))

result_directSum.sort()
result_RMS.sort()

print('\nMatched using direct with frequency {}'.format(result_directSum[0][1]))
print('\nMatched using rms with frequency {}'.format(result_RMS[0][1]))
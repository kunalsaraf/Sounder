import numpy as np
from scipy.io import wavfile

rate, file0 = wavfile.read('500.wav')
rate, file1 = wavfile.read('520.wav')
rate, file2 = wavfile.read('540.wav')
rate, file3 = wavfile.read('560.wav')
rate, file4 = wavfile.read('580.wav')
rate, file5 = wavfile.read('600.wav')
rate, file6 = wavfile.read('620.wav')
rate, file7 = wavfile.read('640.wav')
rate, file8 = wavfile.read('660.wav')
rate, file9 = wavfile.read('680.wav')
rate, fileA = wavfile.read('700.wav')
rate, fileB = wavfile.read('720.wav')
rate, fileC = wavfile.read('740.wav')
rate, fileD = wavfile.read('760.wav')
rate, fileE = wavfile.read('780.wav')
rate, fileF = wavfile.read('800.wav')
rate, filetest = wavfile.read('output.wav')

keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
values = [file0, file1, file2, file3, file4, file5, file6, file7, file8, file9, fileA, fileB, fileC, fileD, fileE,
          fileF]
frequencies = [500,520,540,560,580,600,620,640,660,680,700,720,740,760,780,800]
my_dict = dict(zip(keys, values))
my_dict2 = dict(zip(keys,frequencies))

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

print('\nMatched using direct with {} having freq {}'.format(result_directSum[0][1],my_dict2[result_directSum[0][1]]))
print('\nMatched using rms with {} having freq {}'.format(result_RMS[0][1],my_dict2[result_RMS[0][1]]))
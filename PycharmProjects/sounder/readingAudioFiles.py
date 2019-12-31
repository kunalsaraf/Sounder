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

keys = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
values = [file0,file1,file2,file3,file4,file5,file6,file7,file8,file9,fileA,fileB,fileC,fileD,fileE,fileF]
my_dict = dict(zip(keys,values))
for k in my_dict.keys():
    print(k)
for m in my_dict.values():
    print(m)
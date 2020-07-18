# import numpy as np
# import mne

# edf = mne.io.read_raw_edf('eegData.edf')
# header = ','.join(edf.ch_names)
# np.savetxt('eegData.csv', edf.get_data().T, delimiter=',', header=header)

import pyedflib
import numpy as np

f = pyedflib.EdfReader("FA96319X.edf copy")
n = f.signals_in_file
signal_labels = f.getSignalLabels()
signal_labels_row = ",".join(signal_labels)
# print(signal_labels_row)

sigbufs = np.zeros((n, f.getNSamples()[0]))
text = signal_labels_row + '\n'
for i in np.arange(n):
    sigbufs[i, :] = f.readSignal(i)
    strsigbufs = [str(k) for k in sigbufs[i, :]]
    if i < n-1:
        text = text + ",".join(strsigbufs) + '\n'
    else:
        text = text + ",".join(strsigbufs)
# print(text)

f = open('trainingData.csv','w')
for line in text:
    f.write(line)
f.close()
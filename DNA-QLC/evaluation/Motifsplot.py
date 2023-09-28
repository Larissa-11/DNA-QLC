

import matplotlib.pyplot as plt
import numpy as np


plt.figure(figsize=(8, 6), dpi=100)
plt.subplot(1, 1, 1)
N = 7
values = (10268, 0, 5052, 3874, 10023, 7115, 0)
# name = ('Church', 'Goldman', 'Grass', 'Blawat', 'Erlich', 'Yin-Yang', 'LC')
index = np.arange(N)
width = 0.5
p2 = plt.bar(index, values, width, color="darkkhaki")
plt.bar_label(p2, label_type='edge',fontsize=14)
plt.xlabel('Different methods', fontsize=16, labelpad=10)
plt.ylabel('Number of undesired motifs', fontsize=16, labelpad=8.5)
plt.title('The case of undesired motifs', fontsize=16, pad=20)
plt.xticks(index, ('Church', 'Goldman', 'Grass', 'Blawat', 'Erlich', 'Yin-Yang', 'This work'))
plt.yticks(np.arange(0, 11000, 3000))
plt.savefig('Motifis.png',dpi=100)
plt.close()











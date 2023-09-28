

import matplotlib.pyplot as plt
import numpy as np


plt.figure(figsize=(8, 6), dpi=100)
N = 5
values = [4136,  3120, 4136, 3120, 2757]
# name = ('Church', 'Goldman', 'Grass', 'Blawat', 'Erlich', 'Yin-Yang', 'LC')
index = np.arange(N)
width =0.5
p2 = plt.bar(index, values, width, color=['bisque','khaki','lightsteelblue','paleturquoise','thistle'])
plt.xlabel('Encoding scheme', fontsize=16, labelpad=10)
plt.ylabel('Estimated costs', fontsize=16, labelpad=8.5)
plt.xticks(index, ('Church', 'Grass', 'DNA Fountain', 'Yin-Yang', 'DNA-QES'))
plt.yticks(np.arange(0, 5000, 1000))
for p2 in p2:
    height = p2.get_height()
    plt.text(p2.get_x()+p2.get_width()/2,height+0.3,str(height),ha='center')
plt.savefig('Cost.png',dpi=100)
plt.show()
plt.close()











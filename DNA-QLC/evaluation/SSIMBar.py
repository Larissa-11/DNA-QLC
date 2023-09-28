
import numpy as np
import matplotlib.pyplot as plt

Grass = (0.771, 0.42, 0.269, 0.188, 0.211, 0.147)
Grass_errbar = (0.060, 0.062, 0.030, 0.019, 0.024, 0.013)

YinYang = (1, 0.556, 0.341, 0.212, 0.187, 0.17)
YinYang_errbar = (0, 0.077, 0.047, 0.043, 0.024, 0.021)

LC = (0.917, 0.917, 0.917, 0.917, 0.917, 0.917)
LC_errbar = (0, 0, 0, 0, 0, 0)
index = np.arange(len(Grass))
width = 0.2
cities = ('0.1%', '0.2%', '0.5%', '1%', '1.5%', '2%')

bar_Grass = plt.bar(index, Grass, width, color='none', alpha=0.8 ,edgecolor='cornflowerblue'
                    ,linestyle='-',linewidth=1,hatch='*', yerr=Grass_errbar, error_kw = {'ecolor' : 'dimgrey', 'capsize':5,'elinewidth':1.5})
bar_YinYang = plt.bar(index + width, YinYang, width, color='none', alpha=0.8, edgecolor=['darkorange'],
                      linestyle='-', linewidth=1,hatch='////', yerr=YinYang_errbar, error_kw={'ecolor': 'dimgrey', 'capsize':5,'elinewidth':1.5})
bar_LC = plt.bar(index + width + width, LC, width, color='none', alpha=0.8, edgecolor='dimgrey',
                 linestyle='-',linewidth=1, hatch='\\\\\\\\', yerr=LC_errbar, error_kw={'ecolor': 'dimgrey', 'capsize':5,'elinewidth':1.5})

# plt.xlabel('Error rate', fontproperties='Simhei', fontsize=16)
# plt.ylabel('SSIM', fontproperties='Simhei', fontsize=16)
plt.xlabel('Error rate', fontsize=14)
plt.ylabel('SSIM', fontsize=14)
# plt.xticks(index + width, cities, fontproperties='Simhei', fontsize=12)
plt.xticks(index + width, cities, fontsize=12)
# plt.legend([bar_Grass, bar_YinYang, bar_LC], ['Grass', 'YinYang', 'DNA-QLD'], prop='Simhei', loc='upper center',  ncol=3)
plt.legend([bar_Grass, bar_YinYang, bar_LC], ['Grass', 'Yin-Yang', 'DNA-QLC'], loc='upper center',  ncol=3)
# plt.show()
plt.savefig('SSIMBar.png',dpi=100)
plt.close()

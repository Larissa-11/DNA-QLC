import matplotlib.pyplot as plt


x_axis_data = ['Church et al', 'Grass et al.', 'DNA Fountain', 'YYC', 'DNA-QLD']
y_axis_data = [4136,  3120, 4136, 3120, 2757]
for x, y in zip(x_axis_data, y_axis_data):
    plt.text(x, y+0.3, '%.00f' % y, ha='center', va='bottom', fontsize=10)
plt.plot(x_axis_data, y_axis_data, 'b*--', alpha=0.5, linewidth=2)



plt.xlabel('Coding schemes')
plt.ylabel('Estimated costs ($)')

plt.savefig('Cost evaluation.png',dpi=100)
plt.show()

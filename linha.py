import matplotlib.pyplot as plt

x = [2013,2014,2015,2016,2017,2018,2019]
y = [4.2,14.3,17.4,17.5,20.2,18,14.4]

plt.plot(x, y, c='red', ls='-.', lw='1', marker='o')
plt.xlabel('Ano da venda', fontsize=17)
plt.ylabel('Número em milhões', fontsize=16)
plt.show()
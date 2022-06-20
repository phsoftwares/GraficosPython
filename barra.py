import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

jogos = (' GTA V ', '   GOD WAR     ', ' UNCHARTED 4 ', ' SPIDERMAN ', '   THE WITCHER 3')
indice = np.arange(len(jogos))
vendas = [24,19.5,16,13.2,10.8]

plt.bar(indice, vendas, color='red')
plt.bar(indice,vendas)
plt.xticks(indice, jogos)
plt.ylabel('Número em milhões')
plt.title('Top 5 jogos mais vendidos para PS4')

plt.show()
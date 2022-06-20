import matplotlib.pyplot as plt

rotulos = ['Corrida','FPS','Simulação','Aventura','RolePlay','Ação']
valores = [2,4,2,10,11,19]

plt.figure(figsize=(8,8))
plt.pie(x=valores, labels=rotulos, autopct='%1.1f%%', startangle=90, shadow=True)
plt.show()
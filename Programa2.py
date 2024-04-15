# Numpy no tiene módulos

import numpy as np

# Matplotlib tiene muchos módulos
# Al tener tantos módulos lo más eficiente sería
#  importar sólo los módulos que se van a usar

import matplotlib.pyplot as plt

# Crear un ndarray de 1 dimensión con 100 elementos desde 0 a 2pi

x=np.linspace(0,2*np.pi,100)
y=np.sin(x)

# Crear un gráfico usando matplotlib
# 1. Difinir las dimensiones

plt.figure(figsize=(8,4))
plt.title("Mi primer gráfico cientifico en Programación")
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("seno(x)")
plt.grid(True)
plt.show()
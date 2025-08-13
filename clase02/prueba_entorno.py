import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)

print("La suma de las primeras diez muestras es: ", np.sum(y[:10]))

plt.plot(x, y)
plt.title("Seno de prueba")
plt.xlabel("x [rad]")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()


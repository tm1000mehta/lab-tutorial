from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi, 1000)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, np.zeros(len(x)), linestyle="--", color='0.8')
ax.plot(x, y)

plt.show()
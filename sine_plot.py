from matplotlib import pyplot as plt
import numpy as np

# Create data for sine wave
x = np.linspace(0,2*np.pi, 1000)
y = np.sin(x)

#Draw initial figure and axis
fig, ax = plt.subplots()

#Plot sine wave
ax.plot(x, y)

#Plot reference line
ax.plot(x, np.zeros(len(x)), linestyle="--", color='0.8')

#Show plot
plt.show()
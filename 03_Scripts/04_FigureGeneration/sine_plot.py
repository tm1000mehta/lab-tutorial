from matplotlib import pyplot as plt
import numpy as np
import os

## Path handling to find the parent directory based on location of this file
scriptpath = os.path.realpath(__file__)
parentDirInd = scriptpath.find("03_Scripts")
parentdir = scriptpath[0:parentDirInd]
os.chdir(parentdir)

# Create data for sine wave
x = np.linspace(0,2*np.pi, 1000)
y = np.sin(x)

#Draw initial figure and axis
fig, ax = plt.subplots()

#Plot reference line
ax.plot(x, np.zeros(len(x)), linestyle="--", color='0.8')

#Plot sine wave
ax.plot(x, y)

#Show plot
plt.savefig(os.path.realpath("04_Outputs/01_Figures/sineplot.png"))
plt.show(fig)
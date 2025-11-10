#---------------------------------------------------------
# Python script to make the 2D map multinode latency 
# carenza.cronshaw@york.ac.uk
#---------------------------------------------------------

# Importing modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy.interpolate import griddata

# Pink and Purple Colour pallete (matching purple.style)
colors = [
    (0/9, '#FFFFFF'),
    (1/9, '#FEFBD0'),
    (2/9, '#F1D6B2'),
    (3/9, '#DE9A97'),
    (4/9, '#C76685'),
    (5/9, '#95448E'),
    (6/9, '#5C2D8F'),
    (7/9, '#3C1E70'),
    (8/9, '#1E0D3B'),
    (9/9, '#000000')
]
palette = LinearSegmentedColormap.from_list("custom_palette", colors)

# Loading data from bandwidth file
data = np.loadtxt("bandwidth.txt")
x, y, z = data[:, 0], data[:, 1], data[:, 2]

# Creating the colour grid 
xi = np.linspace(np.min(x), np.max(x), 300)
yi = np.linspace(np.min(y), np.max(y), 300)
Xi, Yi = np.meshgrid(xi, yi)
Zi = griddata((x, y), z, (Xi, Yi), method='cubic')

# Plotting the colour map 
plt.figure(figsize=(8, 6))
mesh = plt.pcolormesh(Xi, Yi, Zi, cmap=palette, shading='auto')

# Creating colourbar
cbar = plt.colorbar(mesh)
cbar.set_label("Bandwidth (Gb/s)", fontsize=20)
cbar.ax.tick_params(labelsize=14) 

# Setting the axis label names and fontsize 
plt.xlabel("Core Number", fontsize=20)
plt.ylabel("Core Number", fontsize=20)

# Sorting out tics and the size of the labels 
plt.xticks(np.arange(0, np.max(x), 20)); plt.yticks(np.arange(0, np.max(y), 20))
plt.tick_params(labelsize=16)

# Plot graph
plt.tight_layout()
plt.show()

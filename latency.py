#---------------------------------------------------------
# Python script to make the 2D map multinode latency 
# carenza.cronshaw@york.ac.uk
#---------------------------------------------------------

#importing modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy.interpolate import griddata

# Pink and Purple Colour pallete
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

# Loading data from latency file
data = np.loadtxt("latency.txt")
x, y, z = data[:, 0], data[:, 1], data[:, 2]    #saving the x/y/z data

# creating grid
xi = np.linspace(np.min(x), np.max(x), 300)
yi = np.linspace(np.min(y), np.max(y), 300)
Xi, Yi = np.meshgrid(xi, yi)
Zi = griddata((x, y), z, (Xi, Yi), method='cubic')

# plotting the colour map 
plt.figure(figsize=(8, 6))  #figure size
mesh = plt.pcolormesh(Xi, Yi, Zi, cmap=palette, shading='auto')

# adding the colour bar to the left
cbar = plt.colorbar(mesh)
cbar.set_label("Latency (ns)", fontsize=20) #label size increased so can be seen when figure size decreased
cbar.ax.tick_params(labelsize=14)  #size of numbers increased

# Setting the axis label names and fontsize 
plt.xlabel("Core Number", fontsize=20)
plt.ylabel("Core Number", fontsize=20)

#sorting out tics and the size of the labels 
plt.xticks(np.arange(0, 257, 20)); plt.yticks(np.arange(0, 257, 20))
plt.tick_params(labelsize=16)

#plot graph
plt.tight_layout()
plt.show()



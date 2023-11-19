import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


galaxies = 1000


x = np.random.normal(10, 100, galaxies)
y = np.random.normal(10, 100, galaxies)
z = np.random.normal(10, 100, galaxies)

specific_colors = ['#0A0068', '#26007B', '#42008D', '#5E00A0', '#7A00B2']
colors = np.random.choice(specific_colors, size=galaxies)

specific_luminosities = np.array([0.1, 0.3, 0.5, 0.7, 0.9])
luminosities = np.random.choice(specific_luminosities, size=galaxies)

sizes = np.random.rand(galaxies)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=np.random.rand(galaxies, 3), marker='o', edgecolors = 'k', s=luminosities * 100)


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('Galaxies in the Universe')

plt.show()

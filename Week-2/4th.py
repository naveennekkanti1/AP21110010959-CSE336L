import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50) * 1000
fig, ax = plt.subplots()
scatter = ax.scatter(x, y, s=z, alpha=0.5)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title('Scatter Plot with Varying Marker Size')
cbar = plt.colorbar(scatter)
cbar.set_label('Bubble Size')
plt.show()

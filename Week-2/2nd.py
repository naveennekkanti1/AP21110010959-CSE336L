import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='Sin', color='blue', linewidth=2)
plt.plot(x, y2, label='Cos', color='red', linewidth=3, linestyle='--')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Multiple Lines Plot')
plt.legend()
plt.show()
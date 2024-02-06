import matplotlib.pyplot as plt
x_positions = [1, 2, 3, 4, 5]
y_positions = [5, 7, 3, 9, 6]
quantities = ['A', 'B', 'C', 'D', 'E']
plt.scatter(x_positions, y_positions, color='blue', s=100)
for i, txt in enumerate(quantities):
    plt.annotate(txt, (x_positions[i], y_positions[i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Quantities with X and Y Positions')
plt.grid(True)
plt.show()

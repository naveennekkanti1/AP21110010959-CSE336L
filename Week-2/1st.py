import matplotlib.pyplot as plt

def draw_line(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Line Plot')
    plt.show()

# Example usage
x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 5, 7, 11]
draw_line(x_values, y_values)
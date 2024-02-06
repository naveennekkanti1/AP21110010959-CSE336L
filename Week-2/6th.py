import matplotlib.pyplot as plt
products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [350, 420, 300, 500]
plt.bar(products, sales, color='skyblue')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales Comparison')
plt.show()

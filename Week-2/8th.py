import matplotlib.pyplot as plt
categories = ['Housing', 'Food', 'Transportation', 'Entertainment', 'Utilities']
expenses = [1000, 800, 500, 300, 400]
plt.pie(expenses, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Expense Distribution')
plt.axis('equal')
plt.show()

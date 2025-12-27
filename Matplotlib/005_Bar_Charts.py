# Bar Chart = compare categories of data by representing each category with a bar

import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweets"])
values = np.array([4, 3, 2, 5, 3, 1])

plt.bar(categories, values, color="skyblue")
# plt.barh(categories, values, color="skyblue") # for horizontal bar chart

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()
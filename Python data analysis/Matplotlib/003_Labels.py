import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])
y3 = np.array([13, 15, 20, 30])

# Header
plt.title("Class size", fontsize=25,
                              family="Arial",
                              fontweight="bold",
                              color="#2d4cfc")

# X-aix topic
plt.xlabel("Year", fontsize=20,
                         family="Arial",
                         fontweight="bold",
                         color="#2dbefc")

plt.ylabel("Students", fontsize=20,
                             family="Arial",
                             fontweight="bold",
                             color="#2dbefc")
# params = parameters
plt.tick_params(axis="both",
                which="major",
                labelsize=10,)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xticks(x) # Show only specific value we uses

plt.subplots_adjust(bottom=0.175, left=0.14) # adjust the size of the whole presentations

plt.show()
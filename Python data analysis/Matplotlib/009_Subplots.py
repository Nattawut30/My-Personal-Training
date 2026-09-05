# Figure = The Entire Canvas
# Ax = A single plot (subplot)

import matplotlib.pyplot as plt
import numpy as np

# axes is technically a NumPy array

x = np.array([1, 2, 3, 4, 5])

figure, axes = plt.subplots(2, 2)

axes[0, 0].plot(x, x*2, color="red")
axes[0, 0].set_title("x*2")

axes[0, 1].bar(x, x**2, color="blue")
axes[0, 1].set_title("x**2")

axes[1, 0].plot(x, x**3, color="green")
axes[1, 0].set_title("x**3")

axes[1, 1].plot(x, x**4, color="orange")
axes[1, 1].set_title("x**4")

plt.show()
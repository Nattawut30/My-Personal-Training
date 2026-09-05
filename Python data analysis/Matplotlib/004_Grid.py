# grid() = Helps make plots easier to read by adding reference lines.

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

# plt.grid(axis="x")
plt.grid(axis="y",
         linewidth=2,
         color="lightgray",
         linestyle="dashed")

plt.plot(x, y)
plt.show()
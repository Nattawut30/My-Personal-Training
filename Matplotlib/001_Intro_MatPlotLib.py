# Matplotlib = customize data into a chart

# Terminal = Pip Install Matplotlib
# Upgrade = pip install --upgrade pip on Terminal

import matplotlib.pyplot as plt
import numpy as np

#print(matplotlib.__version__) # Check version

# Pyplot provides a user-friendly interface for plotting

# We need a set of X-axis and Y-xis for graph

x = np.array([2023, 2024, 2025, 2026])
y = np.array([15, 25, 30, 20])

plt.plot(x, y)
plt.show() # show the separated window
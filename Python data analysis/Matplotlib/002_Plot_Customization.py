import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])
y3 = np.array([13, 15, 20, 29])

# Uses the dictionary to help add the style in y2
line_style = dict(marker=".", # add marker the dot
                     markersize=20, # change marker size, ms=
                     markerfacecolor="#1cd3fc", # add marker color, mfc=
                     markeredgecolor="#1cd3fc", # mec=
                     linestyle="solid", # Change line style, "none" for no line at all
                     linewidth=4,) # Adjust the width of the line

                      # change the line color
                      # Add "color" in the args
plt.plot(x, y1, color="#1c5bfc", **line_style)
plt.plot(x, y2, color="#1cfc45", **line_style) # Calls the line_style dic()
plt.plot(x, y3, color="#fc1c1c", **line_style) # you can add args directly on the plot

# plt.plot(x, x, marker="o") # Add marker the circle
# plt.plot(x, x, marker="v") # Add marker the point
# plt.plot(x, x, marker="*") # add marker the star

plt.show()

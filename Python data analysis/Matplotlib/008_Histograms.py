# Histogram = A visual representation of the distribution of quantitative data.
#             They group values into bins (intervals)
#             and counts how many fall in each range.

import matplotlib.pyplot as plt
import numpy as np

# loc = location of the center, the median of data
# scale = how far away are the scores going to deviate from the center?
# size = how many sample

scores = np.random.normal(loc=80, scale=10, size=100)

scores = np.clip(scores, a_min=0, a_max=100)

plt.hist(scores, bins=10,
                 color="lightgreen",
                 edgecolor="black")

plt.title("Exam Scores")
plt.xlabel("Scores")
plt.ylabel("Number of Students")

plt.show()
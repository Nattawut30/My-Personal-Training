import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data01.csv")

type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values, color="#03dffc",
                                              edgecolor="black")

plt.title("Number of Pokemon Type")
plt.xlabel("Count")
plt.ylabel("Type")

plt.tight_layout()
plt.show()
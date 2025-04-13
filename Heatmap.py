import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("real_immigration_correlation_data_fixed.csv")

print(df.describe())

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap: Immigration vs Economic Indicators")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(df["Month"], df["Immigrants"], marker="o")
plt.title("Monthly Immigration to Canada (2015–2025)")
plt.xlabel("Month")
plt.ylabel("Number of Immigrants")
plt.grid(True)
plt.tight_layout()
plt.show()

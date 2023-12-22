import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {'Values': [1, 2, 3, 4, 5, 20]}

df = pd.DataFrame(data)

# Boxplot for visual inspection
df.boxplot(column='Values')
plt.show()
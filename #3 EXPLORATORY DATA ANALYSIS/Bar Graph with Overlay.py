import pandas as pd
import matplotlib.pyplot as plt

# Sample data for a bar graph with overlay
data = pd.DataFrame({'Category': ['A', 'B', 'C', 'A', 'B', 'C'],
                     'Value1': [10, 15, 8, 12, 20, 18],
                     'Value2': [5, 8, 15, 10, 12, 25]})

# Construct a bar graph with overlay
data.plot(kind='bar', x='Category', y=['Value1', 'Value2'], color=['blue', 'red'],
          title='Bar Graph with Overlay', xlabel='Categories', ylabel='Values')
plt.show()
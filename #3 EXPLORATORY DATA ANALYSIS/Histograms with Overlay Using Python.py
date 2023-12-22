

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data for histograms with overlay
data = pd.DataFrame({'Value1': np.random.normal(10, 2, 100),
                     'Value2': np.random.normal(15, 3, 100)})

# Construct histograms with overlay
plt.hist(data['Value1'], bins=20, color='blue', alpha=0.7, label='Value1')
plt.hist(data['Value2'], bins=20, color='red', alpha=0.7, label='Value2')
plt.title('Histogram with Overlay')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.legend()
plt.show()

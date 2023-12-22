
import pandas as pd
import numpy as np

# Sample data for binning based on predictive value
data = pd.DataFrame({'Value': np.random.normal(10, 2, 100)})

# Define bin edges
bin_edges = [-np.inf, 8, 12, np.inf]

# Perform binning
data['Bin'] = pd.cut(data['Value'], bins=bin_edges, labels=['Low', 'Medium', 'High'])
print(data)

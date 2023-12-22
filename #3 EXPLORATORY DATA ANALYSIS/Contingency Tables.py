import pandas as pd

# Sample data for constructing a contingency table
data = pd.DataFrame({'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
                     'Outcome': ['Yes', 'No', 'No', 'Yes', 'Yes']})

# Construct a contingency table
contingency_table = pd.crosstab(data['Gender'], data['Outcome'])
print(contingency_table)
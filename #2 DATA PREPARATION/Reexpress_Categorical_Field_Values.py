import pandas as pd

# Sample DataFrame with a categorical column
data = {'Category': ['A', 'B', 'A', 'C', 'B']}
df = pd.DataFrame(data)

# Mapping to reexpress values
mapping = {'A': 'High', 'B': 'Medium', 'C': 'Low'}
df['Category'] = df['Category'].replace(mapping)

# Display the DataFrame
print(df)
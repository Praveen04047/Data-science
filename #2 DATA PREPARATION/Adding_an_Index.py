import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['City1', 'City2', 'City3']}

df = pd.DataFrame(data)

# Adding an index field
df = df.reset_index()

# Display the DataFrame
print(df)
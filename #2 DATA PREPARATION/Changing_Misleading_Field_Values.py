import pandas as pd

# Sample DataFrame with misleading values
data = {'Name': ['Alice', 'Bob', 'Unknown', 'Charlie'],
        'Age': [25, 30, -1, 35],
        'City': ['City1', 'City2', 'City3', 'Unknown']}

df = pd.DataFrame(data)

# Replace misleading values
df['Age'] = df['Age'].replace(-1, 0)
df['City'] = df['City'].replace('Unknown', 'NA')

# Display the DataFrame
print(df)

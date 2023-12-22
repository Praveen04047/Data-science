import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['City1', 'City2', 'City3']}

df = pd.DataFrame(data)

# Accessing columns (variables)
name_column = df['Name']
print(name_column)
age_column = df['Age']
print(age_column)

# Accessing rows (records)
first_row = df.iloc[0]  # Using integer location
print(first_row)
second_row = df.loc[1]  # Using label-based location
print(second_row)

# Accessing specific cell value
cell_value = df.at[1, 'Age']
print(cell_value)
# Filtering data based on conditions
filtered_data = df[df['Age'] > 30]
print(filtered_data)
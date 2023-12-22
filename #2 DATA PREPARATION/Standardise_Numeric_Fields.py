from sklearn.preprocessing import StandardScaler
import pandas as pd

# Sample DataFrame with numeric fields
data = {'Height': [160, 170, 155, 180, 175],
        'Weight': [60, 70, 55, 80, 75]}

df = pd.DataFrame(data)

# Standardizing numeric fields
scaler = StandardScaler()
df[['Height', 'Weight']] = scaler.fit_transform(df[['Height', 'Weight']])

# Display the standardized DataFrame
print(df)

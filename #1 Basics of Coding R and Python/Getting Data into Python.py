import pandas as pd
url = 'https://raw.githubusercontent.com/aditya-agr/Data-Science/main/Automobile.csv'
data = pd.read_csv(url)
print(data.head());
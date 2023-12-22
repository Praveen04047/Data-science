
import pandas as pd
from sklearn.model_selection import train_test_split

# Sample data partitioning in Python
# Load or create your dataset
data = pd.read_csv("your_dataset.csv")

# Split the data into training (70%) and testing (30%) sets
train_data, test_data = train_test_split(data, test_size=0.3, random_state=123)

# Display the number of rows in training and testing sets
print("Number of rows in training set:", len(train_data))
print("Number of rows in testing set:", len(test_data))

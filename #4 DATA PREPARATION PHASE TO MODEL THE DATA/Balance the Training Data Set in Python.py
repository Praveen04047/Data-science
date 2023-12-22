
import pandas as pd

# Sample data balancing in Python
# Load or create your dataset
data = pd.read_csv("your_dataset.csv")

# Check the class distribution
print(data['target_variable'].value_counts())

# Balance the training set by sampling with replacement
balanced_data = data[data['target_variable'] == 'class_to_balance'].sample(
    n=data['target_variable'].value_counts().min(), replace=True)

# Check the balanced class distribution
print(balanced_data['target_variable'].value_counts())

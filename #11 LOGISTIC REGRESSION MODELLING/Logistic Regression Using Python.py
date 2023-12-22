# Sample Logistic Regression in Python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd

# Load or create your dataset
data = pd.read_csv("your_dataset.csv")

# Create a binary response variable (e.g., mpg > median)
data['binary_response'] = (data['mpg'] > data['mpg'].median()).astype(int)

# Split the data into features and target variable
X = data[['mpg', 'disp', 'hp']]
y = data['binary_response']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

# Train a logistic regression model
logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)

# Make predictions on the test set
predictions = logistic_model.predict(X_test)

# Evaluate the model
conf_matrix = confusion_matrix(y_test, predictions)
class_report = classification_report(y_test, predictions)

print("Confusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(class_report)

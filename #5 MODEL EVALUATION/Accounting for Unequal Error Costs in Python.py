# Question 23 -> Accounting for Unequal Error Costs in Python:

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd

# Sample accounting for unequal error costs in Python
# Load or create your dataset
data = pd.read_csv("your_dataset.csv")

# Split the data into features and target variable
X = data.drop(columns=['target_variable'])
y = data['target_variable']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

# Train a model (e.g., Decision Tree)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Create a confusion matrix
conf_matrix = confusion_matrix(y_test, predictions)

# Create a cost matrix with unequal error costs
cost_matrix = [[0, 1], [10, 0]]

# Calculate precision and recall accounting for unequal error costs
precision = conf_matrix[1, 1] / (conf_matrix[1, 1] + conf_matrix[0, 1])
recall = conf_matrix[1, 1] / (conf_matrix[1, 1] + conf_matrix[1, 0])

# Calculate cost-sensitive F1 score
f1_score = 2 * (precision * recall) / (precision + recall)

print("Precision:", precision)
print("Recall:", recall)
print("F1 Score (cost-sensitive):", f1_score)


# Sample Neural Network in Python
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd

# Load or create your dataset
data = pd.read_csv("your_dataset.csv")

# Split the data into features and target variable
X = data.drop(columns=['target_variable'])
y = data['target_variable']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

# Define the neural network model
nn_model = MLPClassifier(hidden_layer_sizes=(5, 2), activation='relu', max_iter=1000, random_state=123)

# Train the model
nn_model.fit(X_train, y_train)

# Make predictions on the test set
predictions = nn_model.predict(X_test)

# Evaluate the model
conf_matrix = confusion_matrix(y_test, predictions)
class_report = classification_report(y_test, predictions)

print("Confusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(class_report)

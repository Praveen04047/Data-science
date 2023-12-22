
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree

# Sample CART decision tree in Python
# Load or create your dataset
data = pd.read_csv("your_dataset.csv")

# Split the data into features and target variable
X = data.drop(columns=['target_variable'])
y = data['target_variable']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

# Build a CART decision tree
tree_model = DecisionTreeClassifier()
tree_model.fit(X_train, y_train)

# Display the tree (for visualization)
tree.plot_tree(tree_model)

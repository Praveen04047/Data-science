# Sample Association Rules Mining in Python
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd

# Load or create your dataset
data = pd.read_csv("your_dataset.csv")

# Transform the data into a transaction format (list of lists)
transactions = data.apply(lambda x: x.dropna().tolist(), axis=1).tolist()

# Mine association rules
frequent_itemsets = apriori(transactions, min_support=0.1, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# Display the mined rules
print(rules)

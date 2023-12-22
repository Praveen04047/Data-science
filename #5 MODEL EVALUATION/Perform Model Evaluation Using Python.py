import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.metrics import mean_absolute_error

sales_train = pd.read_csv(r"C:\Users\Ideapad slim 5\OneDrive\Desktop\data set\Website Data Sets\clothing_sales_training.csv")
sales_test = pd.read_csv(r"C:\Users\Ideapad slim 5\OneDrive\Desktop\data set\Website Data Sets\clothing_sales_test.csv")

X = pd.DataFrame(sales_train[['CC', 'Days', 'Web']])
y = pd.DataFrame(sales_train[['Sales per Visit']])

X = sm.add_constant(X)

model01 = sm.OLS(y, X).fit()

model01.summary()

X_test = pd.DataFrame(sales_test[['CC', 'Days', 'Web']])
y_test = pd.DataFrame(sales_test[['Sales per Visit']])
X_test = sm.add_constant(X_test)
model01_test = sm.OLS(y_test, X_test).fit()
model01_test.summary()

X = pd.DataFrame(sales_train[['CC', 'Days']])
X = sm.add_constant(X)

model02 = sm.OLS(y, X).fit()
model02.summary()

X_test = pd.DataFrame(sales_test[['CC', 'Days']])
X_test = sm.add_constant(X_test)
model02_test = sm.OLS(y_test, X_test).fit()
model02_test.summary()

# Single prediction example
cust01 = np.array([1, 0, 333])
prediction_cust01 = model02.predict(cust01.reshape(1, -1))
print("Prediction for cust01:", prediction_cust01)

# Predictions on the test set
ypred = model02.predict(X_test)

# Calculate the Mean Absolute Error (MAE)
mae = mean_absolute_error(y_true=y_test, y_pred=ypred)
print("Mean Absolute Error (MAE) on the test set:", mae)

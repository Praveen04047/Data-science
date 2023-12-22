# Sample Poisson Regression in Python
import statsmodels.api as sm
import pandas as pd

# Load or create your dataset
data = pd.read_csv("your_dataset.csv")

# Fit a Poisson regression model
poisson_model = sm.GLM(data['mpg'], data[['disp', 'hp']], family=sm.families.Poisson()).fit()

# Display model summary
print(poisson_model.summary())

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.savefig('output_plot.png')

from sklearn.linear_model import LinearRegression
import joblib

model = LinearRegression()
# Train the model
# ...

# Save the trained model
joblib.dump(model, 'trained_model.joblib')
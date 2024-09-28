import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")

print(df.head())
prod_per_year = df.groupby('year').totalprod.mean().reset_index()
X = df['year']
X = X.values.reshape(-1, 1)

# plot total production
y = df['totalprod']
plt.scatter(X, y)
plt.show()

# Linear regression model
regr = linear_model.LinearRegression()

# fit the model to the data & print: slope of the line(b) = coef, intercept of the line(m)
regr.fit(X,y)
print(regr.coef_[0])
print(regr.intercept_)

# predictions & plot it
y_predict = regr.predict(X)
plt.plot(X, y_predict)
plt.show()

# Predict the Honey Decline on 2050
X_future = np.array(range(2013, 2051))
print(X_future)
X_future = X_future.reshape(-1,1)

# future predict
future_predict = regr.predict(X_future)
plt.plot(X_future, future_predict)
plt.show()
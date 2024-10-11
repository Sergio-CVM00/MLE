import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

# Input code here:
plt.scatter(df[['size_sqft']], df[['rent']], alpha=0.4)
plt.scatter(df[['min_to_subway']], df[['rent']], alpha=0.4)
plt.scatter(df[['has_roofdeck']], df[['rent']], alpha=0.4)

plt.show()

# To see if there are any features that don’t affect price linearly, let’s graph the different features against rent.
# In regression, the independent variables will either have a positive linear relationship to the dependent variable, 
# a negative linear relationship, or no relationship. A negative linear relationship means that as X values increase, Y values will decrease.
# Similarly, a positive linear relationship means that as X values increase, Y values will also increase. 
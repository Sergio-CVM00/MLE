import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
data = pd.read_csv('tennis_stats.csv')
print(data.head())
X = data[['FirstServeReturnPointsWon']]
y = data[['Winnings']]
plt.scatter(X, y)
plt.show()

###################### 1st ######################
# preparing the data (outcome=winnigns) (features=1stServeReturnPointsWon)
features = data[['FirstServeReturnPointsWon']]
outcome = data[['Winnings']]

# split data: training & test
features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8)

# linear regression: winnings x FirstServeReturnPointsWon
model = LinearRegression()
model.fit(features_train,outcome_train)
model.score(features_test,outcome_test)

# predicted outcome based on model
prediction = model.predict(features_test)
plt.scatter(outcome_test,prediction, alpha=0.4)
plt.show()

###################### 2nd ######################
# 1. preparing the data (outcome=winnigns) (features=BreakPointsOpportunities)
features = data[['BreakPointsOpportunities']]
outcome = data[['Winnings']]

# 2. split data: training & test
features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8)

# 3. linear regression: winnings x BreakPointsOpportunities
model = LinearRegression()
model.fit(features_train,outcome_train)
model.score(features_test,outcome_test)

# 4. predicted outcome based on model
prediction = model.predict(features_test)
plt.scatter(outcome_test,prediction, alpha=0.4)
plt.show()

###################### 3rd ######################
# 1. preparing the data: two features to predict
features = data[['BreakPointsOpportunities',
'FirstServeReturnPointsWon']]
outcome = data[['Winnings']]

# 2. split data: training & test
features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8)

# 3. linear regression: winnings x BreakPointsOpportunities x FirstServeReturnPointsWon
model = LinearRegression()
model.fit(features_train,outcome_train)
model.score(features_test,outcome_test)

# 4. predicted outcome based on model
prediction = model.predict(features_test)
plt.scatter(outcome_test,prediction, alpha=0.4)
plt.show()

###################### 4th ######################
# 1. preparing the data: two features to predict
features = data[['FirstServe','FirstServePointsWon','FirstServeReturnPointsWon',
'SecondServePointsWon','SecondServeReturnPointsWon','Aces',
'BreakPointsConverted','BreakPointsFaced','BreakPointsOpportunities',
'BreakPointsSaved','DoubleFaults','ReturnGamesPlayed','ReturnGamesWon',
'ReturnPointsWon','ServiceGamesPlayed','ServiceGamesWon','TotalPointsWon',
'TotalServicePointsWon']]
outcome = data[['Winnings']]

# 2. split data: training & test
features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.7)

# 3. linear regression:
model = LinearRegression()
model.fit(features_train,outcome_train)
model.score(features_test,outcome_test)

# 4. predicted outcome based on model
prediction = model.predict(features_test)
plt.scatter(outcome_test,prediction, alpha=0.8)
plt.show()
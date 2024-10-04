import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

# check dataset
digits = datasets.load_digits()
print(digits)
print(digits.DESCR)
print(digits.data)
print("TARGET = ", digits.target)

# plot data images
plt.gray() 
plt.matshow(digits.images[100])
plt.show()
print(digits.target[100])

# K-means clustering start
# No. digits
k = 10 

model = KMeans(n_clusters=k, random_state=42)
model.fit(digits.data)

# Visualizing after K-Means
fig = plt.figure(figsize=(8, 3))
fig.suptitle('Cluser Center Images', fontsize=14, fontweight='bold')

# loop to displays cluster_centers
for i in range(10):
  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)

  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
  
plt.show()

# Testing our model:
# get the array from 'test.html' 
# -> draw with your mouse in the squares (1,1,1,1) -> "Get array" 
new_samples = np.array(
[
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.14,5.80,0.61,0.00,0.00,0.00,0.00,0.53,4.50,7.62,2.52,0.00,0.00,0.00,0.38,7.47,7.62,7.62,3.21,0.00,0.00,0.00,0.00,1.98,1.98,7.63,4.04,0.00,0.00,0.00,0.00,0.00,0.00,6.94,4.58,0.00,0.00,0.00,0.31,6.71,7.62,7.62,7.55,6.18,2.98,0.00,0.08,3.51,3.28,3.05,3.81,5.18,2.82,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,6.48,3.66,0.00,0.00,0.00,0.00,0.00,1.68,7.63,5.19,0.00,0.00,0.00,0.00,2.75,7.47,7.62,5.34,0.00,0.00,0.00,0.00,2.59,4.50,5.80,6.79,0.00,0.00,0.00,0.00,0.00,0.00,3.36,7.62,0.84,0.00,0.00,0.00,2.59,5.34,6.25,7.62,5.26,0.00,0.00,0.00,2.59,5.34,5.34,4.58,2.59,0.00,0.00],
[0.00,0.00,0.00,0.23,1.15,0.00,0.00,0.00,0.00,0.00,0.15,4.65,7.55,0.31,0.00,0.00,3.51,4.12,6.48,7.62,7.62,1.22,0.00,0.00,5.19,6.86,5.95,3.66,7.62,1.52,0.00,0.00,0.00,0.00,0.00,1.52,7.62,1.52,0.00,0.00,0.00,0.00,1.07,3.20,7.62,3.35,1.60,0.00,0.46,7.32,7.62,7.62,7.62,7.62,7.63,0.61,0.00,2.75,2.75,1.45,0.76,1.91,2.21,0.00],
[0.00,0.00,0.00,0.00,1.30,0.00,0.00,0.00,0.00,0.00,0.00,1.83,7.62,1.37,0.00,0.00,0.00,0.23,0.84,4.42,7.62,2.82,0.00,0.00,0.00,4.50,7.62,7.62,7.40,6.03,0.00,0.00,0.00,0.92,2.29,1.37,4.20,7.63,0.00,0.00,0.00,0.46,3.05,3.28,5.64,7.47,4.27,2.75,0.00,1.98,7.63,7.62,7.02,6.10,7.40,7.47,0.00,0.00,0.00,0.00,0.00,0.00,0.84,0.69]
]
)

# predictions from our model
new_labels = model.predict(new_samples)
print(new_labels)

# mappping out the labels
for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')

# Remember, this model is trained on handwritten digits of 30 Turkish people (from the 1990’s)
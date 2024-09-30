from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# load the data
breast_cancer_data = load_breast_cancer()

# take a look
print(breast_cancer_data.data[0])
print(breast_cancer_data.feature_names)

# 0 = malignant
print(breast_cancer_data.target)
print(breast_cancer_data.target_names)

## Splitting the data into Training and Validation Sets
train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2, random_state = 100)

training_data, validation_set, training_labels, validation_labels = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2, random_state = 100)

# length of datas to check
print(len(training_data))
print(len(training_labels))

## Running the classifier sklearn model
classifier = KNeighborsClassifier(n_neighbors = 3)
classifier.fit(training_data, training_labels)
print(classifier.score(validation_set, validation_labels))

# loop to search the best k 1-100
max_index = 0
maximum = 0
accuracies = []
k_list = range(1, 101)

for k in range(1, 101):
  classifier = KNeighborsClassifier(n_neighbors = k)
  classifier.fit(training_data, training_labels)
  score_result = classifier.score(validation_set, validation_labels)

  if score_result > maximum : 
    maximum = score_result
    max_index = k
  
  print("score k:",k," = ", score_result)
  accuracies.append(score_result)
print("The best k index is =", max_index, ", with score =", maximum)

## TIME TO PLOT IT!
plt.plot(k_list, accuracies)
plt.title("Breast Cancer Classifier Accuracy")
plt.xlabel("K values")
plt.ylabel("Validation accuracy")
plt.show()
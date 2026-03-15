"""
this is example uses the rather ubiquitous breast cancer dataset as an
example. First, we import the used libraries and modules
"""
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score

# load the breast cancer wisconsin dataset
dataset=load_breast_cancer()
# the dataset is a dictionary-like object that contains the data and the target labels

X = pd.DataFrame(dataset.data, columns=dataset.feature_names)

# we will select only three features for this example to make it easier to visualize the decision boundaries of the KNN classifier
X = X[['mean smoothness', 'mean concavity', 'radius error']]

# the target labels are binary, indicating whether a tumor is malignant (1) or benign (0
y = pd.Categorical.from_codes(dataset.target, dataset.target_names)
# we will convert the target labels into a binary format using one-hot encoding, which is a common preprocessing step for classification tasks
y = pd.get_dummies(y, drop_first=True)

# we will split the dataset into a training set and a test set using the train_test_split function from scikit-learn
X_train, X_test, y_train, y_test = train_test_split(X, y)

# we will initialize the KNN classifier with a specified number of neighbors and a distance metric
knn = KNeighborsClassifier(n_neighbors=4, metric='manhattan')

# we will fit the KNN classifier to the training data and then use it to make predictions on the test set
knn.fit(X_train, y_train.values.ravel())


y_pred = knn.predict(X_test)
# we will evaluate the performance of the KNN classifier using various metrics such as confusion matrix, accuracy score, recall score, and precision score
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
print(recall_score(y_test, y_pred))
print(precision_score(y_test, y_pred))
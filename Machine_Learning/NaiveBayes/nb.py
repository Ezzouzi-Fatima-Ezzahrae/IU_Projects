# Import the required libraries
# pandas: used for reading and manipulating tabular data (like CSV files)
# GaussianNB: implementation of the Gaussian Naive Bayes classifier from sklearn
import pandas as pd
from sklearn.naive_bayes import GaussianNB


# ---------------------------------------------------------
# STEP 1: Load the training dataset
# ---------------------------------------------------------

# Read the CSV file that contains the training data.
# sep=';' means the columns in the CSV file are separated by semicolons instead of commas.
exam_data = pd.read_csv('bayes.csv', sep=';')

# Print the dataset to see its contents in the console
print(exam_data)


# ---------------------------------------------------------
# STEP 2: Separate features (X) and labels (y)
# ---------------------------------------------------------

# Features (X): all columns except the target column "Passed"
# These are the inputs the model will learn from.
X = exam_data.drop(columns=['Passed'])

# Labels (y): the target variable we want the model to predict
# In this example, it tells whether the student passed (1) or failed (0)
y = exam_data['Passed']


# ---------------------------------------------------------
# STEP 3: Convert categorical data into numeric format
# ---------------------------------------------------------

# The column "Invested effort" contains text values (low, medium, high).
# Machine learning models require numeric values.
# pd.get_dummies() converts each category into binary columns.
# Example:
# low -> [1,0,0]
# medium -> [0,1,0]
# high -> [0,0,1]
X = pd.get_dummies(X)


# ---------------------------------------------------------
# STEP 4: Create and train the Naive Bayes model
# ---------------------------------------------------------

# Initialize the Gaussian Naive Bayes classifier
# It assumes that feature values follow a Gaussian (normal) distribution
model = GaussianNB()

# Train the model using the training data
# The model learns the relationship between the features (X) and the labels (y)
model.fit(X, y)


# ---------------------------------------------------------
# STEP 5: Load the test dataset
# ---------------------------------------------------------

# This dataset contains new students whose results we want to predict
test_data = pd.read_csv('bayes_test.csv', sep=';')

# Separate the features and labels in the test dataset
X_test = test_data.drop(columns=['Passed'])
y_test = test_data['Passed']


# Convert categorical values in the test set the same way as the training data
X_test = pd.get_dummies(X_test)


# ---------------------------------------------------------
# STEP 6: Generate predictions
# ---------------------------------------------------------

# Use the trained model to predict whether each student will pass or fail
y_pred = model.predict(X_test)


# ---------------------------------------------------------
# STEP 7: Print the prediction results
# ---------------------------------------------------------

print(f'Prediction results:\n{y_pred}')


# Output example:
# [0 1 1]
# This means:
# Student 11 -> predicted to fail (0)
# Student 12 -> predicted to pass (1)
# Student 13 -> predicted to pass (1)
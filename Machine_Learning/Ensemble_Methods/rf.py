import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# load the dataset
dataset=pd.read_csv('takingAwalk_dataset.csv', sep=';')
print(dataset.head())

# featuers 
x=dataset.drop(columns=['Label','Week'])
# label 
y=dataset['Label']
# encoding the categorical data
x=pd.get_dummies(x)  
# split the dataset
x_train , x_test , y_train , y_test =train_test_split(
    x,
    y,
    test_size=0.3,
    shuffle=True, # Because data is ordered by weeks ; If we don't shuffle: ,training = winter , testing = summer / That would be bad.
    random_state=42
)

# create the model 

model=RandomForestClassifier(
    n_estimators=100, # the forest contains 100 desicion trees 
    max_depth=3, # the max depth of each tree is 3 levels to avoid overfitting
    random_state=42
)

# Train the model 
model.fit(x_train, y_train)
"""
Random Forest:

1️⃣ builds many decision trees
2️⃣ each tree learns patterns
3️⃣ predictions are combined by majority vote

Example idea:

Tree 1 → walk
Tree 2 → no walk
Tree 3 → walk

Final decision:

walk
"""
#make prediction 
y_pred=model.predict(x_test)   #The model predicts whether the person went for a walk.

# evaluate the model 
print(confusion_matrix(y_test,y_pred))
print(accuracy_score(y_test,y_pred))

feature_score=pd.Series(
    model.feature_importances_, # The importance score of each feature in the model.
    index=x_train.columns # The names of the features corresponding to the importance scores.
    ).sort_values(ascending=False)  # Sort the features by importance in descending order

'''
Here we access a property from the trained Random Forest model.

feature_importances_ gives:

The importance score of each feature used in the model.

Example output:

[0.19, 0.18, 0.15, 0.14, 0.17, 0.16]

Each number tells how much that feature helped the model make predictions.

Important idea:

higher value → more important feature
'''
    
'''
index=x_train.columns //
Here we assign names to the importance values.

X_train.columns contains the feature names.

Example:

Index([
'Outlook_Rainy',
'Outlook_Sunny',
'Humidity_High',
'Humidity_Normal',
'Wind_No',
'Wind_Yes'
])

So now we match:

importance score → feature name

Example result:

Humidity_Normal   0.19
Outlook_Sunny     0.18
Wind_No           0.16

Without this line, we would only see numbers without knowing which feature they belong to.
'''
print(feature_score)

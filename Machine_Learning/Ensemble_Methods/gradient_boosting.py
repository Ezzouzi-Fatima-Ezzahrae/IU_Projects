import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# load dataset 

dataset=pd.read_csv('takingAwalk_dataset.csv', sep=';')
print(dataset.head())
# featuers
x=dataset.drop(columns=['Label','Week'])
# label
y=dataset['Label']
# encoding the categorical data
x=pd.get_dummies(x)
#split datset 
x_train , x_test , y_train , y_test =train_test_split(
    x,
    y,
    test_size=0.3,
    shuffle=True, # Because data is ordered by weeks ; If we don't shuffle: ,training = winter , testing = summer / That would be bad.
    random_state=42
)
# create the model
model=GradientBoostingClassifier(
    n_estimators=100,
    max_depth=3,
    random_state=42

)
# Train the model
model.fit(x_train,y_train) 

#make prediction
y_pred=model.predict(x_test)

#evaluate the model 
print(confusion_matrix(y_test,y_pred))
print(accuracy_score(y_test,y_pred))

# feature importance 
feature_score=pd.Series(
    model.feature_importances_,
    index=x_train.columns,
).sort_values(ascending=False)
print(feature_score)

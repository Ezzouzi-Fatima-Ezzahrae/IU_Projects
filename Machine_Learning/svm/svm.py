#import libraries
import pandas as pd 
from sklearn.datasets  import load_breast_cancer
from sklearn.model_selection import train_test_split

from sklearn import svm

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

#load the dataset

dataset=load_breast_cancer()
# transform it to a dataframe
x=pd.DataFrame(dataset.data , columns=dataset.feature_names)
# prepare the abel (target)
y=pd.Categorical.from_codes(dataset.target , dataset.target_names)
y=pd.get_dummies(y, drop_first=True)

#split the dataset into training and testing sets

x_train , x_test , y_train , y_test = train_test_split(
    x,y,
    test_size=0.3 ,
    random_state=42
)
# create the model 
model=svm.SVC(kernel='rbf')

#train the model
model.fit(x_train,y_train.values.ravel())

#make predictons 
y_pred=model.predict(x_test)

# evluate the model 
print(confusion_matrix(y_test,y_pred))

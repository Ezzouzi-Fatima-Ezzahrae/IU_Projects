from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import numpy as np
from matplotlib import pyplot as plt 



#load the iris dataset
iris=datasets.load_iris()
print(iris.data)

# split data into features and labeks
# features
x=iris["data"][:,3:]

#Labels
y=(iris["traget"]==2).astype(int)

#initialize the logistic regression model
log_reg=LogisticRegression()
log_reg.fit(x,y)


# once the model has been trained , it can be used to predict the probability , for a given petal width between 0 and 3 
x_new=np.linspace(0,3,1000).reshape(-1,1)
y_proba=log_reg.predict_proba(x_new)

# now we can plot the probability of the iris being of the virginica class as a function of the petal width ranging from 0 to 3 cm 
plt.plot(x_new,y_proba[:,1],"g-",
         label="iris_viirginica")
plt.plot(x_new,y_proba[:,0],"b--",
         label="not-iris-virginica"
         )
plt.xlabel("Petal Width")
plt.ylabel("Probability")
plt.legend()
plt.show()
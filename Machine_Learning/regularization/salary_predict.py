import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

dataset= pd.read_csv("salary_data.csv")
x_train=dataset.drop(columns=["Salary"])
y_train=dataset.iloc[:,1].values

regressor=LinearRegression()
regressor.fit(x_train,y_train)

plt.scatter(x_train,y_train,color="red")
plt.plot(x_train,regressor.predict(x_train))
plt.title("Experience vs Salary (train set)")
plt.xlabel("Experience in years")
plt.ylabel("Salary")
plt.show()
print(regressor.intercept_,regressor.coef_)
# Example: Define x_newdata with new experience values (assuming single feature)
import numpy as np
x_newdata = np.array([[5], [10], [15]])  # Replace with actual new data

# Predict salaries
y_pred = regressor.predict(x_newdata)
print("Predicted salaries:", y_pred)
 
# Lasso Regression
Lasso_regressor=Lasso(alpha=0.1)
Lasso_regressor.fit(x_train,y_train)
print(Lasso_regressor.intercept_, Lasso_regressor.coef_)
#Ridge regression
Ridge_reg=Ridge(aplha=1)
Ridge_reg.fit(x_train,y_train)
print(Ridge_reg.intercept_,Ridge_reg.coef_)

# ElasticNet Regression
ElasticNet_reg=ElasticNet(alpha=0.1,l1_ratio=1) #lasso mean l1 norm and means alpha times sum pf absolute of coef ,ridge L2 (alpha time SS of weights(coef))
ElasticNet_reg.fit(x_train,y_train)
print(ElasticNet_reg.intercept_, ElasticNet_reg.coef_)



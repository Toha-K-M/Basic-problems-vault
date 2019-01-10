import  matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv',index_col=0)

#displaying first five line
print(data.head())
#displaying last five line
print(data.tail())

print(data.shape)

import seaborn as sns

#plt.figure()
#sns.pairplot(data[["TV","radio","newspaper","sales"]])
sns.pairplot(data, x_vars=["TV","radio","newspaper"], y_vars=["sales"], size = 7, aspect=0.7, kind='reg')
#size and aspect is for better visualization .. just to increase the size of font
#plt.savefig("1_seaborn_pair_plot.png")
#plt.show() #this will show the graph

feature_cols = ["TV","radio","newspaper"]

X = data[feature_cols]
print(X.head())

y = data["sales"]
print(y.head())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.linear_model import LinearRegression

linreg = LinearRegression()

linreg.fit(X_train,y_train)

print(linreg.intercept_)
print(linreg.coef_)
# pair the feature names with the coefficients
list(zip(feature_cols, linreg.coef_))

y_pred = linreg.predict(X_test)

print(y_pred)

from sklearn import  metrics
print("MAE: ", metrics.mean_absolute_error(y_test,y_pred))
# some other error prediction in jupyter notebook
print("MSE: ", metrics.mean_squared_error(y_test, y_pred))
print("RMSE: ", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# removing feature to lessen error ......... more on jupyter notebool

print("\n\n***************************************************************")
print("********************** Feature Selection **********************")
print("***************************************************************\n\n")

feature_cols = ['TV', 'radio']

X = data[feature_cols]
y = data.sales

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
linreg.fit(X_train,y_train)

y_pred = linreg.predict(X_test)

print("After removing newspaper feature : \nRMSE: ", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

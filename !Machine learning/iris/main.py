from sklearn.datasets import load_iris

iris = load_iris()
print(type(iris))
print(iris.data)

print(iris.feature_names)
print(iris.target)
print(iris.target_names)
print(type(iris.data))
print(type(iris.target))

print(iris.data.shape)
print(iris.target.shape)

#####################################

X,y = iris.data,iris.target

print(X.shape)
print(y.shape)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)
print(knn)

knn.fit(X, y)
print(knn.predict([[3,5,4,2]]))

X_new = [[3,4,5,2],[5,4,3,2]]
print("Knn: " , knn.predict(X_new))

knn_twick = KNeighborsClassifier(n_neighbors=5)
knn_twick.fit(X, y)
print("Knn Twick: " , knn_twick.predict(X_new))

########################################

from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()

logreg.fit(X, y)

print("Logistic Regression: " , logreg.predict(X_new))

############# Accuracy Measure ###############################

y_pred = logreg.predict(X)

print(y_pred, "\nLength: ",len(y_pred))

# compute classification accuracy for the logistic regression model
from sklearn import metrics
print("Logistic Regression Accuracy: " , metrics.accuracy_score(y, y_pred)) # known as training accuracy

y_pred = knn_twick.predict(X)
print("Knn_Twick Accuracy: " , metrics.accuracy_score(y, y_pred))

y_pred = knn.predict(X)
print("Knn Accuracy: " , metrics.accuracy_score(y, y_pred))

############# Evaluation Procedure ############
######## Train/Test ###################

# splitting
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=4)

print("X_train: ", X_train.shape, "X_test: ", X_test.shape)
print("y_train: ", y_train.shape, "y_test: ", y_test.shape)

# train the model
logreg.fit(X_train,y_train)
knn_twick.fit(X_train,y_train)
knn.fit(X_train,y_train)

#predicting logreg
y_pred = logreg.predict(X_test)
#printing accuracy
print("\n\n***************************************************************************")
print("************************* after train_test_split **************************")
print("***************************************************************************\n\n")

print("Logistic Regression Accuracy",metrics.accuracy_score(y_test, y_pred))

#predicting knn_twick
y_pred = knn_twick.predict(X_test)
print("Knn Twick Accuracy: ", metrics.accuracy_score(y_test,y_pred))
#predicting knn
y_pred = knn.predict(X_test)
print("Knn Accuracy: ", metrics.accuracy_score(y_test,y_pred))

print("**************** checking for different k=n where n = 1,2,3,....,n values ****************")

k_range = list(range(1,26))
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train,y_train)
    y_pred = knn.predict(X_test)
    scores.append(metrics.accuracy_score(y_test,y_pred))

##### printing in graph #########
import matplotlib.pyplot as plt

# plot the relationship between K and testing accuracy

plt.plot(k_range,scores)
plt.xlabel('value of K for KNN')
plt.ylabel('Testing Accuracy')
plt.show() # this will show the graph

#### its important to train the mchine with whole data after selecting the best model

knn = KNeighborsClassifier(n_neighbors=11)
knn.fit(X,y)

y_pred = knn.predict([[3,5,4,2]])
print("best prediction : ", y_pred)

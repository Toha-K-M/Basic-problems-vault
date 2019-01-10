import pandas as pd
import numpy as np

X = pd.read_csv('C:/Users/MasterChief/Downloads/Datasets/RNA-Seq Datasets/data.csv', header=None, skiprows=1).iloc[:,1:].values
y = pd.read_csv('C:/Users/MasterChief/Downloads/Datasets/RNA-Seq Datasets/labels.csv', header=None, skiprows=1).iloc[:,1].values


print(X.shape, y.shape)

from sklearn.preprocessing import LabelEncoder
y = LabelEncoder().fit_transform(y)

from sklearn.preprocessing import Imputer
X[:, 0:X.shape[1]] = Imputer(strategy='mean').fit_transform(X[:, 0:X.shape[1]])

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier

Classifiers = [
    LogisticRegression(),
    KNeighborsClassifier(),
    DecisionTreeClassifier(),
    GaussianNB(),
    BaggingClassifier(),
    RandomForestClassifier(),
    AdaBoostClassifier(),
    GradientBoostingClassifier(),
    SVC(kernel='rbf', probability=True)
]
from sklearn.metrics import accuracy_score, label_ranking_average_precision_score,average_precision_score, recall_score, mean_absolute_error, f1_score

from sklearn.model_selection import StratifiedKFold
cv = StratifiedKFold(n_splits=10, shuffle=True)

accuracy = []
precision = []
recall = []
MAE = []
f1 = []

for classifier in Classifiers:
    print(classifier.__class__.__name__)
    print("--------------------------------------------------------------------------")

    for train_index, test_index in cv.split(X, y):
        X_train = X[train_index]
        X_test = X[test_index]

        y_train = y[train_index]
        y_test = y[test_index]

        # Step 06 : Scaling the feature
        from sklearn.preprocessing import StandardScaler

        scale = StandardScaler()
        X_train = scale.fit_transform(X_train)
        X_test = scale.transform(X_test)

        model = classifier

        model.fit(X_train, y_train)

        y_artificial = model.predict(X_test)

        y_proba = model.predict_proba(X_test)[:, 1]

        accuracy.append(accuracy_score(y_pred=y_artificial, y_true=y_test))
        precision.append(label_ranking_average_precision_score(y_test, y_artificial))
        recall.append(recall_score(y_pred=y_artificial, y_true=y_test))
        MAE.append(mean_absolute_error(y_pred=y_artificial, y_true=y_test))
        f1.append(f1_score(y_pred=y_artificial, y_true=y_test))

    print('average_accuracy: ', np.mean(accuracy))
    print('precision_score: ', np.mean(precision))
    print('recall_score: ', np.mean(recall))
    print('mean_square_error: ', MAE)
    print('F_score:: ', f1)
    print('_______________________________________')


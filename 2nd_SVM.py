import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import rcParams
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.pipeline import Pipeline
rcParams['figure.figsize'] = 8,6


data = pd.read_csv('C:/keras_project/SVM/2nd_SVM.csv', header=None , encoding='latin-1') ##load data
names=['feature_1', 'feature_2', 'feature_4', 'feature_4', 'feature_5', 'feature_6','feature_7', 'feature_8',
        'feature_9', 'feature_10', 'feature_11', 'feature_12', 'label']
data.columns = names

X = data.drop(['label'], axis = 1)
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 97)##split train, test data

second_svm_model = SVC(C =  2.575757717171717, kernel = 'linear', probability = True, verbose = 4) ## define svm model
second_svm = second_svm_model.fit(X_train, y_train) ## compile model
y_predict = second_svm.predict(X_test)

from sklearn.metrics import accuracy_score ## test result
accuracy_score(y_test, y_predict)



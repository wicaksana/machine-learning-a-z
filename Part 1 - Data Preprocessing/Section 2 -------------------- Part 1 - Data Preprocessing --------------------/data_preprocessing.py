import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer

dataset = pd.read_csv('../../datasets/Data_Preprocessing/Data.csv')
print(dataset.values)

X = dataset.iloc[:, :-1].values
print(X)

Y = dataset.iloc[:,
    3].values
print(Y)

# data preprocessing
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
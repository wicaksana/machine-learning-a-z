import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('../../datasets/Data_Preprocessing/Data.csv')
print(dataset.values)

X = dataset.iloc[:, :-1].values
print(X)

Y = dataset.iloc[:, 3].values
print(Y)
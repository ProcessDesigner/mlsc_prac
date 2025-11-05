import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Admission_Predict.csv')

X = df['GRE Score'].values
Y = df['TOEFL Score'].values

n = len(X)
mx = sum(X)/n
my = sum(Y)/n
m = sum([(X[i]-mx)*(Y[i]-my)for i in range(n)])/sum([(X[i]-mx)**2 for i in range(n)])
c = my - m*mx
X = np.array(X)
y_pred = m*X+c
plt.scatter(X,Y)
plt.plot(X,y_pred,color='red')
plt.show()

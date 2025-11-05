import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler
df=pd.read_csv(r"C:\Users\SitaRam\Downloads\Social_Network_Ads.csv")
print("Dataset Overview:")
print(df.head())
X=df[['Age','EstimatedSalary']]
y=df['Purchased']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
X_train=StandardScaler().fit_transform(X_train)
X_test=StandardScaler().fit_transform(X_test)
model=LogisticRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("Model accuracy: ",accuracyaccuracy_score(y_test,y_pred))
print("Confusion matrix: ",confusion_matrix(y_test,y_pred))
print("Classification report: ",classification_report(y_test,y_pred))
plt.figure(figsize=(8,6))
plt.scatter(X_test[:,0], X_test[:,1], c=y_pred, cmap='bwr', alpha=0.7)
plt.title("Logistic Regression Classification Results")
plt.xlabel("Age (scaled)")
plt.ylabel("Estimated Salary (scaled)")
plt.show()

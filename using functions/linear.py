import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
df=pd.read_csv(r"C:\Users\SitaRam\Downloads\StudentsPerformance.csv")
print("Dataset Preview:")
print(df.head())
X=df[['reading score','writing score']]
y=df['math score']
X_train,X_test,y_train,y_test= train_test_split(X, y, test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("\nModel Evaluation:")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))
line_points = np.linspace(y_test.min(), y_test.max(), 100)
plt.plot(line_points, line_points, color='red', linewidth=2, label='Perfect Prediction Line')
plt.scatter(y_test, y_pred, color='blue')
plt.xlabel("Actual Math Scores")
plt.ylabel("Predicted Math Scores")
plt.title("Actual vs Predicted (Linear Regression)")
plt.show()
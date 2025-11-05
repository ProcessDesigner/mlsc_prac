import math

X=[1,2,4,5]
Y=[0,0,1,1]

m = 0.0
lr = 0.1
b = 0.0
epochs = 100

for _ in range(epochs):
    for i in range(len(X)):
        z = m*X[i]+b
        p = 1/(1+2.71828**(-z))
        err = Y[i] - p
        m+=lr*err*X[i]
        b+=lr*err


correct = 0
for i in range(len(X)):
    p = 1/(1+2.71828**(-(m*X[i]+b)))
    pred = 1 if p>0.5 else 0
    if pred == Y[i]:
        correct += 1
print("Accuracy:",(correct/len(X))*100,"%")
print("final weights: m = ",round(m,3),", b = ",round(b,3))

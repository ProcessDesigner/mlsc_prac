import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom
iris = load_iris()
X = iris.data
y = iris.target
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
som = MiniSom(x=7, y=7, input_len=X_scaled.shape[1], sigma=1.0, learning_rate=0.5)
som.random_weights_init(X_scaled)
print("Training SOM...")
som.train_random(X_scaled, num_iteration=1000)
print("Training completed.")
plt.figure(figsize=(8, 8))
for i, x in enumerate(X_scaled):
    w = som.winner(x) # Best Matching Unit (BMU)
    plt.text(w[0] + 0.5, w[1] + 0.5, str(y[i]),
    color=plt.cm.rainbow(y[i] / 2), fontdict={'size': 12, 'weight': 'bold'})
plt.xlim([0, som.get_weights().shape[0] + 1])
plt.ylim([0, som.get_weights().shape[1] + 1])
plt.title("Self-Organizing Map on Iris Dataset")
plt.show()
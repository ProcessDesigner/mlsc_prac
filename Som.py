import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1,1,0,0],[0,0,0,1],[1,0,0,0],[0,0,1,1]])
W = np.array([[0.2,0.8,0.6,0.4],[0.5,0.7,0.9,0.3]])

lr = 0.5

print("Initial Weights: \n",W)


for x in X:
    d = np.linalg.norm(W - X,axis=1)
    j = np.linalg(d)
    W[j] = W[j] + lr*(x-W[j])
    print("\nAfter Input ",x,"-> Updated Weights:\n",W)

print("\n FInal Weights:\n",W)

clusters = [np.argmin(np.linalg.norm(W-x,axis=1)) for x in X]
print("\nClusters :",clusters)

plt.scatter(range(len(X)),clusters,c = clusters,s = 200)
plt.title("SOM clustering Visualisation")
plt.xlabel("Input Index")
plt.ylabel("cluster")
plt.show()


import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import KernelPCA
from sklearn.preprocessing import StandardScaler
iris = load_iris()
X = iris.data
y = iris.target
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kpca = KernelPCA(n_components=2, kernel="rbf", gamma=15)
X_kpca = kpca.fit_transform(X_scaled)
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.scatter(X_scaled[:,0], X_scaled[:,1], c=y, cmap=plt.cm.Set1, s=40)
plt.title("Iris Dataset (first 2 features)")
plt.subplot(1,2,2)
plt.scatter(X_kpca[:,0], X_kpca[:,1], c=y, cmap=plt.cm.Set1, s=40)
plt.title("Iris Dataset after Kernel PCA (RBF kernel)")
plt.show()
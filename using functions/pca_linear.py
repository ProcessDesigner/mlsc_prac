import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
iris=load_iris()
X=iris.data
y=iris.target
target_names=iris.target_names
X_scaled=StandardScaler().fit_transform(X)
pca=PCA(n_components=2)
X_pca=pca.fit_transform(X_scaled)
print("Explained variance ratio: ", pca.explained_variance_ratio_)
plt.figure(figsize=(8,6))
colors=['red','blue','green']
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], color=color, lw=2, label=target_name)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('PCA on Iris Dataset')
    plt.legend()
    plt.grid(True)
    plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class SSOM:
    def __init__(self, m, n, input_dim, n_classes, lr=0.5, sigma=None):
        self.m, self.n = m, n
        self.grid_size = m * n
        self.input_dim, self.n_classes = input_dim, n_classes
        self.lr0, self.sigma0 = lr, sigma if sigma else max(m, n) / 2
        self.weights = np.random.randn(self.grid_size, input_dim)
        self.label_weights = np.random.randn(self.grid_size, n_classes) * 0.01
        self.coords = np.array([(i, j) for i in range(m) for j in range(n)])

    def _decay(self, val, epoch, max_epoch): return val * np.exp(-epoch / max_epoch)
    def _bmu(self, x): return np.argmin(np.linalg.norm(self.weights - x, axis=1))
    def _neigh(self, bmu, sigma):
        d2 = np.sum((self.coords - self.coords[bmu])**2, axis=1)
        return np.exp(-d2 / (2*sigma**2))

    def fit(self, X, y, epochs=50):
        self.hist = []
        for e in range(epochs):
            lr, sigma = self._decay(self.lr0, e, epochs), self._decay(self.sigma0, e, epochs)
            for x, yv in zip(X, y):
                bmu = self._bmu(x)
                h = self._neigh(bmu, sigma)[:, None]
                self.weights += lr * h * (x - self.weights)
                self.label_weights += lr * h * (yv - self.label_weights)
            self.hist.append(accuracy_score(np.argmax(y,1), self.predict(X)))

    def predict(self, X):
        return [np.argmax(self.label_weights[self._bmu(x)]) for x in X]



iris = datasets.load_iris()
X, y = iris.data, iris.target
X = StandardScaler().fit_transform(X)

oh = OneHotEncoder(sparse_output=False)
y_oh = oh.fit_transform(y.reshape(-1,1))

Xtr, Xte, ytr, yte = train_test_split(X, y_oh, test_size=0.3, random_state=42, stratify=y)

som = SSOM(6, 6, input_dim=X.shape[1], n_classes=3, lr=0.5)
som.fit(Xtr, ytr, epochs=60)
ypred = som.predict(Xte)

print("Test accuracy:", accuracy_score(np.argmax(yte,1), ypred))

plt.plot(som.hist)
plt.xlabel("Epoch"); plt.ylabel("Train accuracy"); plt.title("SSOM training accuracy")
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
def plot_decision_boundary(clf, X, y, title):
    h = .02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
    np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='k')
    plt.title(title)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.tight_layout()
X_nonlin, y_nonlin = make_moons(n_samples=100, noise=0.2, random_state=1)
models_nonlin = [
("RBF Kernel, C=1", make_pipeline(StandardScaler(), SVC(kernel="rbf", C=1))),
("RBF Kernel, C=100", make_pipeline(StandardScaler(), SVC(kernel="rbf", C=100)))
]
plt.figure(figsize=(10, 4))
for i, (name, model) in enumerate(models_nonlin):
    model.fit(X_nonlin, y_nonlin)
    plt.subplot(1, 2, i + 1)
    plot_decision_boundary(model, X_nonlin, y_nonlin, name)
plt.tight_layout()
plt.show()
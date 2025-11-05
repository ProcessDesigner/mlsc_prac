import numpy as np
import pandas as pd

# Load dataset
data = pd.read_csv('Admission_Predict.csv')
X = data.values

# Step 1: Mean centering
X_meaned = X - np.mean(X, axis=0)

# Step 2: Covariance matrix
cov_mat = np.cov(X_meaned, rowvar=False)

# Step 3: Eigen decomposition
eigen_values, eigen_vectors = np.linalg.eigh(cov_mat)

# Step 4: Sort eigenvalues and eigenvectors
sorted_index = np.argsort(eigen_values)[::-1]
sorted_eigenvalues = eigen_values[sorted_index]
sorted_eigenvectors = eigen_vectors[:, sorted_index]

# Step 5: Choose number of components
n_components = 2
eigenvector_subset = sorted_eigenvectors[:, :n_components]

# Step 6: Transform data
X_reduced = np.dot(X_meaned, eigenvector_subset)

print("Covariance Matrix:\n", cov_mat)
print("\nEigenvalues:\n", sorted_eigenvalues)
print("\nEigenvectors:\n", sorted_eigenvectors)
print("\nReduced Data (first 5 rows):\n", X_reduced[:5])

import numpy as np

class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.mean = None
        self.std_dev = None
        self.projection_matrix = None

    def fit(self, X):
        # 1. Standardize the Data
        self.mean = np.mean(X, axis=0)
        self.std_dev = np.std(X, axis=0)
        X_scaled = (X - self.mean) / self.std_dev

        # 2. Calculate the Covariance Matrix
        covariance_matrix = np.cov(X_scaled, rowvar=False)

        # 3. Compute Eigenvalues and Eigenvectors
        eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

        # 4. Sort Eigenvectors by Eigenvalues
        sorted_indices = np.argsort(eigenvalues)[::-1]
        sorted_eigenvectors = eigenvectors[:, sorted_indices]

        # 5. Select Principal Components
        self.projection_matrix = sorted_eigenvectors[:, :self.n_components]

    def transform(self, X):
        # Standardize new data using the mean and std_dev from fitting
        X_scaled = (X - self.mean) / self.std_dev
        # 6. Transform the Data
        transformed_data = np.dot(X_scaled, self.projection_matrix)
        return transformed_data

# Example Usage:
# from sklearn.datasets import load_iris
# iris = load_iris()
# X = iris.data

# pca = PCA(n_components=2)
# pca.fit(X)
# X_transformed = pca.transform(X)
# print(X_transformed.shape) # (150, 2)
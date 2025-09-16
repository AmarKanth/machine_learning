import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

class SimpleXGBoost:
    def __init__(self, n_estimators=10, learning_rate=0.1, max_depth=3):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.trees = []
        self.initial_prediction = None

    def fit(self, X, y):
        # Initial prediction (e.g., mean of y for regression)
        self.initial_prediction = np.mean(y)
        current_predictions = np.full_like(y, self.initial_prediction, dtype=float)

        for _ in range(self.n_estimators):
            # Calculate residuals (negative gradients for squared error)
            residuals = y - current_predictions

            # Train a new tree on the residuals
            tree = DecisionTreeRegressor(max_depth=self.max_depth)
            tree.fit(X, residuals)
            self.trees.append(tree)

            # Update predictions
            tree_predictions = tree.predict(X)
            current_predictions += self.learning_rate * tree_predictions

    def predict(self, X):
        predictions = np.full(X.shape[0], self.initial_prediction, dtype=float)
        for tree in self.trees:
            predictions += self.learning_rate * tree.predict(X)
        return predictions

if __name__ == "__main__":
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    y = np.array([10, 20, 30, 40, 50])

    model = SimpleXGBoost(n_estimators=5, learning_rate=0.2, max_depth=1)
    model.fit(X, y)
    predictions = model.predict(X)

    print(f"True values: {y}")
    print(f"Predictions: {predictions}")
    print(f"MSE: {mean_squared_error(y, predictions)}")
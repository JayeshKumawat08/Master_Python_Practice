import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class CustomLinearRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.lr = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.iterations):
            y_predicted = np.dot(X, self.weights) + self.bias
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)
            
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

if __name__ == "__main__":
    # Generating the dataset
    np.random.seed(42)
    X_raw = np.random.rand(100, 1) * 10
    y_raw = 5 * X_raw.flatten() + 10 + np.random.randn(100) * 2
    X_train, X_test, y_train, y_test = train_test_split(X_raw, y_raw, test_size=0.2, random_state=4)

    # Test 1: The Optimal Rate (0.05)
    print("--- Testing Learning Rate: 0.05 ---")
    model_optimal = CustomLinearRegression(learning_rate=0.05, iterations=1000)
    model_optimal.fit(X_train, y_train)
    mse_optimal = mean_squared_error(y_test, model_optimal.predict(X_test))
    print(f"Final Weights: {model_optimal.weights[0]:.2f}")
    print(f"MSE: {mse_optimal:.4f}")

    # Test 2: The Micro-Step Rate (0.001)
    print("\n--- Testing Learning Rate: 0.001 ---")
    model_slow = CustomLinearRegression(learning_rate=0.001, iterations=1000)
    model_slow.fit(X_train, y_train)
    mse_slow = mean_squared_error(y_test, model_slow.predict(X_test))
    print(f"Final Weights: {model_slow.weights[0]:.2f}")
    print(f"MSE: {mse_slow:.4f}")
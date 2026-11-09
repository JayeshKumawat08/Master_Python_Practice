import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 1. Manually engineering the Gradient Descent engine 
class CustomLinearRegression:
    def __init__(self, learning_rate=0.9, iterations=1000):
        # Hyperparameters for our SGD engine
        self.lr = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        # We need to know the dimensions of our data to build the math matrices
        n_samples, n_features = X.shape
        
        # Initialize our starting parameters (Weight = 0, Bias = 0)
        self.weights = np.zeros(n_features)
        self.bias = 0

        # The core Loop for Gradient Descent
        for _ in range(self.iterations):
            # The mathematical prediction formula: y_pred = X*w + b
            y_predicted = np.dot(X, self.weights) + self.bias
            
            # Calculate the derivative of the error function (The Gradients)
            # This tells the algorithm which direction to step to reduce the error
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)
            
            # Update weights and bias (taking a step down the gradient)
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

# 2. Testing our custom engine
if __name__ == "__main__":
    print("--- Initiating Custom Gradient Descent Engine ---")
    
    # Simulating standard dataset: 100 students, X = study hours, y = exam score
    np.random.seed(42)
    # Generate 100 random study hours between 1 and 10
    X_raw = np.random.rand(100, 1) * 10
    # Simulate scores with a perfect linear relationship + some random noise
    y_raw = 5 * X_raw.flatten() + 10 + np.random.randn(100) * 2

    # Split the data to test accuracy (Module 4)
    X_train, X_test, y_train, y_test = train_test_split(X_raw, y_raw, test_size=0.2, random_state=4)

    # Initialize and train our manual ML model
    print("Training custom model (calculating derivatives)...")
    model = CustomLinearRegression(learning_rate=0.01, iterations=1000)
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)
    
    # Evaluate performance
    mse = mean_squared_error(y_test, predictions)
    
    print("\n✅ Training Complete.")
    print(f"Final Weights (Slope): {model.weights[0]:.2f}")
    print(f"Final Bias (Intercept): {model.bias:.2f}")
    print(f"Model MSE on unseen data: {mse:.4f}")
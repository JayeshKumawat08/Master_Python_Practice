import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error

class realEstate:
    def __init__(self):
        self.data = pd.DataFrame({
            'Square_Feet': [1000, 1500, np.nan, 2500, 3000, np.nan, 4000],
            'Price': [300000, 450000, 600000, 750000, 900000, 1050000, 1200000]
        })

    def run_pipeline(self):
        print("--- Starting Robust ML Workflow ---")
        
        X_raw = self.data[['Square_Feet']] 
        y = self.data['Price']
        
        print(f"Missing Values Before Imputation:\n{X_raw.isnull().sum()}")
        
        print("\nDeploying SimpleImputer (Strategy: Mean)...")
        imputer = SimpleImputer(strategy='mean')
        
        X_cleaned = imputer.fit_transform(X_raw)
        
        X_train, X_test, y_train, y_test = train_test_split(X_cleaned, y, test_size=0.2, random_state=42)
        
        print("Training Linear Regression Engine...")
        model = LinearRegression()
        model.fit(X_train, y_train) 
        
        print("Evaluating Model on Hidden Test Data...")
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        
        print("\n Execution Complete.")
        print(f"Mean Squared Error: {mse}")

if __name__ == "__main__":
    engine = realEstate()
    engine.run_pipeline()
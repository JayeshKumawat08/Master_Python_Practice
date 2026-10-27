import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class RealEstateModel:
    def __init__(self):
        self.data = pd.DataFrame({
            'Square_Feet': [1000, 1500, 2000, 2500, 3000, 3500, 4000],
            'Price': [300000, 450000, 600000, 750000, 900000, 1050000, 1200000]
        })
    def run_pipeline(self):

        print("Starting ML Workflow")

        X = self.data[['Square_Feet']]
        y = self.data['Price']

        X_train, X_test, y_train,y_test = train_test_split(X,y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train,y_train)

        prediction = model.predict(X_test)

        mse = mean_squared_error(y_test,prediction)

        print(f"Test Set True Prices: {y_test.values}")
        print(f"Model Predictions:    {prediction}")
        print(f"Mean Squared Error:   {mse}")

if __name__ == "__main__":
    engine = RealEstateModel()
    engine.run_pipeline()
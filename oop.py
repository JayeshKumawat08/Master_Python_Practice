import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class python_Pipeline:
    def __init__(self):

        self.imputer = SimpleImputer(strategy='mean')
        self.encoder = LabelEncoder()
        self.model = KNeighborsClassifier(n_neighbors=3)

    def load_data(self):
        df = pd.DataFrame({
            'Satisfaction': [4.5, 3.2, np.nan, 2.1, 4.8, 3.9, np.nan, 1.5],
            'Department': ['IT', 'HR', 'IT', 'Sales', 'HR', 'IT', 'Sales', 'HR'],
            'Will_Leave': [0, 1, 0, 1, 0, 0, 1, 1]  # Target: 0 = Stay, 1 = Leave
        })
        return df

    def preprocess_data(self, df):
        print("Preprocessing process started....")

        df['Satisfaction'] = self.imputer.fit_transform(df['Satisfaction'].values.reshape(-1,1))
        df['Department_Encoded'] = self.encoder.fit_transform(df["Department"])

        X = df[['Satisfaction', 'Department_Encoded']]
        y = df['Will_Leave']
        return X,y

    def split_data(self,X, y):
        print("Training and Splitting")
        return train_test_split(X,y,test_size=0.25,random_state=42)

    def train_model(self, X_train, y_train):
        print("Training K nearest neighbors pred engine")
        self.model.fit(X_train,y_train)

    def eval_model(self, X_test, y_test):
        print("Evaluating model performance on hidden test data")
        prediction = self.model.predict(X_test)
        accuracy = accuracy_score(y_test,prediction)

        print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
        print(f"True Outcomes: {y_test.values}")
        print(f"Predictions:   {prediction}")

    def execute_workflow(self):
        print("ML Pipeline")

        df = self.load_data()
        X, y = self.preprocess_data(df)
        X_train, X_test, y_train, y_test = self.split_data(X,y)
        self.train_model(X_train, y_train)
        self.eval_model(X_test, y_test)

if __name__ == "__main__":
    pipeline = python_Pipeline()
    pipeline.execute_workflow()

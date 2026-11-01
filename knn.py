import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class LoanApprovalEngine:
    def __init__(self):
        
        self.data = pd.DataFrame({
            'Income': [40000, 80000, 30000, 120000, 50000, 150000, 45000],
            'Credit_Tier': ['Poor', 'Good', 'Poor', 'Excellent', 'Good', 'Excellent', 'Poor'],
            'Loan_Status': ['Rejected', 'Approved', 'Rejected', 'Approved', 'Approved', 'Approved', 'Rejected']
        })

    def pipeline(self):
        print("Starting KNN Classification Workflow ")

        print("Encoding ordinal text data into mathematics.")
        encoder = LabelEncoder()

        self.data["Credit_Tier_Encoded"] = encoder.fit_transform(self.data["Credit_Tier"])
        print(f"Encoded Mapping:\n{self.data[['Credit_Tier', 'Credit_Tier_Encoded']].head(3)}\n")

        X = self.data[['Income', 'Credit_Tier_Encoded']] 
        y = self.data['Loan_Status']

        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

        print("Training K-Nearest Neighbors (KNN) Classifier...")
        model = KNeighborsClassifier(n_neighbors=3)
        model.fit(X_train,y_train)

        print("Evaluating Model on Hidden Test Data...")
        prediction = model.predict(X_test)
        accuracy = accuracy_score(y_test,prediction)

        print('-'*40)
        print(f"Test Set True Status: {y_test.values}")
        print(f"Model Predictions:    {prediction}")
        print(f"Accuracy Score:       {accuracy * 100}%")


if __name__ == "__main__":
    engine = LoanApprovalEngine()
    engine.pipeline()

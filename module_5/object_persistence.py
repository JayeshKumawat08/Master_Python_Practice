import pickle
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

class PersistenceEngine:
    def __init__(self):
        self.filename = "saved_knn_model.pkl"
        
    def train_and_freeze(self):
        print("1. Training new KNN Model...")

        # Dummy data: [Study_Hours, Attendance] -> [0 = Fail, 1 = Pass]
        X = np.array([[2, 50], [8, 90], [7, 85], [1, 40]])
        y = np.array([0, 1, 1, 0])
        
        model = KNeighborsClassifier(n_neighbors=3)
        model.fit(X, y)
        
        print("2. Serializing (Pickling) the model to hard drive...")

        with open(self.filename, 'wb') as file:
            pickle.dump(model, file)
            
        print(f"Model successfully frozen into '{self.filename}'\n")

    def resurrect_and_predict(self):
        print("3. System Rebooted. Loading frozen model from hard drive...")

        with open(self.filename, 'rb') as file:
            restored_model = pickle.load(file)
            
        print("4. Predicting new data using restored model...")

        new_student = np.array([[9, 95]])
        prediction = restored_model.predict(new_student)
        
        result = "Pass" if prediction[0] == 1 else "Fail"
        print(f"Prediction Complete: The student will {result}.")

if __name__ == "__main__":
    engine = PersistenceEngine()
    
    engine.train_and_freeze()
    engine.resurrect_and_predict()
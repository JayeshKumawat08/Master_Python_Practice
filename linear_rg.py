import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#database
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1,1)
marks = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

X_train, X_test, y_train,y_test = train_test_split(hours,marks,test_size=0.2,random_state=42)

#train
model = LinearRegression()
model.fit(X_train,y_train)

#prediction
y_pred = model.predict(X_test)

print("Actual Marks:", y_test)
print("Predicted Marks:", y_pred)

#eval
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print("Mean Squared Error:", mse)
print("R2 Score:", r2)

#predict for new study hours
new_hours = np.array([[7]])
prediction = model.predict(new_hours)
print("Predicted marks for 7 hours:", prediction[0])
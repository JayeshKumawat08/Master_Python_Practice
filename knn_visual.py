import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.neighbors import KNeighborsClassifier

class StudentManagementKNN:
    def __init__(self):
        # 1. Loading the Student Data
        # X: [Study_Hours, Attendance_Percentage]
        self.X = np.array([
            [2, 50], [3, 60], [1, 40], [4, 55], # Mostly Failing profiles
            [8, 90], [7, 85], [9, 95], [6, 80], # Mostly Passing profiles
            [5, 70], [4, 75], [7, 60], [3, 90]  # Borderline profiles
        ])
        # y: 0 = Fail (Red), 1 = Pass (Green)
        self.y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0])

    def plot_decision_boundary(self):
        print("Training KNN and generating spatial boundaries...")
        
        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(self.X, self.y)

        # Create the Mesh Grid (The canvas for the background colors)
        # find the min and max limits of the data, and stretch the grid slightly beyond them
        x_min, x_max = self.X[:, 0].min() - 1, self.X[:, 0].max() + 1
        y_min, y_max = self.X[:, 1].min() - 5, self.X[:, 1].max() + 5
        
        # np.meshgrid creates thousands of tiny coordinates across the graph
        xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                             np.arange(y_min, y_max, 1.0))

        # 4. Ask KNN to predict the outcome for EVERY coordinate on the grid
        Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        plt.figure(figsize=(10, 6))
        
        # background color based on the KNN predictions (Red zone vs Green zone)
        custom_cmap = ListedColormap(['#ff9999', '#99ff99'])
        plt.contourf(xx, yy, Z, alpha=0.4, cmap=custom_cmap)

        # Plot actual student data points on top
        scatter = plt.scatter(self.X[:, 0], self.X[:, 1], c=self.y, 
                              cmap=ListedColormap(['red', 'green']), 
                              edgecolor='black', s=100)

        plt.title("KNN Decision Boundaries: Student Pass/Fail Prediction (K=3)", fontsize=14, fontweight='bold', pad=15)
        plt.xlabel("Weekly Study Hours", fontsize=12, fontweight='bold')
        plt.ylabel("Attendance Percentage (%)", fontsize=12, fontweight='bold')
        
        plt.legend(handles=scatter.legend_elements()[0], labels=['Fail', 'Pass'], loc='lower right')
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    management_system = StudentManagementKNN()
    management_system.plot_decision_boundary()
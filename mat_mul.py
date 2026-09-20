import pandas as pd
import numpy as np  

candidates = pd.DataFrame({
    "Math":[80,60,90],
    "Coding":[70,95,85],
    "Logic":[90,80,88]
},index=["Amit","Priya","Rahul"])

print("Candidate Matrix(X)")
print(candidates)

weights = np.array([0.3,0.5,0.2])

final_score = candidates @ weights

print("Final AI Suitability Score")
print(final_score)
import pandas as pd

student_dict = {
    "Roll_No":[101,102,103,104],
    "Name":["Amit", "Priya", "Rahul", "Sneha"],
    "Department": ["CS", "IT", "CS", "Mechanical"],
    "Marks": [85, 92, 78, 88]
}

df = pd.DataFrame(student_dict)

print("Student Data Table")
print(df)














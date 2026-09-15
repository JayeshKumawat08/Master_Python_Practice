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

top_students = df[df["Marks"]>85]
print(f"The Top Student who  has more than 85 marks are:\n {top_students}")
print("-"*40)

#postion based selectionn according to the index
first_student = df.iloc[1:3]
print(first_student)

#extractinng buy lables using loc function
print("-"*40)
name_and_marks = df.loc[:,["Name","Marks"]]
print(name_and_marks)











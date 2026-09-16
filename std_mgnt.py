import pandas as pd
import os

def university_system():
    df = None
    while True:
        print("University Dataset")
        print("1.Load and Inspect data")
        print("2.Clean the dataset (Imputation)")
        print("3.Find Top Performer (Filter)")
        print("4.Department Analysis (Groupby)")
        print("5.Exit")
        print()

        choice = input("Enter Your Choice: ").strip()

        if choice == '1':
            if os.path.exists("students.csv"):
                df = pd.read_csv("students.csv")
                print(f"Total Records: {df.shape[0]} rows, {df.shape} columns")
                print()
                print("First 3 Rows")
                print(df.head(3))
            else:
                print("Not found CSV")

        elif choice == '2':
            if df is None:
                print("load the dataset first")
            else:
                marks_avg = df["Marks"].mean()
                att_avg = df["Attendance_Pct"].mean()

                df["Marks"] = df["Marks"].fillna(marks_avg)
                df["Attendence_Pct"] = df["Attendance_Pct"].fillna(att_avg)

                print("Missing value successfully resolved")

        elif choice == '3':
            if df is None:
                print("Load the Dataset")
            else:
                min_marks = float(input("Enter minimum marks threshold: "))
                min_att = float(input("Enter minimum attendence threshold: "))

                top_students = df[(df["Marks"]>= min_marks) & (df["Attendance_Pct"]>= min_att)]

                print("\nTop Performers")
                print(top_students.loc[:,["Name","Department"]])


        elif choice == '4':
            if df is None:
                print("Dataset not loaded")
            else:
                print("\nDepartmnet Analysis")
                dept_report = df.groupby("Department")["Marks"].mean()
                print(dept_report)

        elif choice == '5':
            print("\nShutting down the system")
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    university_system()

class StudentManager:
    def __init__(self,filename):
        self.filename = filename

    def add_student(self,reg_no,name,marks):
        with open(self.filename,'a') as file:
            file.write(f"{reg_no},{name},{marks}")
            print(f"Student {name} is added into the file.\n")

    def show_top_student(self):
        print("Student with more than 75 marks\n")
        with open(self.filename,'r') as file:
            lines = file.readlines()

            if not lines:
                print("the current file is empty.")
                return
            for line in lines:
                details = line.strip().split(',')

                if len(details) == 3:
                    reg_no = details[0]
                    name = details[1]
                    marks = int(details[2])

                    if marks > 75:
                        print(f"Reg No.: {reg_no}| Name: {name}, Marks: {marks}")

def run_student_system():
    manager = StudentManager("student.txt")

    while True:
        print()
        print("STUDENT RECORD MANAGER")
        print("1. Add New Student")
        print("2. Display Students (> 75 Marks)")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            reg = input("Enter the Reg No.: ").strip()
            name = input("Enter your Name: ").strip()
            mark = input("Enter your Marks: ").strip()
            manager.add_student(reg,name,mark)

        elif choice == '2':
            manager.show_top_student()

        elif choice == '3':
            print("Exiting the file.  Bye!!")
            break 
        else:
            print("Invalidd  choice entered")

if __name__ == "__main__":
    run_student_system()

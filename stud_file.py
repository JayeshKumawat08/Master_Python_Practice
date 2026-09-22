class StudentFileHandler:
    def __init__(self,filename):
        self.filename = filename

    def save_student(self,roll_no,name,marks):

        with open(self.filename,'a') as file:
            file.write(f"{roll_no},{name},{marks}\n")
        print(f"Data Saved with name as {name}")

    def load_students(self):
        print("Reading Data from File\n")

        with open(self.filename,'r') as file:
            for line in file:
                data = line.strip().split(',')
                print(f"Roll No: {data[0]}| Name: {data[1]}| Marks: {data[2]}")

def run_basic_file_system():

    my_file = 'student_db.txt'
    handler = StudentFileHandler(my_file)

    while True:
        print()
        print("1.Add a Student Record")
        print("2.Read all records")
        print("3.Exit")

        choice = input("Enter your Choice: ").strip()

        if choice == '1':
            roll = input("Enter your Roll No.: ").strip()
            name = input("Enter your Name: ").strip()
            marks = input("Enter your Marks: ").strip()
            handler.save_student(roll,name,marks)

        elif choice == '2':

            handler.load_students()

        elif choice == '3':
            print()
            print("exiting the file")
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    run_basic_file_system()

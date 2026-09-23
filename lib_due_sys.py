import pandas as pd

def run_library_due_system():

    records = []

    while True:
        print()
        print("Library Due Managemnet System")
        print("1. Add a member")
        print("2.Due more the 1 Month")
        print("3.Exit")

        choice = input("Enter the Choice: ").strip()

        if choice == '1':
            user_id = input("Enter User Id: ").strip()
            name = input("Enter User Name: ").strip()
            fine_number = float(input("Enter Fine Amount in Rs.: ").strip())
            due_months = int(input("Enter the Due Months: ").strip())

            records.append({
                "ID":user_id,
                "Name": name,
                "Fine_Amount": fine_number,
                "Due_Months": due_months
            })
            print(f"Records added for {name} Successfully")

        elif choice == '2':
            if not records:
                print("No record found . add records")
            else:
                df = pd.DataFrame(records)

                defaulters = df.loc[df["Due_Months"]>1,["ID","Name","Fine_Amount"]]
                if defaulters.empty:
                    print("no members have dues more than 1 month")
                else:
                    print("Members Having Dues more than 1 Months----")
                    print(defaulters)

        elif choice == '3':
            print("Exiting the System")
            break
        else:
            print("Invalid choice selected")

if __name__ == "__main__":
    run_library_due_system()

                

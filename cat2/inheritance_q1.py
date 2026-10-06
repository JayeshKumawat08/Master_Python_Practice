class Employee():
    def __init__(self,emp_id,name):
        self.emp_id = emp_id
        self.name = name

class Developer(Employee):
    def __init__(self,emp_id,name,basic_sal,lang):
        super().__init__(emp_id,name)
        self.basic_sal = basic_sal
        self.lang = lang

class SeniorDeveloper(Developer):
    def __init__(self,emp_id,name,basic_sal,lang,years_exp,project_allowance):
        super().__init__(self,emp_id,name, basic_sal,lang)
        self.years_exp =  years_exp
        self.project_allowance = project_allowance

    def calculate_salary(self):
        gross_sal = self.basic_sal + self.project_allowance

        if self.years_exp >= 10:
            bonus = 0.20 * gross_sal
        elif self.years_exp >= 5:
            bonus = 0.10 * gross_sal
        else:
            bonus = 0
        final_sal = gross_sal + bonus

    def display(self):
        gross, bonus, final = self.calculate_salary()

        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Language:", self.lang)
        print("Experience:", self.years_exp)
        print("Gross Salary:", gross)
        print("Experience Bonus:", bonus)
        print("Final Salary:", final)

s1 = SeniorDeveloper(
    101, "Rahul", 60000, "Python", 12, 8000
)

s2 = SeniorDeveloper(
    102, "Aman", 50000, "Java", 7, 5000
)

s1.display()
s2.display()
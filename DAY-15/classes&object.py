class Employees:
    #constructor
    def __init__(self,name,email,dept,salary):
        self.name=name
        self.email=email
        self.dept=dept
        self.salary=salary

    def emp_info(self):
        print(f'Name is {self.name}')
        print(f'email is {self.email}')
        print(f'department is {self.dept}')
        print(f'salary is {self.salary}')
        

emp1=Employees('raju','raju@email.com','sales', 50000)

emp1.emp_info()
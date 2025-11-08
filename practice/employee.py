class Employee:
    def __init__(self,id,n,sal):
        self.empid=id
        self.name=n
        self.salary=sal

    def details(self):
        print("Employee_id : ",self.empid)
        print("Employee name: ",self.name)
        print("Employee salary: ",self.salary)
    
    def apply(self,percent):
        newsalary = self.salary+(self.salary*percent)/100
        self.salary+=newsalary
        print(percent,"is raise. New salary :",self.salary)
    
emp=Employee(1,"John",4000)
emp.details()
emp.apply(50)
emp.details()



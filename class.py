class Employee:
    company ="tutorial gate way"

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def func_message(self):
        print("welcome to python programming")


emp1=Employee('hari vardhan reddy','24','male')
print(emp1.company)
emp1.func_message()
print(emp1.name)
print(emp1.age)
print(emp1.gender)


    
emp2=Employee('dharani  ','24','female')
print(emp2.company)
emp1.func_message()
print(emp2.name)
print(emp2.age)
print(emp2.gender)


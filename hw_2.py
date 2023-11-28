class Person:
    def __init__(self,fullname,age,is_married):
     self.fullname=fullname
     self.age=age
     self.is_married=is_married
    def introduce_myself (self):
     print(f"ФИО {self.fullname},Возраст- {self.age}, Статус - {self.is_married}")
     
self1=Person("Tairova Darika",23,"married")   
self1.introduce_myself()

   
class Teacher(Person):
    def __init__(self,fullname,age,is_married,experiance,salary):
         Person. __init__(self,fullname,age,is_married)
         self.experiance = experiance
         self.salary=salary

    def count (self):
       for i in range(self.experiance):
        self.salary += 3000
        print(f" Name -{self.fullname} ,Salary is {self.salary}")

result = Teacher("Darika",23,"married",3,50000)
result.introduce_myself()
result.count()
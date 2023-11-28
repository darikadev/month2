class GeeksPeople():
    def __init__(self,name,email,phone):
        self.name= name 
        self.email= email
        self.phone=phone
    def __str__(self):
        return f"{self.name},{self.email},{self.phone}"
    


class Student(GeeksPeople):
    def __init__(self,name,email,phone,student_id,group_where_study):
     GeeksPeople.__init__(self,name,email,phone)
     self.student_id = student_id
     self.group_where_study = group_where_study
     
    def study(self): 
     print(f" Обучается в группе - {self.group_where_study}")
    def info(self):
       print(f" Имя - Darika","email - darikatairova0310@gmail.com", "Phone -706022812","Darika Backend id","group 13-3B")
darika = Student(f"Darika","darikatairova0310@gmail.com",706022812,"Darika Backend id","group 13-3B")
darika.info()      
darika.study()    

class Teacher(GeeksPeople):
   def __init__(self,name,email,phone,teacher_id,group_where_teach):
    GeeksPeople.__init__(self,name,email,phone)
    self.teacher_id = teacher_id
    self.group_where_teach = group_where_teach
   def info(self):
          print(f"name - Syimyk","email - syimyk@mail.com","phone -556596825","id is - Backend","Group - 13-3-B")
   def teach(self):
       print(f"Обучает группу - {self.group_where_teach}")
syimyk = Teacher(f"Syimyk","syimyk@email.com","556596825","Backend","13-3-B")
syimyk.info()
syimyk.teach()

class Admin(GeeksPeople):
   def __init__(self,name,email,phone,admin_id):
      GeeksPeople.__init__(self,name,email,phone)
      self.admin_id = admin_id
   def info(self):
      print(f"name - Beksultan","email - beksultan@email.com",5563196496,"Id_Administrator")
   def create_group(self):
      group = input("Text new group")
      print(group)
beksultan = Admin("Beksultan","beksultan@mail.com",5563196469,"Id_administrtor") 
beksultan.info()
beksultan.create_group()

class Mentor(Student,Teacher):
   def __init__(self,name,email,phone,student_id,group_where_study,teacher_id,group_where_teach):
       Student.__init__(self,name,email,phone,student_id,group_where_study)
       Teacher.__init__(self,name,email,phone,teacher_id,group_where_teach)
   def info (self):
      print((f" name - Kudbuhon","email - kudbuhonb@email.com",6445621456,"student_id - kudbuhon_student","group_study - backend9-3","teacher_kudbuhon","13-3B"))
   
   def study(self): 
     print(f" Обучается в группе - {self.group_where_study}")
   def teach(self):
       print(f"Обучает группу - {self.group_where_teach}")
kudbuhon = Mentor(f"Kudbuhon","kudbuhonb@email.com",6445621456,"kudbuhon_student","backend9-3","teacher_kudbuhon","13-3B")
kudbuhon.info()    
kudbuhon.study()
kudbuhon.teach()
    

class Fruits:
   def __init__ (self,name,color,taste):
      self.name= name
      self.color=color
      self.taste=taste
   def info_f(self):
      print(f" Название фрукта - {self.name},Цвет- {self.color}, Вкус - {self.taste}")
      
class malina(Fruits) :
     def __init__(self,name,color,taste):
      Fruits. __init__ (self,name,color,taste)
     def action(self):
      print("Soft1")
class apple1(Fruits):
   def __init__(self,name,color,taste):
      Fruits. __init__ (self,name,color,taste)
   def action(self):
      print("hard")

class banana(Fruits):
   def __init__(self,name,color,taste):
      Fruits. __init__ (self,name,color,taste)

   def action(self):
      print("Soft")
   

apple = Fruits("Strawberry","Red",'Tasty')
apple.info_f()
malina=malina("Malina",'pink','Tasty')
apple=apple1("Apple","green",'Tasty')
banana=banana("Banana","Yellow","Tasty")
malina.action()
apple.action()
banana.action()
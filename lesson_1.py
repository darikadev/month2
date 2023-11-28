# #ООП - Обьектно Ориентированное Програмирование
# #DRY - Don't repeat yourself == не повторяйся
# class Car:
#     #class - чертеж,инструкция
#     def __init__(self,model,color):
#         # self.model= model=model -Атрибут обьекта
#         self.color=color
#         self.year=2023
#         wheels = 4 #Атрибут класса
#     # pass- пропустить
#     #self - сам обьект 
#     #____init___ =- конструктор
     
# mersedes = Car("cls","black",)
# mersedes.info()
# mersedes.drive("Ош",200)


# # print(mersedes.model)
# # print(mersedes.color)
# # print(mersedes.year)

def info(self):
 print(f"Бренд машины - {self.model},Цвет - {self.color},Год{self.year}")





# def drive(self,location,speed):
#    print("машина едет в {location} со скоростью {speed}км/ч")





class Airplane:
      def ___init___(self , model,year,color,capacity,max_speed,):
       self.model=model
       self.year=year
       self.color=color
       self.capacity= capacity
       self.max_speed= max_speed
       self.is_flying= False
       self.odometer = 0
      def info_about_airplane(self):
          print(f"{self.model},{self.year}Года выпуска,Цвет{self.color},{self.capacity},{self.max_speed}")
      def take_of(self):
          self.is_flying = True
          print("Самолет взлетел")

plane =Airplane("MI-38",1992,"black",3,450)
plane.info_about_airplane()
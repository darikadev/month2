#Задание 1
# class Fruits:
#     def __init__ (self,name,color,weight):

#         self.name=name
#         self.color=color
#         self.taste="sweet"
#         self.weight=weight

#     def info(self):
#        print(f"Название фрукта - {self.name}, Цвет - {self.color},Вес - {self.weight} , Вкус - {self.taste}")       
    
# fruit1 = Fruits("Apple","red","30gr")
# fruit2=Fruits("Strawberry","red","10gr")
# fruit3=Fruits("Watermelon","green","1.5 kg")
# fruit1.info()
# fruit2.info()
# fruit3.info()



#Задание 2 - Доп задание

# class Book:
#     def __init__ (self,title,author,pages,current_page):
#      self.title=title
#      self.author=author
#      self.pages=pages
        
#      if self.pages < 100:
#       return "Книга тонкая"
#      elif 100 <= self.pages <= 300:
#        return "Эта книга средней толщины."
#      else:
#          return "Эта книга толстая."
     
    
# def turn_page(self, page_number):
#         if 1 <= page_number <= self.pages:
#             self.current_page = page_number
#             print(f"Вы на странице {self.current_page}.")
#         else:
#             print("Эта страница не существует в книге.")

# book = Book("книга", "автор", 500)
# print(book.check_pages())

# book.turn_page(21)
# book1= Book(f"Унесенные ветром","Сара Джио",250)
# print(book1.check_pages())

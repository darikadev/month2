class Computer:
    def __init__(self,cpu,memory,make_computations):
       self.__cpu = cpu
       self.__memory = memory
       self.__make_computations = make_computations

    @property
    def cpu(self):
        return self.__cpu
    
    @property
    def memory(self):
        return self.__memory
    
    @property
    def make_computations(self):
        print(f"Результат : {self.__cpu + self.__memory}")
        print(f"Результат :{self.__cpu - self.__memory}")
        print(f"Результат :{self.__cpu  * self.__memory}")
        print(f"Результат:{self.__cpu  / self.__memory}")
        return self.__make_computations
        
number=Computer(15,10, "Результат")
number.make_computations

class Laptop(Computer):
    def __init__(self,cpu, memory, make_computations ,memory_card):
        super().__init__(cpu, memory, make_computations)
        self.__memory_card = memory_card
          
    @property
    def memory_card(self):
        return self.__memory_card
    @memory_card.setter
    def memory(self, mem_cord):
        self.memory_card == mem_cord
    
    def info (self):
        print(f"АДР: {self.cpu}, Памать:{self.memory_card}гб")
object = Laptop(3,32,"Result",64)
object.info()
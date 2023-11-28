class Computer:
    def init (self,cpu,memory, ):
       self.__cpu = cpu
       self.__memory = memory
    @property
    def cpu(self):
        return self.__cpu
    

    @property
    def memory(self):
        return self.__memory
    

    
    def __make_computations (self):
        print(f"Result - {self.__cpu + self.__memory}")
        print(f"Result -{self.__cpu - self.__memory}")
        print(f"Result - {self.__cpu  * self.__memory}")
    @property
    def make_commputations(self):
        return self.__make_computations

result=Computer(15,10)
result.__make_computations()

class Laptop (Computer):
    def __init (self,cpu,memory, make_computations,memory_card):
     Computer.__init(self,cpu,memory)
     self.__memory_card = memory_card
          
    @property
    def memory_card(self):
        return self.__memory_card
  
    def info (self):
        print(f"{self.cpu},Память - {self.memory},{self.memory_card}")
memory_card = (256,"Gb")
object = Laptop(15,10, "Memory card - 256 Gb")
object.info()


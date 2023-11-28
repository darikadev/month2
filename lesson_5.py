class Phone:
    def __init__(self,battery):
        self.battery = battery
        #магические методы для арифметических действий
    def __str__(self):
        return f"Емкость баттареи {self.battery}"
    def __add__(self,other):
        new_battery = self.battery + other.battery
        return Phone(new_battery)
 
phone = Phone(2000)
phone_2 = Phone(3000)
print (phone + phone_2)
print(phone)
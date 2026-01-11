class Car:
    def __init__(self, name, color, power):
        self.name = name
        self.color = color
        self.power = power
        self.mileage = 0
        self.is_running = False

    def printInfo(self):
        print("="*10)
        print(f"Название машины: {self.name}")
        print(f"Цвет: {self.color}")
        print(f"Мощность: {self.power}")
        print(f"Машина:{self.is_running}")
        print(f"Пробег машины {self.mileage}")

        print("="*10)
    
    def start_engine(self):
        if self.is_running:
            print("Двигатель уже запущен!")
            return #точка выхода из функции
        self.is_running = True
        print("Двигатель заведен")


# class Cat:
#     def __init__(self, breed, color, name):
#         self.breed = breed
#         self.color = color
#         self.name = name
    
#     def catsay(self):
#         print("Мяу")
        
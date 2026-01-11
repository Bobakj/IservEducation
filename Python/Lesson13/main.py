from car import *


# car1 = Car("Lada Granta", "Черный", 200)
# car2 = Car("Kia K5", "Белый", 500)

# car1.printInfo()
# car2.printInfo()
# name = car2.name
# print(name)

# car2.power = 200

# car2.color = "Черный"
# car2.printInfo()

# cat1 = Cat("Сиамская", "Рыжий", "Муся")
# cat2 = Cat("Манечкин", "Белый", "Беляш")

# cat1.catsay()
# cat2.catsay()
car1 = Car("Audi R8", "Белый", 800)
car1.printInfo()

name = getattr(car1, "name")
print(name)

setattr(car1, "color", "Черный")
car1.start_engine()
car1.start_engine()
car1.printInfo()
# Урок 4 
## Циклы
```
 while age < 18:
     # print(f"Мне {age} лет, Я ребенок!")
    age += 1
print("Пора в армию!")
i = 0
 while i < 5:
     print("Привет")
     i += 1
a = 1
b = "Привет мир"
while a < 11:
    print(b)
    a += 1
# Задача номер 2
price = 20
allmoney = 110

 while allmoney >= price:
      print("Вы купили товар")
     allmoney -= price
     print(f"У вас осталось: {allmoney}")
print("У вас не хватает денег")




# Задача 3
print("*" * 30)
print("Игра - Угадай число \n")
print("*" * 30)
mysteryNumber = 5
inputNumber = int(input("Угадай какое число я загадал (1-100)"))


 while mysteryNumber != inputNumber:
    if mysteryNumber < inputNumber:
        print("Загадоное число меньше")
    else:
        print("Загадонное число больше")
    print("Это неверное число")
    inputNumber = int(input("Попробуй еще раз:"))

print("Подравляем ты угадал!!!!!")
# Цикл for


for MAX in range(100):
     print("")

# Задача 4

a = int(input("Введите число: "))
sum = 0
for i in range(1, a + 1):
    sum += i
print(sum)
```
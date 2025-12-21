# # print(f"Результат остаточного деления числа 435 на 35 = {435 % 35}")
# # print(f"Результат остаточного деления числа 543 на 246 = {543 % 246}")
# # print(f"Результат остаточного деления числа 400 на 20 = {400 // 20}")
# book = 100
# a = int(input("Введите свой бюджет: "))
# if a >= 100:
#     print("Поздравляем вас, хотите оформить покупку?")
# else:
#     print("Увы, у вас недостаточно средств, но мы можем предложить вам другую не менее интересную книгу")
current_year = 2025
current_day = 5
current_month = 10
birthday_year = int(input("Введите ваш год рождения: "))
birthday_month = int(input("Введите ваш месяц рождения: "))
birthday = int(input("Введите число вашего рождения: "))
age = current_year - birthday_year
if (current_month > birthday_month):
    print("Вам", age, "лет")
elif (current_month == birthday_month):
    if (current_day >= birthday):
        print("Вам", age, "лет")
    else:
        print("Вам", age - 1, "лет")
else:
    print("Вам", age - 1, "лет")








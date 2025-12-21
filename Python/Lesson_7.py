#Генератор пароля

# import random as r
# import string as s

# def password_generation(lenPas, iSnums, isUpAlpha):
#     symbols = s.ascii_lowercase
#     password = ""
#     if isUpAlpha:
#         symbols += s.ascii_uppercase
#     if iSnums:
#         symbols += "1234567890"
#     for _ in range(lenPas):
#         password += r.choice(symbols)
#     return password


# print(password_generation(3, True, False))



#Определитель четности
def chet(c):
    if c % 2 == 0:
        return True
    else:
        return False
print(chet(9))

#Количество глассных букв
def bykvi(word):
    w = "аеуюяиэёоы"
    count = 0
    for sym in w:
        count += word.count(sym)
        return count
 
#Сумма цифр числа
def SumDigitsOfNumber(number):
    strNumber = str(number)
    summa = 0
    for i in strNumber:
        summa += int(i)
    return(summa)
print(SumDigitsOfNumber(456))

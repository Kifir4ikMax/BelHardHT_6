""" Задача 3.

Получить на ввод количество рублей и копеек и вывести в правильной форме,
например, 3 рубля, 1 рубль 25 копеек, 3 копейки.

"""


# Создаём цикл на проверку вводимых данных для "рублей" и "копеек" соответственно.
while True:
    rubles_income = input("Введите количество рублей: ")
    if not rubles_income.isdigit():
        print("Введите число!")
    else:
        break
while True:  
    coins_income = input("Введите количество копеек: ")
    if not coins_income.isdigit():
        print("Введите число!")
    else:
        break
    
# Создаём условие для проверки окончаний выводимых слов в зависимости от ввода. Используем списки и срезы. Сначала "рубли".
list_1 = ['0', '1', '5', '6', '7', '8', '9']
list_2 = ['2', '3', '4']
list_3 = ['12', '13', '14']
list_4 = ['21', '31', '41', '51', '61', '71', '81', '91', '01']
if rubles_income[-1] in list_1:
    quote1 = "рублей"
if rubles_income[-1] in list_2:
    quote1 = "рубля"
if rubles_income[-2:] in list_3:
    quote1 = "рублей"
if rubles_income == '1' or rubles_income[-2:] in list_4:
    quote1 = "рубль"


# Теперь для "копеек".
if coins_income[-1] in list_1:
    quote2 = "копеек"  
if coins_income[-1] in list_2:
    quote2 = "копейки" 
if coins_income[-2:] in list_3:
    quote2 = "копеек"     
if coins_income == '1' or coins_income[-2:] in list_4:
    quote2 = "копейка"    


#Выводим результат на экран с помощью f-строк.
print(f"Ваш депозит: {rubles_income} {quote1} {coins_income} {quote2}.")

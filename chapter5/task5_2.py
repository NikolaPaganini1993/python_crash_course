# 5.2. Больше условий: количество условий не ограничивается десятью.
# Программа должна выдавать по крайней мере один истинный и один ложный результат для следующих видов проверок:
# • Проверка равенства и неравенства строк.
# • Проверки с использованием функции lower().
# • Числовые проверки равенства и неравенства, условий «больше», «меньше», «больше или равно», «меньше или равно».
# • Проверки с ключевым словом and и or.
# • Проверка вхождения элемента в список.
# • Проверка отсутствия элемента в списке.
car = input("What's auto?\n")
car = car.lower()
cars = ['toyota', 'kia', 'nissan']
if car in cars:
    print(f'Yes, i wanna {car.title()}')
    price = int(input('What price?\n'))
    if price >= 500000 and price <= 1000000:
        print('Good')
        age = int(input('Which year?\n'))
        passport = input('Do have autopassport? (Answer: yes/no)\n')
        if age >= 2010 and passport == 'да':
            print('Yes, i need it')
        else:
            print('I need another option')
    elif price > 1000000:
        print('Very expensive')
    else:
        print('We can habe something better?')
else:
    print('Lets go search another auto')

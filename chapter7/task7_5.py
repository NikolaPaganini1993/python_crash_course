# 7.5. Билеты в кино: кинотеатр установил несколько вариантов цены на билеты в зависимости от возраста посетителя.
# Для посетителей младше 3 лет билет бесплатный; в возрасте от 3 до 12 билет стоит $10;
# наконец, если возраст посетителя больше 12, билет стоит $15.
# Напишите цикл, который предлагает пользователю ввести возраст и выводит цену билета.
while True:
    age = int(input('How old are you?\n'))
    if age < 3:
        print("You price for free")
    elif age >= 3 and age <= 12:
        print("You price is $10.")
    else:
        print("You price is $15.")
    break


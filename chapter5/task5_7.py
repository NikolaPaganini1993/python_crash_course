# 5.7. Любимый фрукт: составьте список своих любимых фруктов.
# Напишите серию независимых команд if для проверки того, присутствуют ли некоторые фрукты в списке.
# • Создайте список трех своих любимых фруктов и назовите его favorite_fruits.
# • Напишите пять команд if. Каждая команда должна проверять, входит ли определенный тип фрукта в список.
# Если фрукт входит в список, блок if должен выводить
# сообщение вида «You really like bananas!».
favorite_fruits = ['watermelon', 'pineapple', 'mango']
fruit = input('What fruit?\n')
fruit = fruit.lower()
if fruit in favorite_fruits:
    print(f'I really like {fruit}')
else:
    print(f'I dont like {fruit}')
# Перебор всего списка
# В ситуациях, требующих применения одного действия к каждому
# элементу списка, можно воспользоваться циклами for.
# Допустим, имеется список с именами фокусников и вы хотите вывести каждое имя
# из списка. Конечно, можно обратиться к каждому элементу по отдельности, но такой подход создает ряд проблем.
# Во-первых, для очень длинных списков все сведется к однообразным повторениям.
# Во-вторых, при любом изменении длины списка в программу придется вносить изменения.
# Цикл for решает обе проблемы: Python будет следить за всеми техническими деталями в своей внутренней реализации.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was great trick!')
    print(f'i cant wait you next trick, {magician.title()}.\n')
print('Thank you, everyone, that was great magic show!')

# Функция range()
# Функция range() упрощает построение числовых последовательностей. Например,
# с ее помощью можно легко вывести серию чисел:
for value in range(1,5):
    print(value)

# Использование range() для создания числового списка
# Если вы хотите создать числовой список, преобразуйте результаты range() в список
# при помощи функции list(). Если заключить вызов range() в list(), то результат
# будет представлять собой список с числовыми элементами.
# В примере из предыдущего раздела числовая последовательность просто выводилась на экран.
# Тот же набор чисел можно преобразовать в список вызовом list():
numbers = list(range(1,6))
print(numbers)

# Функция range() также может генерировать числовые последовательности, пропуская числа в заданном диапазоне.
# Например, построение списка четных чисел от 1 до 10 происходит так:
even_numbers = list(range(2,11,2))
print(even_numbers)

# С помощью функции range() можно создать практически любой диапазон чисел.
# Например, как бы вы создали список квадратов всех целых чисел от 1 до 10?
# В языке Python операция возведения в степень обозначается двумя звездочками (**).
# Один из возможных вариантов выглядит так:
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# Простая статистика с числовыми списками
# Некоторые функции Python предназначены для работы с числовыми списками.
# Например, вы можете легко узнать минимум, максимум и сумму числового списка:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# Генераторы списков
# Описанный выше способ генерирования списка squares состоял из трех или четырех
# строк кода. Генератор списка (list comprehension) позволяет сгенерировать тот же
# список всего в одной строке. Генератор списка объединяет цикл for и создание новых
# элементов в одну строку и автоматически присоединяет к списку все новые элементы.
# В следующем примере список квадратов, знакомый вам по предыдущим примерам,
# строится с использованием генератора списка:
squares = [value**2 for value in range(1,11)]
print(squares)
# Чтобы использовать этот синтаксис, начните с содержательного имени списка,
# например squares. Затем откройте квадратные скобки и определите выражение
# для значений, которые должны быть сохранены в новом списке.
# В данном примере это выражение value**2, которое возводит значение во вторую степень.
# Затем напишите цикл for для генерирования чисел, которые должны передаваться выражению, и закройте квадратные скобки.
# Цикл for в данном примере — for value in range(1,11) — передает значения с 1 до 10 выражению value**2.
# Обратите внимание на отсутствие двоеточия в конце команды for.

# Создание сегмента
# Чтобы создать сегмент на основе списка, следует задать индексы первого и последнего элементов,
# с которыми вы намереваетесь работать. Как и в случае с функцией
# range(), Python останавливается на элементе, предшествующем второму индексу.
# Скажем, чтобы вывести первые три элемента списка, запросите индексы с 0 по 3,
# и вы получите элементы 0, 1 и 2.
# В следующем примере используется список игроков команды:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# Перебор содержимого сегмента
# Если вы хотите перебрать элементы, входящие в подмножество элементов, используйте сегмент в цикле for.
# В следующем примере программа перебирает первых
# трех игроков и выводит их имена:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Копирование списка
# Чтобы скопировать список, создайте сегмент, включающий весь исходный список
# без указания первого и второго индекса ([:]). Эта конструкция создает сегмент,
# который начинается с первого элемента и завершается последним; в результате
# создается копия всего списка.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
my_foods.append('ice cream')
print(my_foods)
print("\nMy friend's favorite foods are:")
friend_foods.append('hot dog')
print(friend_foods)

# Кортежи
# В языке Python значения, которые не могут изменяться, называются неизменяемыми (immutable),
# а неизменяемый список называется кортежем.
# Определение кортежа
# Кортеж выглядит как список, не считая того, что вместо квадратных скобок используются круглые скобки.
# После определения кортежа вы можете обращаться к его отдельным элементам по индексам точно так же,
# как это делается при работе со списком.
# Допустим, имеется прямоугольник, который в программе всегда должен иметь
# строго определенные размеры. Чтобы гарантировать неизменность размеров, можно объединить размеры в кортеж:
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Перебор всех значений в кортеже
# Для перебора всех значений в кортеже используется цикл for, как и при работе со списками:
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# Замена кортежа
# Элементы кортежа не могут изменяться, но вы можете присвоить новое значение
# переменной, в которой хранится кортеж. Таким образом, для изменения размеров
# прямоугольника следует переопределить весь кортеж:
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
# Глава № 2.

# Переменные и простые типы данных.
# Попробуем использовать переменную в программе.

message = "Hello Python world!"
print(message)

# В программу добавилась переменная с именем message.
# В каждой переменной хранится значение, то есть данные,
# связанные с переменной. В нашем случае значением
# является текст "Hello Python world!".

# Строки
# Строка представляет собой простую последовательность символов.
# Любая последовательность символов, заключенная в кавычки, в Python считается строкой

# Одна из простейших операций, выполняемых со строками, — изменение регистра символов.
name = "ada lovelace"
print(name.title())
# Метод title() преобразует первый символ каждого слова в строке к верхнему
# регистру, тогда как все остальные символы выводятся в нижнем регистре

# Для работы с регистром также существуют другие полезные методы. Например, все
# символы строки можно преобразовать к верхнему или нижнему регистру:
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# Использование переменных в
# В некоторых ситуациях требуется использовать значения переменных внутри строки
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
# Чтобы вставить значение переменной в строку, поставьте букву f непосредственно
# перед открывающей кавычкой. Такие строки называются f-строками.
# С f-строками можно сделать много интересного. Например, с их помощью можно
# строить сложные сообщения с информацией, хранящейся в переменных. Рассмотрим пример:
first_name2 = "никола"
last_name2 = "паганини"
full_name2 = f"{first_name2} {last_name2}"
print(f"Hello, {full_name2.title()}!")

# Табуляции и разрывы строк
# Для включения в текст позиции табуляции используется комбинация символов \t
print("Python")
print("\tPython")

# Разрывы строк добавляются с помощью комбинации символов \n:
print("Languages:\nPython\nC\nJavaScript")

# Табуляции и разрывы строк могут сочетаться в тексте. Скажем, последовательность
# "\n\t" приказывает Python начать текст с новой строки, в начале которой располагается табуляция.
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Удаление пропусков
# Python может искать лишние пропуски у левого и правого края строки. Чтобы
# убедиться в том, что у правого края (в конце) строки нет пропусков, вызовите
# метод rstrip().
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
# Впрочем, удаление лишь временное, чтобы навсегда исключить пропуск из строки,
# следует записать усеченное значение обратно в переменную:
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)
# Пропуски также можно удалить у левого края (в начале) строки при помощи метода lstrip(),
# а метод strip() удаляет пропуски с обоих концов:
favorite_language2 = ' python '
print(favorite_language2)
print(favorite_language2.rstrip())
print(favorite_language2.lstrip())
print(favorite_language2.strip())

# Целые числа
# В Python с целыми числами можно выполнять операции сложения (+), вычитания (-), умножения (*) и деления(/).
# Для представления операции возведения в степень в Python используется сдвоенный знак умножения (**).
print(1 + 1)

# Вещественные числа
# В Python числа, имеющие дробную часть, называются вещественными (или «числами с плавающей точкой»).
print(1.1 + 1.2)

# Целые и вещественные числа
# При делении двух любых чисел — даже если это целые числа, частным от деления
# которых является целое число, — вы всегда получаете вещественное число:
print(4 / 2)

# При смешении целого и вещественного числа в любой другой операции вы также
# получаете вещественное число:
print(4 - 3.0)

# Множественное присваивание
# В одной строке программы можно присвоить значения сразу нескольким переменным.
# Например, следующая строка инициализирует переменные x, y и z нулями:
x, y, z = 0, 0, 0
print(x, y, z)

# Константы
# Константа представляет собой переменную, значение которой остается неизменным
# на протяжении всего срока жизни программы. В Python нет встроенных типов констант,
# но у программистов Python принято записывать имена переменных, которые должны
# рассматриваться как константы и оставаться неизменными, буквами верхнего регистра:
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)
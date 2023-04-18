# Списки
# Списки позволяют хранить в одном месте взаимосвязанные данные,
# сколько бы их ни было — несколько элементов или несколько миллионов элементов

# Список представляет собой набор элементов, следующих в определенном порядке.
# Вы можете создать список для хранения букв алфавита, цифр от 0 до 9 или имен
# всех членов вашей семьи. В список можно поместить любую информацию, причем
# данные в списке даже не обязаны быть как-то связаны друг с другом.
# Так как список обычно содержит более одного элемента, рекомендуется присваивать спискам
# имена во множественном числе: letters, digits, names и т. д.
# В языке Python список обозначается квадратными скобками ([]), а отдельные
# элементы списка разделяются запятыми. Простой пример списка с названиями моделей велосипедов:
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Обращение к элементам списка
# Списки представляют собой упорядоченные наборы данных, поэтому для обращения
# к любому элементу списка следует сообщить Python позицию (индекс) нужного
# элемента. Чтобы обратиться к элементу в списке, укажите имя списка, за которым
# следует индекс элемента в квадратных скобках.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

# Индексы начинаются с 0, а не с 1
# Python считает, что первый элемент списка находится в позиции 0, а не в позиции 1.
print(bicycles[1])
print(bicycles[3])

# В Python также существует специальный синтаксис для обращения к последнему
# элементу списка. Если запросить элемент с индексом –1, Python всегда возвращает
# последний элемент в списке:
print(bicycles[-1])

# Синтаксис также распространяется на
# другие отрицательные значения индексов. Индекс –2 возвращает второй элемент
# от конца списка, индекс –3 — третий элемент от конца, и т.
print(bicycles[-2])
print(bicycles[-3])

# Отдельные значения из списка используются так же, как и любые другие переменные.
# Например, вы можете воспользоваться f-строками для построения сообщения, содержащего значение из списка.
# Попробуем извлечь название первого велосипеда из списка и составить сообщение,
# включающее это значение.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# Изменение элементов в списке
# Синтаксис изменения элемента напоминает синтаксис обращения к элементу
# списка. Чтобы изменить элемент, укажите имя списка и индекс изменяемого элемента в квадратных скобках;
# далее задайте новое значение, которое должно быть присвоено элементу.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# Присоединение элементов в конец списка
# Простейший способ добавления новых элементов в список — присоединение элемента в конец списка.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

# Метод append() в точке  присоединяет строку 'ducati' в конец списка, другие
# элементы в списке при этом остаются неизменными
# Метод append() упрощает динамическое построение списков. Например, вы можете начать с пустого списка
# и добавлять в него элементы серией команд append().
# В следующем примере в пустой список добавляются элементы 'honda', 'yamaha' и 'suzuki':
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Вставка элементов в список
# Метод insert() позволяет добавить новый элемент в произвольную позицию списка.
# Для этого следует указать индекс и значение нового элемента.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Удаление элемента с использованием команды del
# Если вам известна позиция элемента, который должен быть удален из списка, воспользуйтесь командой del.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# Удаление элемента с использованием метода pop()
# Иногда значение, удаляемое из списка, должно как-то использоваться. Допустим,
# вы хотите получить координаты x и y только что сбитого корабля пришельцев,
# чтобы изобразить взрыв в этой позиции. В веб-приложении пользователь, удаленный
# из списка активных участников, может быть добавлен в список неактивных, и т. д.
# Метод pop() удаляет последний элемент из списка, но позволяет работать с ним
# после удаления. Удалим мотоцикл из списка:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()   #создаём новый список, и в него кладём последний удаленный элемент из списка
print(motorcycles)
print(popped_motorcycle)

# Извлечение элементов из произвольной позиции списка
# Вызов pop() может использоваться для удаления элемента в произвольной позиции
# списка; для этого следует указать индекс удаляемого элемента в круглых скобках.
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Удаление элементов по значению
# Иногда позиция удаляемого элемента неизвестна. Если вы знаете только значение
# элемента, используйте метод remove().
# Допустим, из списка нужно удалить значение 'ducati':
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# Метод remove() также может использоваться для работы со значением, которое
# удаляется из списка. Следующая программа удаляет значение 'ducati' и выводит
# причину удаления:
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# Постоянная сортировка списка методом sort()
# Метод sort() позволяет относительно легко отсортировать список. Предположим,
# имеется список машин и вы хотите переупорядочить эти элементы по алфавиту.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Список также можно отсортировать в обратном алфавитном порядке; для этого
# методу sort() следует передать аргумент reverse=True. В следующем примере
# список сортируется в порядке, обратном алфавитному:
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Временная сортировка списка функцией sorted()
# Чтобы сохранить исходный порядок элементов списка, но временно представить их
# в отсортированном порядке, можно воспользоваться функцией sorted(). Функция
# sorted() позволяет представить список в определенном порядке, но не изменяет
# фактический порядок элементов в списке.
# Попробуем применить эту функцию к списку машин.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# Вывод списка в обратном порядке
# Чтобы переставить элементы списка в обратном порядке, используйте метод
# reverse(). Скажем, если список машин первоначально хранился в хронологическом
# порядке даты приобретения, элементы можно легко переупорядочить в обратном хронологическом порядке:
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# Определение длины списка
# Вы можете быстро определить длину списка с помощью функции len().
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
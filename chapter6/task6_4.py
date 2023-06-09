# 6.4. Глоссарий 2: теперь, когда вы знаете, как перебрать элементы словаря, упростите код из упражнения 6.3,
# заменив серию команд print циклом, перебирающим ключи и значения словаря.
# Когда вы будете уверены в том, что цикл работает, добавьте в глоссарий еще пять терминов Python.
# При повторном запуске программы новые слова и значения должны быть автоматически включены в вывод.
glossary = {
    'словари': 'Словари — структурах данных, предназначенных для объединения взаимосвязанной информации.\n',
    'списки': 'Список представляет собой набор элементов, следующих в определенном порядке.'
    '\nСписки позволяют хранить в одном месте взаимосвязанные данные, '
    '\nсколько бы их ни было — несколько элементов или несколько миллионов элементов\n',
    'строки': 'Строка представляет собой простую последовательность символов.'
    '\nЛюбая последовательность символов, заключенная в кавычки, в Python считается строкой\n',
    'простые команды if': 'Простейшая форма команды if состоит из одного условия и одного действия.\n',
    'удаление пар «ключ-значение»': 'Пару «ключ-значение» можно полностью удалить при помощи команды del.\n'
    }
for values in glossary.values():
    print(values)
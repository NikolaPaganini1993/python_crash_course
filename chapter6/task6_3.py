# 6.3. Глоссарий: словари Python могут использоваться для моделирования «настоящего» словаря
# (чтобы не создавать путаницу, назовем его глоссарием):
# • Вспомните пять терминов из области программирования, которые вы узнали в предыдущих главах.
# Используйте эти слова как ключи глоссария, а их определения — как значения.
# • Выведите каждое слово и его определение в аккуратно отформатированном виде.
# Например, вы можете вывести слово, затем двоеточие и определение или же слово
# в одной строке, а его определение — с отступом в следующей строке. Используйте
# символ новой строки (\n) для вставки пустых строк между парами «слово — определение» в выходных данных.
person = {'словари': 'Словари — структурах данных, предназначенных для объединения взаимосвязанной информации.',
          'списки': 'Список представляет собой набор элементов, следующих в определенном порядке.'
                    '\nСписки позволяют хранить в одном месте взаимосвязанные данные, '
                    '\nсколько бы их ни было — несколько элементов или несколько миллионов элементов',
          'строки': 'Строка представляет собой простую последовательность символов.'
                    '\nЛюбая последовательность символов, заключенная в кавычки, в Python считается строкой',
          'простые команды if': 'Простейшая форма команды if состоит из одного условия и одного действия.'
          }
print(person['словари'])
print(person['списки'])
print(person['строки'])
print(person['простые команды if'])
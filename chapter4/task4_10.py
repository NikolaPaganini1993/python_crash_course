# 4.10. Сегменты: добавьте в конец одной из программ, написанных в этой главе, фрагмент,
# который делает следующее:
# • Выводит сообщение «The first three items in the list are:», а затем использует сегмент
# для вывода первых трех элементов из списка.
# • Выводит сообщение «Three items from the middle of the list are:», а затем использует
# сегмент для вывода первых трех элементов из середины списка.
# • Выводит сообщение «The last three items in the list are:», а затем использует сегмент
# для вывода последних трех элементов из списка.
numbers = [i for i in range(1, 10)]
print(f'The first three items in the list are:')
print(numbers[:3])
print('\nThree items from the middle of the list are:')
print(numbers[4:7])
print('\nThe last three items in the list are:')
print(numbers[-3:])
# 5.3. Цвета 1: представьте, что в вашей компьютерной игре только что был подбит корабль
# пришельцев. Создайте переменную с именем alien_color и присвойте ей значение 'green',
# 'yellow' или 'red'.
# • Напишите команду if для проверки того, что переменная содержит значение
# 'green'. Если условие истинно, выведите сообщение о том, что игрок только что
# заработал 5 очков.
# • Напишите одну версию программы, в которой условие if выполняется, и другую
# версию, в которой оно не выполняется. (Во второй версии никакое сообщение выводиться не должно.)
colors = ['green', 'yellow', 'red']
alien_color = input('Which color?\n')
alien_color = alien_color.lower()
if alien_color in colors:
    if alien_color == 'green':
        print('You earned 5 points')
    else:
        print('Nothing')
else:
    print('Select green/yellow/red')
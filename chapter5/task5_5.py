# 5.5. Цвета 3: преобразуйте цепочку if-else из упражнения 5.4 в цепочку if-elif-else.
# • Если переменная содержит значение 'green', выведите сообщение о том, что игрок
# только что заработал 5 очков.
# • Если переменная содержит значение 'yellow', выведите сообщение о том, что игрок
# только что заработал 10 очков.
# • Если переменная содержит значение 'red', выведите сообщение о том, что игрок
# только что заработал 15 очков.
# • Напишите три версии программы и проследите за тем, чтобы для каждого цвета
# пришельца выводилось соответствующее сообщение.
alien_color = input('Which color?\n')
alien_color = alien_color.lower()
if alien_color == 'green':
    print('You earned 5 points')
elif alien_color == 'yellow':
    print('You earned 10 points')
elif alien_color == 'red':
    print('You earned 15 points')
else:
    print('Select green/yellow/red')
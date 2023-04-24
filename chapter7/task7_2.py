# 7.2. Заказ стола: напишите программу, которая спрашивает у пользователя,
# на сколько мест он хочет забронировать стол в ресторане.
# Если введенное число больше 8, выведите сообщение о том, что пользователю придется подождать.
# В противном случае сообщите, что стол готов.
table = int(input('How many person you want in you table?'))
if table > 8:
    print('Sorry now we havent table, plz wait')
else:
    print('You table is ready, we waiting you')

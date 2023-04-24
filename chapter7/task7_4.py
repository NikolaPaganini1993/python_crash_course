# 7.4. Топпинг для пиццы: напишите цикл, который предлагает пользователю вводить дополнения для пиццы до тех пор,
# пока не будет введено значение 'quit'.
# При вводе каждого дополнения выведите сообщение о том, что это дополнение включено в заказ.
toppings = []
while True:
    topping = input('What topping you want?\n'
                    'Enter "quit" to end the program. \n')
    toppings.append(topping)
    if topping == 'quit':
        break
    print(f'We added {topping.title()}')
print('You gave pizza with that topping:')
for i in toppings[:-1]:
    print(f'\tYour added {i.title()}.')
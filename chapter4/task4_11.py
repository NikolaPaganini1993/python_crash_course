# 4.11. Моя пицца, твоя пицца: начните с программы из упражнения. Создайте копию
# списка с видами пиццы, присвойте ему имя friend_pizzas. Затем сделайте следующее:
# • Добавьте новую пиццу в исходный список.
# • Добавьте другую пиццу в список friend_pizzas.
# • Докажите, что в программе существуют два разных списка. Выведите сообщение
# «My favorite pizzas are:», а затем первый список в цикле for. Выведите сообщение
# «My friend’s favorite pizzas are:», а затем второй список в цикле for. Убедитесь в том,
# что каждая новая пицца находится в соответствующем списке.
pizzas = ['charlote', 'peperoni', 'cheese']
friend_pizzas = pizzas[:]
pizzas.append('bologneze')
friend_pizzas.append('karbonara')
print(f'My favorite pizzas are:')
for i in pizzas:
    print(i.title())
print(f'\nMy friend’s favorite pizzas are:')
for i in friend_pizzas:
    print(i.title())

# 4.12. Больше циклов: во всех версиях foods.py из этого раздела мы избегали использования
# цикла for при выводе для экономии места. Выберите версию foods.py и напишите два цикла for для вывода каждого списка.
pizzas = ['charlote', 'peperoni', 'cheese']
for i in pizzas:
    print(i.title())
friend_pizzas = pizzas[:]
for i in friend_pizzas:
    print(i.title())
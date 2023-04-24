# 7.8. Сэндвичи: создайте список с именем sandwich_orders, заполните его названиями различных видов сэндвичей.
# Создайте пустой список с именем finished_sandwiches.
# В цикле переберите элементы первого списка и выведите сообщение для каждого элемента
# (например, «I made your tuna sandwich»).
# После этого каждый сэндвич из первого списка перемещается в список finished_sandwiches.
# После того как все элементы первого списка будут обработаны,
# выведите сообщение с перечислением всех изготовленных сэндвичей.
# sandwich_orders = ['subway', 'cheeseburger', 'hamburger']
# finished_sandwiches = []
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"Added sandwich: {current_sandwich}")
#     sandwich_orders.append(current_sandwich)
# print('Your order that sandwich: ')
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich)

sandwich_orders = ['subway', 'cheeseburger', 'hamburger']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Added sandwich: {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)
print("\nYour order that sandwich: ")
for finished_sandwich in finished_sandwiches:
    print(f'\t {finished_sandwich.title()}')




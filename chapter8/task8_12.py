# 8.12. Сэндвичи: напишите функцию, которая получает список компонентов сэндвича.
# Функция должна иметь один параметр для любого количества значений,
# переданных при вызове функции, и выводить описание заказанного сэндвича.
# Вызовите функцию три раза с разным количеством аргументов.
def make_sandwich(size, *sandwich_info):
    print(f'Making a {size}-inch pizza with the following toppings:')
    for topping in sandwich_info:
        print(f'\t-- {topping}')
make_sandwich(15, 'cheese', 'ham', 'mushrooms')
make_sandwich(20, 'cheese', 'ham')
make_sandwich(25, 'cheese')

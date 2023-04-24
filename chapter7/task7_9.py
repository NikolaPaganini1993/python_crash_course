# 7.9. Без пастрами: используя список sandwich_orders из упражнения 7.8,
# проследите за тем, чтобы значение 'pastrami' встречалось в списке как минимум три раза.
# Добавьте в начало программы код для вывода сообщения о том, что пастрами больше нет,
# и напишите цикл while для удаления всех вхождений 'pastrami' из sandwich_orders.
# Убедитесь в том, что в finished_sandwiches значение 'pastrami' не встречается ни одного раза.
sandwich_orders = ['subway', 'pastrami', 'cheeseburger', 'pastrami', 'hamburger', 'pastrami']
finished_sandwiches = []
print('Now we havent pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print('Remove pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'We added {current_sandwich}')
    finished_sandwiches.append(current_sandwich)
print('In finished sandwiches we have: ')
for i in finished_sandwiches:
    print(f'\t{i}')
# 4.2. Животные: создайте список из трех (и более) животных, обладающих общей характеристикой.
# Используйте цикл for для вывода названий всех животных.
# • Измените программу так, чтобы вместо простого названия выводилось сообщение,
# включающее это название, — например, «A dog would make a great pet».
# • Добавьте в конец программы строку с описанием общего свойства.
# Например, можно вывести сообщение «Any of these animals would make a great pet!».
animals = ['cat', 'dog', 'tiger']
for animal in animals:
    print(f'{animal.title()} would make gteat pet')
print('Any of these animals would make a great pet')
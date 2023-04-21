# 5.8. Hello Admin: создайте список из пяти и более имен пользователей, включающий имя
# 'admin'. Представьте, что вы пишете код, который выводит приветственное сообщение для
# каждого пользователя после его входа на сайт.
# Переберите элементы списка и выведите сообщение для каждого пользователя:
# • Для пользователя с именем 'admin’ выведите особое сообщение — например, «Hello
# admin, would you like to see a status report?».
# • В остальных случаях выводите универсальное приветствие — например, «Hello
# Jaden, thank you for logging in again».
users = ['admin', 'quest', 'manager', 'staff', 'client']
for user in users:
    if user == 'admin':
        print(f'Hello, {user.title()}, would you like to see status report?')
    elif user == 'quest':
        print(f'Hello, {user.title()}, please registration for continue')
    elif user == 'manager':
        print(f'Hello, {user.title()}, any sales today?')
    elif user == 'staff':
        print(f'Hello, {user.title()}, you must work')
    elif user == 'client':
        print(f'Hello, {user.title()}, please give me you login and password')
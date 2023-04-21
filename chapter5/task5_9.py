# 5.9. Без пользователей: добавьте в hello_admin.py команду if,
# которая проверит, что список пользователей не пуст.
# • Если список пуст, выведите сообщение «We need to ind some users!».
# • Удалите из списка все имена пользователей и убедитесь в том, что программа выводит правильное сообщение.
users = []
if users:
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
else:
    print('We need to ind some users!')
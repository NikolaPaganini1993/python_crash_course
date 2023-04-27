# 8.8. Пользовательские альбомы: начните с программы из упражнения 8.7.
# Напишите цикл while, в котором пользователь вводит исполнителя и название альбома.
# Затем в цикле вызывается функция make_album() для введенных пользователей и выводится созданный словарь.
# Не забудьте предусмотреть признак завершения в цикле while.
def make_album(vocalist, album, quantity=None):
    if quantity:
        track = {'vocalist': vocalist, 'album': album, 'quantity': quantity}
    else:
        track = {'vocalist': vocalist, 'album': album}
    return track
while True:
    print('\nPlease tell me your favorite singer:')
    print("(enter 'q' at any time to quit)")
    name = input('What name?\n')
    if name == 'q':
        break
    album = input('What album?\n')
    if album == 'q':
        break
    quantity = input('Do you know how many tracks in album? \nIf you dont know, select no\n')
    if quantity == 'q':
        break
    if quantity == 'no':
        quantity = None
    formatted_info = make_album(name, album, quantity)
    print(f'\n{formatted_info}')
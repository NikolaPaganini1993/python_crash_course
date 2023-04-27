# 8.17. Стилевое оформление функций: выберите любые три программы, написанные для этой главы.
# Убедитесь в том, что в них соблюдаются рекомендации стилевого оформления, представленные в этом разделе.
def display_message(name):
    print(f'Hello, {name.title()}')
display_message('nikola')
def make_shirt(size, message):
    print(f'I wanna shirt {size} size and text on my shirt {message.upper()}')
make_shirt(size='40', message='arsenal')
def make_album(vocalist, album, quantity=None):
    if quantity:
        track = {'vocalist': vocalist, 'album': album, 'quantity': quantity}
    else:
        track = {'vocalist': vocalist, 'album': album}
    return track
print(make_album('eminem', 'in to the bridge'))
def greet_user(name, age):
    print(f'Hello, {name}! You {age} old year')
greet_user('nikola', 30)
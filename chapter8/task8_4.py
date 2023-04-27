# 8.4. Большие футболки: измените функцию make_shirt(),
# чтобы по умолчанию футболки имели размер L и на них выводился текст «I love Python».
# Создайте футболку с размером L и текстом по умолчанию, а также футболку любого размера с другим текстом.
def make_shirt(size='L', message='I love Python'):
    print(f'I wanna shirt {size.title()} size and text on my shirt {message.upper()}')
make_shirt()
make_shirt(size='m', message='arsenal')
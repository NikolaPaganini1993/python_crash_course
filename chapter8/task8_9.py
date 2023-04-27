# 8.9. Сообщения: создайте список с серией коротких сообщений.
# Передайте список функции show_messages(), которая выводит текст каждого сообщения в списке.
messages = ['Привет!', 'Как дела?', 'Что нового?', 'Все хорошо?', 'До свидания!']
def show_messages(message_list):
    for message in message_list:
        print(message)
show_messages(messages)

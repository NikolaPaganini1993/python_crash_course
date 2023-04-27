# 8.10. Отправка сообщений: начните с копии вашей программы из упражнения 8.9.
# Напишите функцию send_messages(),
# которая выводит каждое сообщение и перемещает его в новый список с именем sent_messages.
# После вызова функции выведите оба списка и убедитесь в том, что перемещение прошло успешно.
def show_messages(messages):
    for message in messages:
        print(message)
def send_messages(messages):
    sent_messages = []
    while messages:
        current_message = messages.pop(0)
        print("Отправка сообщения: " + current_message)
        sent_messages.append(current_message)
    return sent_messages
messages = ['Привет!', 'Как дела?', 'Что нового?', 'Все хорошо?', 'До свидания!']
show_messages(messages)
sent_messages = send_messages(messages)
print("Исходный список сообщений: ")
print(messages)
print("Новый список отправленных сообщений: ")
print(sent_messages)
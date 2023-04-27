# 8.11. Архивированные сообщения: начните с программы из упражнения 8.10.
# Вызовите функцию send_messages() для копии списка сообщений.
# После вызова функции выведите оба списка и убедитесь в том, что в исходном списке остались все сообщения.
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
print("Новый список отправленных сообщений: ")
send_messages(messages[:])
print("Исходный список сообщений: ")
show_messages(messages)
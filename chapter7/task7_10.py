# 7.10. Отпуск мечты: напишите программу, которая опрашивает пользователей, где бы они хотели провести отпуск.
# Включите блок кода для вывода результатов опроса.
responses = {}
polling_active = True
while polling_active:
    name = input('What is your name?\n')
    response = input('Where you wanna going in holiday?\n')
    responses[name] = response
    repeat = input('Would you like to let another person respond? y/n\n')
    if repeat == 'n':
        polling_active = False
for name, response in responses.items():
    print(f'{name.title()} wanna going on holiday in {response.title()}!')


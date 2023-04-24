# 7.3. Числа, кратные 10: запросите у пользователя число и сообщите, кратно оно 10 или нет
number = int(input('What is you number?'))
if number % 10 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')
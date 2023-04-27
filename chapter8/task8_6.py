# 8.6. Названия городов: напишите функцию city_country(), которая получает название города и страну.
# Функция должна возвращать строку в формате "Santiago, Chile".
# Вызовите свою функцию по крайней мере для трех пар «город — страна» и выведите возвращенное значение.
def city_country(sity, country):
    full = f'{sity}, {country}'
    return full.title()
print(city_country('moscow', 'russia'))
print(city_country(sity='itkutsk', country='russia'))
print(city_country('phuket', country='thailand'))

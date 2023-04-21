# 6.11. Города: создайте словарь с именем cities.
# Используйте названия трех городов в качестве ключей словаря.
# Создайте словарь с информацией о каждом городе; включите в него страну, в которой расположен город,
# примерную численность населения и один примечательный факт, относящийся к этому городу.
# Ключи словаря каждого города должны называться country, population и fact.
# Выведите название каждого города и всю сохраненную информацию о нем.
cities = {
    'irkutsk': {
        'country': 'russia',
        'population': 750_000,
        'fact': 'We have lake Baikal'
    },
    'london': {
        'country': 'england',
        'population': 5_000_000,
        'fact': 'We have best football stadium in Europe'
    },
    'bangkok': {
        'country': 'thailand',
        'population': 8_000_000,
        'fact': 'We have sun and sea'
    }
}
for city, city_info in cities.items():
    print(f'City: {city.title()}')
    print(f"\tCountry: {city_info['country'].title()}")
    print(f"\tPopulation: {city_info['population']}")
    print(f"\tFact: {city_info['fact']}")


# 6.12. Расширение: примеры, с которыми мы работаем, стали достаточно сложными,
# и в них можно вносить разного рода усовершенствования.
# Воспользуйтесь одним из примеров этой главы и расширьте его: добавьте новые ключи и значения, измените контекст
# программы или улучшите форматирование вывода.
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
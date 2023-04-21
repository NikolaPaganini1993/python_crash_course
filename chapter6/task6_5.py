# 6.5. Реки: создайте словарь с названиями трех больших рек и стран, по которым протекает каждая река.
# Одна из возможных пар «ключ-значение» — 'nile': 'egypt'.
# • Используйте цикл для вывода сообщения с упоминанием реки и страны — например, «The Nile runs through Egypt».
# • Используйте цикл для вывода названия каждой реки, включенной в словарь.
# • Используйте цикл для вывода названия каждой страны, включенной в словарь.
rivers = {
    'nile': 'egypt',
    'angara': 'russia',
    'vena': 'austria'
}
for key, values in rivers.items():
    print(f'The {key.title()} runs through {values.title()}.')
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())

# 3.10. Все функции: придумайте информацию, которую можно было бы хранить в списке.
# Например, создайте список гор, рек, стран, городов, языков… словом, чего угодно.
# Напишите программу, которая создает список элементов, а затем вызывает каждую функцию,
# упоминавшуюся в этой главе, хотя бы один раз.
countries = ['china', 'russia', 'thailand', 'germany', 'england']
print(countries[0])
print(countries[-1])
print(f'I from {countries[1].title()}, bro!')
countries[0] = 'belarus'
print(countries)
countries.append('brazil')
print(countries)
countries.insert(0, 'france')
print(countries)
del countries[1]
print(countries)
countries.pop()
print(countries)
countries.remove('germany')
print(countries)
asia = 'thailand'
countries.remove(asia)
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
print(sorted(countries))
countries.reverse()
print(countries)
print(len(countries))
# 6.7. Люди: начните с программы, написанной для упражнения 6.1 (с. 113).
# Создайте два новых словаря, представляющих разных людей, и сохраните все три словаря в списке с именем people.
# Переберите элементы списка людей. В процессе перебора выведите всю имеющуюся информацию о каждом человеке.
people1 = {'first_name': 'nikola',
          'last_name': 'paganini',
          'age': 30,
          'city': 'irkutsk'
          }
people2 = {'first_name': 'cristiano',
          'last_name': 'ronaldo',
          'age': 38,
          'city': 'lissabon'
          }
people3 = {'first_name': 'andrei',
          'last_name': 'arshavin',
          'age': 38,
          'city': 'saint petersburg'
          }
peoples = [people1, people2, people3]
for people in peoples:
    print(people)
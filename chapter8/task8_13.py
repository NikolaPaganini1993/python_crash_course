# 8.13. Профиль: начните с копии программы user_profile.py.
# Создайте собственный профиль вызовом build_profile(),
# укажите имя, фамилию и три другие пары «ключ-значение» для вашего описания.
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile1 = build_profile('albert', 'einstein',location='princeton',field='physics')
user_profile2 = build_profile('nikola', 'paganini',location='princeton',field='programmer', age=30)
print(user_profile2)

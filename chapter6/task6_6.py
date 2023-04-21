# 6.6. Опрос: возьмите за основу код favorite_languages.py (с. 115).
# • Создайте список людей, которые должны участвовать в опросе по поводу любимого языка программирования.
# Включите некоторые имена, которые уже присутствуют в списке, и некоторые имена, которых в списке еще нет.
# • Переберите список людей, которые должны участвовать в опросе.
# Если они уже прошли опрос, выведите сообщение с благодарностью за участие.
# Если они еще не проходили опрос, выведите сообщение с предложением принять участие.
friends = ['nikola', 'vadim', 'jen', 'sarah', 'edward', 'phil']
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f'{name.title()} study {language.title()}.')
for friend in friends:
    if friend not in favorite_languages.keys():
        print(f'{friend.title()} you must complete the survey')



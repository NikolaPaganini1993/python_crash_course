# 5.13. Ваши идеи: к этому моменту вы уже стали более квалифицированным программистом, чем когда начинали читать книгу.
# Теперь вы лучше представляете, как в программах
# моделируются явления реального мира, и сможете сами придумать задачи, которые будут
# решаться в ваших программах. Запишите несколько задач,
# которые вам хотелось бы решить по мере роста вашего профессионального мастерства.
# Может быть, это какие-то компьютерные игры, задачи анализа наборов данных или веб-приложения?
colors = ['green', 'yellow', 'red']
alien_color = input('Which color?\n')
alien_color = alien_color.lower()
if alien_color in colors:
    if alien_color == 'green':
        print('You earned 5 points')
    elif alien_color == 'yellow':
        print('You earned 10 points')
    elif alien_color == 'red':
        print('You earned 15 points')
else:
    print('Select green/yellow/red')
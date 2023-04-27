# 8.16. Импортирование: возьмите за основу одну из написанных вами программ с одной функцией.
# Сохраните эту функцию в отдельном файле.
# Импортируйте функцию в файл основной программы и вызовите функцию каждым из следующих способов:
# import имя_модуля
# from имя_модуля import имя_функции
# from имя_модуля import имя_функции as псевдоним
# import имя_модуля as псевдоним
# from имя_модуля import *
import printing_functions
from printing_functions import make_pizza
from printing_functions import build_profile as bd
import printing_functions as pf
from printing_functions import *

import chapter8
chapter8.make_pizza(16, 'pepperoni')
chapter8.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from chapter8 import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from chapter8 import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

import chapter8 as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
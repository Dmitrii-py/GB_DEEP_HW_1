"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
NUM = randint(LOWER_LIMIT, UPPER_LIMIT)
COUNTER = 10
BINGO = None
i = 0
while i < COUNTER:
    i += 1
    input_num = int(input(f'Введите число больше 0 и меньше {UPPER_LIMIT} : '))
    if input_num > NUM:
        print(f'Число больше\n Осталось попыток {COUNTER - i}')
        BINGO = False
    elif input_num < NUM:
        print(f'Число меньше\n Осталось попыток {COUNTER - i}')
        BINGO = False
    else:
        print('Вы угадали число!')
        BINGO = True
        break
if not BINGO:
     print(f'К сожалению вы не угадали число {NUM}')

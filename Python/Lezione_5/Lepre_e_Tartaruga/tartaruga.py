import random

tartaruga = 0

def tartaruga_step():

    global tartaruga
    
    step = random.randint(1, 10)

    match step:
        case 1 | 2 | 3 | 4 | 5:
            tartaruga += 3
        case 6 | 7:
            tartaruga -= 6
        case 8 | 9 | 10:
            tartaruga += 1

    if tartaruga < 0:
        tartaruga = 0

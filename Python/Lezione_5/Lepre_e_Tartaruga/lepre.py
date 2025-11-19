import random

lepre = 0


def lepre_step():

    global lepre

    step = random.randint(1, 10)

    match step:
        case 1 | 2:
            lepre += 0
        case 3 | 4:
            lepre += 9
        case 5:
            lepre -= 12
        case 6 | 7 | 8:
            lepre += 1
        case 9 | 10:
            lepre -= 2

    if lepre < 0:
        lepre = 0

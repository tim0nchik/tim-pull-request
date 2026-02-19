from random import randint

play = input('напиши: play')
lists = ['камень', 'ножницы', 'бумага']

if play == 'play':
    num = randint(0,2)
    print(f'вы показали: {lists[num]}')
    num1 = randint(0,2)
    print(f'противник показал: {lists[num1]}')
    if num == 0:
        if num1 == 1:
            print('win')
        if num1 == 0:
            print('draw')
        if num1 == 2:
            print('lose')
    elif num == 1:
        if num1 == 0:
            print('lose')
        if num1 == 1:
            print('draw')
        if num1 == 2:
            print('win')
    elif num == 2:
        if num1 == 0:
            print('win')
        if num1 == 1:
            print('lose')
        if num1 == 2:
            print('draw')
    
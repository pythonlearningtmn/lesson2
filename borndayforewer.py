# МОДУЛЬ 5

year = 1799
bornyear = 0
day = '6 июня'
bornday = ''

while bornyear != year:
    bornyear = int(input('В каком году родился А.С. Пушкин? '))
    if bornyear != year:
        print('Неверно. Попробуйте ещё раз')

while bornday != day:
    bornday = input('В какой день родился А.С. Пушкин? (формат "1 января") ')
    if bornday != day:
        print('Неверно. Попробуйте ещё раз')

print('Верно')

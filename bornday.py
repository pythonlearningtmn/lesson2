# МОДУЛЬ 3

year = 1799
day = '6 июня'
bornyear = int(input('В каком году родился А.С. Пушкин? '))

if bornyear == year:
    bornday = input('В какой день родился А.С. Пушкин? (формат "1 января") ')
    if bornday == day:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')

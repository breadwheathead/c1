"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.

"""

duration = 999999999
if duration // 60:
    minutes = duration // 60
    seconds = duration % 60
    if minutes // 60:
        hours = minutes // 60
        minutes %= 60
        if hours // 24:
            days = hours // 24
            hours %= 24
            if days // 30:
                mounts = days // 30
                days %= 30
                if mounts // 12:
                    years = mounts // 12
                    mounts %= 12
                    print(f'{years} год ', end='')
                print(f'{mounts} месяц ', end='')
            print(f'{days} день ', end='')
        print(f'{hours} час ', end='')
    print(f'{minutes} мин {seconds} сек')
else:
    print(f'{duration} сек')


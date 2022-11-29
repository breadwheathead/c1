"""
1. Создать класс TrafficLight (светофор):
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт

"""
import time
import os
import itertools


class TrafficLight:

    def __init__(self, color):
        self._color = color

    def running(self):
        if self._color in ('red', 'yellow', 'green'):
            while True:
                if self._color == 'red':
                    print(self._color)
                    time.sleep(1)
                    self._color = 'yellow'
                elif self._color == 'yellow':
                    print(self._color)
                    time.sleep(1)
                    self._color = 'green'
                else:
                    print(self._color)
                    time.sleep(1)
                    self._color = 'red'
            # for clr in itertools.cycle(valid_colors):
            #   pass
        else:
            raise ValueError('Нет такого цвета!')


if __name__ == '__main__':
    light = TrafficLight('red')
    light.running()

"""
 Реализуйте базовый класс Car:
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.

"""


class Car:
    def __init__(self, speed, color, name):
        self.speed = float(speed)
        self.color = color
        self.name = name
        self.is_police = False

    def __str__(self):
        return f'{self.speed} {self.color} {self.name} {self.is_police}'

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        return f'Машина повернула {direction.lower()}'

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости! {self.speed}'
        return self.speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости! {self.speed}'
        return self.speed


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


if __name__ == '__main__':
    kamaz = WorkCar('120.4', 'yellow', 'KAMAZ')
    print(kamaz)
    print(kamaz.go())
    print(kamaz.show_speed())
    print(kamaz.turn('налево'))
    print(kamaz.turn('Направо'))
    print(kamaz.stop())

    lada_calina = SportCar('270', 'red', 'LADA Calina Sport')
    print(lada_calina)

    lada_priora = PoliceCar('240', 'blue-white', 'LADA Priora')
    print(lada_priora)

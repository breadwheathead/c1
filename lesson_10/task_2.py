"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определённое название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке
знания. Реализовать абстрактные классы для основных классов проекта и проверить работу
декоратора @property

"""


class Clothes:
    def __init__(self, name='одежда'):
        self.name = name
        self._fabric_consumption = 0

    def __str__(self):
        return self.name

    @property
    def fabric_consumption(self):
        if not self._fabric_consumption:
            self._fabric_consumption = self.get_fabric_consumption()
        return self._fabric_consumption

    def get_fabric_consumption(self):
        raise NotImplementedError

    def __add__(self, other):
        result = Clothes()
        result._fabric_consumption = self.fabric_consumption + other.fabric_consumption
        return result

    def __radd__(self, other):
        if not isinstance(other, Clothes):
            return self
        return self.__add__(other)


class Coat(Clothes):
    def __init__(self, name, size: float):
        super().__init__(name)
        self.size = float(size)

    def get_fabric_consumption(self):
        return round(self.size / 6.5 + 0.5, 3)


class Costume(Clothes):
    def __init__(self, name, height: float):
        super().__init__(name)
        self.height = float(height)

    def get_fabric_consumption(self):
        return round(2 * self.height + 0.3, 3)


if __name__ == '__main__':
    clothes = Clothes()
    print(clothes)
    coat = Coat('пальто', 48)
    print(coat)
    print(coat.fabric_consumption)
    costume = Costume('костюм', 170)
    print(costume)
    print(costume.fabric_consumption)
    print(sum([coat.fabric_consumption, costume.fabric_consumption, costume.fabric_consumption]))

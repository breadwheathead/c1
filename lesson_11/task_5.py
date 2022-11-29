"""
Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за
приём оргтехники на склад и передачу в определённое подразделение компании. Для
хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).

"""

from abc import ABC, abstractmethod


class Storage:
    def acceptance(self):
        """ Прием оргтехники на склад """
        pass

    def transfer(self):
        """ Передача оргтехники в определенное подразделение компании  """
        pass


class Equipment:
    def __init__(self, name, model, brand, price):
        self.name = name
        self.model = model
        self.brand = brand
        self._price = price


class Printer(Equipment):
    def __init__(self, name, model, brand, price, color=False):
        super().__init__(name, model, brand, price)
        self.color = color


class Scanner(Equipment):
    def __init__(self, name, model, brand, price, scan_speed: float):
        super().__init__(name, model, brand, price)
        self.scan_speed = scan_speed


class Xerox(Equipment):
    def __init__(self, name, model, brand, price, weight, height):
        super().__init__(name, model, brand, price)
        self.weight = weight
        self.height = height


if __name__ == '__main__':
    pass

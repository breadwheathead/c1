"""
Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также
класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведённых типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

"""

class Storage:
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

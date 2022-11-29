"""
Реализовать базовый класс Worker (работник):
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.


"""


class Worker:
    def __init__(self, name, surname, position, wade, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wade': wade,
            'bonus': bonus,
        }


class Position(Worker):
    def get_full_name(self):
        return '{} {}'.format(self.name, self.surname)

    def get_total_income(self):
        return self._income['wade'] + self._income['bonus']


if __name__ == '__main__':
    ironman = Worker('Tony', 'Stark', 'Ironman', 15000, 2000)
    capitan_america = Position('Steven', 'Rogers', 'Capitan America', 12300, 4000)
    thor = Position('Thor', 'Odinson', 'God of Thunder', 12330, 32300)

    print(capitan_america.get_full_name())
    print(capitan_america.get_total_income())

    print(thor.get_full_name())
    print(thor.get_total_income())
    
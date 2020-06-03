"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (
должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров). """


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0, 'bonus': 0}

    def __init__(self, name, surname, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):
    def __init__(self, name, surname, wage: float, bonus: float, *args, **kwargs):
        super().__init__(name, surname, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


position1 = Position('Константин', 'Гримашевич', 100000, 500)
print('Сотрудник', position1.get_full_name(), 'c полным доходом', position1.get_total_income())

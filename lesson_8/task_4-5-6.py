"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за
приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. Подсказка:
постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по
ООП. """

import datetime


def get_days_of_month(year: int, month: int) -> int:
    """
    Функция возвращает кол-во дней в месяце указанного года
    :param year: год в int формате
    :param month: месяц указанного года
    :return: возвращает кол-во дней или 0, если месяц указан с ошибкой
    """
    if year < 1:
        return 0

    if 1 <= month <= 7 and month != 2:
        return 30 + month % 2
    elif 8 <= month <= 12:
        return 31 - month % 2
    elif month == 2:
        return 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    else:
        return 0


def check_date(date: str) -> bool:
    """
    Проверяет корректность даты. Возвращает True или False
    :param date: 'yyyy-mm-dd'
    :return: bool
    """
    try:
        y, m, d = map(int, (date.split('-')))
    except ValueError:
        return False

    if d == 0:
        return False

    return d in range(get_days_of_month(y, m) + 1)


class DateError(ValueError):
    def __init__(self, txt):
        self.text = txt


class CostError(ValueError):
    def __init__(self, txt):
        self.text = txt


class WareHouse:
    __last_id = 0  # Последний id для добавления в словарь и инкрементации
    __items = {}
    """
    items = {id: item} (Словарь словарей c ключем id
    item = {'id': id, 'item': объект учета, 'dep': Подразделение, за которым закреплена единица учета
    'dep_log': [список списков - история перемещения по подразделениям. [дата, подразделение]]}
    """

    def itm_reception(self, item, dep):  # Добавляет объект в перечень имущества склада
        self.__items[self.__last_id] = {'item': item, 'dep': dep, 'dep_log': [[dep, str(datetime.date.today())]]}
        self.__last_id += 1

    def itm_move(self, move_id, dep):
        self.__items[move_id]['dep'] = dep
        self.__items[move_id]['dep_log'].append([dep, str(datetime.date.today())])

    def __str__(self):
        result = ''
        for i in self.__items:
            itm = self.__items[i]['item']
            result += f'{str(i)}: {itm.eq_type} {itm.name}, инв: {itm.inv_n} ({self.__items[i]["dep"]})\n'
        return result


class WareHouseItem:
    eq_type = ''

    def __init__(self, inv_n: str, get_date: str, cost: float, name):
        if not check_date(get_date):
            raise DateError('Ошибка ввода даты. Правильный формат: yyyy-mm-ddd')
        self.inv_n = inv_n  # Инвентарный номер
        self.get_date = get_date  # Дата приобретения в формате yyyy-mm-ddd
        self.cost = cost  # Стоимость на момент приянтия
        self.name = name  # Наименование, включая производителя и модель


class OfficeEq(WareHouseItem):
    eq_type = 'Оргтехника'

    def __init__(self, inv_n: str, get_date: str, cost: float, name, sn, max_format):
        super().__init__(inv_n, get_date, cost, name)
        self.sn = sn  # Сериный номер
        self.max_format = max_format  # Макисмальный размер формата бумаги


class Printers(OfficeEq):
    eq_type = 'Принтер'

    def __init__(self, inv_n: str, get_date: str, cost: float, name, sn, max_format, print_type,
                 is_color: bool, lan: bool, wifi: bool, duplex: bool):
        super().__init__(inv_n, get_date, cost, name, sn, max_format)
        self.print_type = print_type  # Лазерный, струйный, матричный и.т.д.
        self.is_color = is_color  # Цветной True/False
        self.lan = lan  # Сетевой True/False
        self.wifi = wifi  # Наличие Wi-Fi True/False
        self.duplex = duplex  # Наличие дуплекса True/False


class Scanners(OfficeEq):
    eq_type = 'Сканер'

    def __init__(self, inv_n: str, get_date: str, cost: float, name, sn, max_format, lan: bool,
                 feeder: bool, max_res):
        super().__init__(inv_n, get_date, cost, name, sn, max_format)
        self.lan = lan  # Наличие сети True/False
        self.feeder = feeder  # Наличие автоподатчика True/False
        self.max_res = max_res  # Максимальное разрешение сканирования (в мегапикселях)


class Copier(OfficeEq):
    eq_type = 'Копир'

    def __init__(self, inv_n: str, get_date: str, cost: float, name, sn, max_format,
                 copy_speed, paper_vol):
        super().__init__(inv_n, get_date, cost, name, sn, max_format)
        self.copy_speed = copy_speed  # Скорость копирования
        self.paper_vol = paper_vol  # Объем загрузки бумаги


wh1 = WareHouse()  # Создаем склад

# Создаем и добавляем принтер на склад
printer1 = Printers('151-А', str(datetime.date.today()), 15000, 'HP LaserJet 1100', '011-54441D2', 'A4',
                    'laser', False, False, False, False)
wh1.itm_reception(printer1, 'Бухгалтерия')

# Создаем и добавляем еще один принтер на склад
printer2 = Printers('152-А', str(datetime.date.today()), 25000, 'Kyocera 2020DX', '91544412FN', 'A3',
                    'laser', False, True, True, True)
wh1.itm_reception(printer2, 'Отдел продаж')

# Печатаем состояние склада
print(wh1, '\n')

# Перемещаем хороший принтер из отдела продаж к директору
wh1.itm_move(1, 'Директор')

# Печатаем состояние склада
print(wh1)

"""
Проверяем на ошибки при вводе
"""
try:
    printer3 = Printers('152-А', '25.10.2020', 25000, 'Kyocera 2020DX', '91544412FN', 'A3',
                        'laser', False, True, True, True)
except DateError:
    print('ВНИМАНИЕ!!! Ошибка ввода даты. Проверьте формат даты: гггг-мм-дд')
except ValueError:
    print('ВНИМАНИЕ!!! Ошибка ввода данных. Провеьте корректность ввода')

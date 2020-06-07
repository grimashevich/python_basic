"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных. """


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


class MyDate:
    date = '07-06-2020'

    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_days(cls, date: str):
        """
        Возвращает кол-во дней в указанной дате (кол-во дней от начала летоисчисления)
        :param date: 'dd-mm-yyyy'
        :return: count of the days -> int
        """
        try:
            d, m, y = map(int, (date.split('-')))
        except ValueError:
            return None

        days = y * 365 + (y // 4 - y // 100 + y // 400) - 366  # Отнимаем 366 дней 0-го года, которого как не бы было.
        # Но он должен был быть високосным, по логике

        days += sum([get_days_of_month(y, i) for i in range(m)])
        days += d  # - 1    # -1 Если последний день указанной даты не включаем в расчет
        return days

    @staticmethod
    def check_date(date: str) -> bool:
        """
        Проверяет корректность даты. Возвращает True или False
        :param date: 'dd-mm-yyy'
        :return: bool
        """
        try:
            d, m, y = map(int, (date.split('-')))
        except ValueError:
            return False

        if d == 0:
            return False

        return d in range(get_days_of_month(y, m) + 1)


a = '07-06-2020'
print(f'На конец даты {a} прошло {MyDate.date_to_days(a)} дней с начала новой эры')
print('-'*10)

b = ['30-02-2020', '07-06-2020', '32-01-1900', '01-13-1998', '31-12-1999', '29-02-2000', 'A1-08-2000']
for i in b:
    print(i, MyDate.check_date(i))

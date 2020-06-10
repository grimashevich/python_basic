"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат. """


class Car:
    speed: int
    color: str
    name: str
    is_police: bool
    _is_moving = False

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self._is_moving = True
        print(f'Автомобиль {self.name} пришел в движение')

    def stop(self):
        self._is_moving = False
        print(f'Автомобиль {self.name} становился')

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул {direction}')

    def show_speed(self):
        if self._is_moving:
            print(f'Текущая скорость автомобиля {self.name} = {self.speed} км/ч')
        else:
            print(f'Автомобиль {self.name} не двигается в даный момент')


class SportCar(Car):
    is_police = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PoliceCar(Car):
    is_police = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TownCar(Car):
    speed_limit = 60
    is_police = False

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self._is_moving:
            print(f'Текущая скорость автомобиля {self.name} = {self.speed} км/ч')
            if self.speed > self.speed_limit:
                print(f'Внимание! Максимальная скорость ({self.speed_limit} км/ч) превышена!!!')
        else:
            print(f'Автомобиль {self.name} не двигается в даный момент')


class WorkCar(TownCar):
    speed_limit = 40

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def print_car(car: Car):
    print(f'Создан автомобиль {car.name} цвета {car.color} c макс. скоростью {car.speed}')


sport_car_1 = SportCar(200, 'red', 'Nissan Skyline')
print_car(sport_car_1)
police_car_1 = PoliceCar(150, 'blue', 'Police Ford Focus')
print_car(police_car_1)
town_car_1 = TownCar(65, 'black', 'Toyota Camry')
print_car(town_car_1)
work_car_1 = WorkCar(35, 'white', 'Mazda Bongo')
print_car(work_car_1)

print('')

sport_car_1.go()
police_car_1.go()
sport_car_1.turn('направо')
police_car_1.turn('направо')
sport_car_1.show_speed()
police_car_1.show_speed()
police_car_1.stop()
police_car_1.show_speed()

print('')

town_car_1.go()
town_car_1.show_speed()
town_car_1.turn('налево')
town_car_1.stop()

print('')

work_car_1.go()
work_car_1.show_speed()
work_car_1.turn('направо')
work_car_1.stop()
work_car_1.show_speed()

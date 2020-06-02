"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт. """

import time
import sys


class TrafficLight:
    color = 'red'
    __normal_state = 'red'  # Приватная переменная для проверки корретности преключения
    switch_param = {'red': (7, 'КРАСНЫЙ', '\033[31m'),
                    'yellow': (2, 'ЖЕЛТЫЙ', '\033[33m'),
                    'green': (5, 'ЗЕЛЕНЫЙ', '\033[32m'),
                    }

    def __switch_to_next(self):  # Выполняет непосредтсвенное переключение светофора
        if self.color == 'red':
            self.color = self.__normal_state = 'yellow'
        elif self.color == 'yellow':
            self.color = self.__normal_state = 'green'
        else:
            self.color = self.__normal_state = 'red'

    def switch_color(self):  # Оформляет переключение с задержкой
        if not self.color == self.__normal_state:
            print('\nКто-то взломал светофор, аварийный выход')
            sys.exit()

        switch_sec = self.switch_param[self.color][0]
        rus_title = self.switch_param[self.color][1]
        print_color = self.switch_param[self.color][2]

        for _i in range(switch_sec, 0, -1):
            print_str = '\r' + print_color + rus_title + '\t' + str(_i)
            print(print_str, end='')
            time.sleep(1)
        self.__switch_to_next()


tl1 = TrafficLight()

"""Проверка на корретность порядка переключения светофора"""
# tl1.switch_color()
# tl1.color = 'red'
# tl1.switch_color()

tl_count = ''
while not tl_count.isdigit():
    tl_count = input('Сколько раз переключаем светофор?\n')

    for i in range(0, int(tl_count)):
        tl1.switch_color()

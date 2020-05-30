"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить ее на экран. """

from random import randint

num_str = ''

for i in range(0, 10):
    num_str += str(randint(0, 99)) + ' '
num_str = num_str.strip()

print(num_str)

with open('task5/task5.txt', mode='w', encoding='utf-8') as task5_file:
    task5_file.write(num_str)

with open('task5/task5.txt', mode='r', encoding='utf-8') as task5_file:
    all_num = task5_file.read().split(' ')

print('Сумма чисел: ', sum(map(int, all_num)))

"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл. """


#  Лучше сразу напишу универсальный переводчик (заменяльщик) по словарю. Авось еще сгодится =)
#  Но пока без функции сохранения регистра слов

def multi_replace(source_str: str, repl_dict: dict):
    for key in repl_dict:
        source_str = source_str.replace(key, repl_dict[key])  # replace работает быстрее, чем find. Пруфы в конце
    return source_str


with open('task4/dict.txt', mode='r', encoding='utf-8') as dict_file:
    cur_dict = {}
    for cur_line in dict_file:
        cur_line = cur_line.replace('\n', '')
        cur_line = cur_line.split(':', maxsplit=1)
        cur_dict.update({cur_line[0]: cur_line[1]})

with open('task4/task4.txt', mode='r', encoding='utf-8') as task4_file:
    with open('task4/task4_result.txt', mode='w', encoding='utf-8') as result_file:
        for cur_line in task4_file:
            result_file.write(multi_replace(cur_line, cur_dict))

"""Удивительно, но replace работает быстрее, чем find примерно на 30%. Ниже заготовки для консоли"""
# from time import time
# a = 'Lorem ipsum dolor sit amet, consectetaur adipisicing elit, sed do eiusmod tempor incididunt ut'
# start = time()
# for i in range(0, 10**7):
#     a.find('bbb')
# print(time() - start)
#
# from time import time
# a = 'Lorem ipsum dolor sit amet, consectetaur adipisicing elit, sed do eiusmod tempor incididunt ut'
# start = time()
# for i in range(0, 10**7):
#     a.replace('bbb', 'aaa')
# print(time() - start)

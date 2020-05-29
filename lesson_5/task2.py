"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке. """


def cut_spaces(txt: str):  # Убирает лишние пробелы в строке
    while txt.find('  ') != -1:
        txt = txt.replace('  ', ' ')
    return txt.strip()


with open('task2/task2.txt', mode='r', encoding='utf-8') as r_file:
    file_text = r_file.readlines()

i = 1
words_count = 0

for cur_line in file_text:
    cur_line = cut_spaces(cur_line)
    cur_words = cur_line.count(" ") + 1
    print(f'Строка {i} содержит {cur_words} слов')
    i += 1
    words_count += cur_words

print(f'\nИТОГО в файле {i - 1} строк и {words_count} слов')

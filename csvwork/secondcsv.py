# В csv-файле (разделитель - точка с запятой, кавычки не используются)
# содержится анонимизированная информация о зарплатах сотрудников в различных
# компаниях. В первом столбце записано название компании, а во втором -
# зарплата.
# Поменяйте местами первый и второй столбцы, по-прежнему разделяя значения в
# ячейках одной строки точкой с запятой. Сохраняйте порядок строк.

with open('input (1).csv', 'r', encoding='utf-8') as infile:
    with open('output (1).csv', 'w', encoding='utf-8') as outfile:
        for line in infile:
            print(line.split(';')[1][:-1], line.split(';')[0], sep=';',
                  file=outfile)

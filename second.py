# Дан файл, каждая строка которого может содержать одно или несколько целых
# чисел, разделенных одним или несколькими пробелами.
# Вычислите сумму чисел в каждой строке и выведите эти суммы через пробел
# (для каждой строки выводится сумма чисел в этой строке).

with open('input 2.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        total = 0
        lst = list(line.split())
        for n in lst:
            if n.isdigit():
                total += int(n)
        print(total, end=' ')

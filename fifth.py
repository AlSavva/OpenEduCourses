# Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк.
# Выведите три найденных числа в формате, приведенном в примере. Словом
# считается последовательность больших и маленьких латинских букв (для
# проверки того, состоит ли строка только из латинских букв удобно
# пользоваться методом isalpha()). Все остальные символы считаются
# разделителями слов.

with open('input 5.txt', 'r', encoding='utf-8') as infile:
    letvol = 0
    mylist = ''
    linvol = len(infile.readlines())
    infile.seek(0)
    for letters in infile.read():
        if letters.isalpha():
            letvol += 1
            mylist += letters
        else:
            mylist += ' '
    wordvol = len(mylist.split())
    print(letvol)

    print(f'Letters - {letvol}\n'
          f'Words - {wordvol}\n'
          f'Strings - {linvol}.')

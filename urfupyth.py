# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:55:42 2020

@author: asavv
"""
# Большинство сайтов предоставляет возможность оставить комментарий, поэтому 
# необходимо вести их учет, иногда можно увидеть такую запись:
# Комментарии (28)
# Давайте составим программу, которая будет записывать слово "комментарий" 
# в нужной форме, например:
# 24 комментария
# На вход вашей программе подается число, необходимо вывести слово 
# "комментарий" в нужной форме.

num = input('ooo: ')
my_dict = {'комментарий': [1],
           'комментария': [2, 3, 4],
           'комментариев': [5, 6, 7, 8, 9, 0]
           }
if 11 <= int(num) % 100 <= 19:
    print('комментариев')
else:        
    for key, value in my_dict.items():
        if int(num[-1]) in value:
            print(key)
   
# Напишите программу, которая принимает на вход строку текста и вычисляет 
# количество букв (кириллица, латиница в любом регистре), цифр и специальных 
# символов. При выводе в первой строке указывается количество букв, во второй - 
# количество цифр, в третьей - количество специальных символов.

string = input("__: ")
symb = alph = num = 0
for letter in string:
    if letter.isalpha():
        alph += 1
    elif letter.isdigit():
        num += 1
    else:
        symb += 1
print(alph, num, symb, sep='\n')

# Написать программу для сжатия строки, в которой алгоритм работает следующим 
# образом: string = 'xxxxtttсyyaaa' преобразуется в 'x4t3с1a3', то есть 
# последовательность одинаковых символов строки заменяется на этот символ и 
# количество его повторений в текущей позиции строки.

string = input('__: ')
lst = []
count = 1
tot = string[0]
for i in range(1, len(string)):
    if tot == string[i]:
        count += 1
    else:
        lst.append(tot + str(count))
        tot = string[i]
        count = 1
lst.append(tot + str(count))
for tot in lst:
    print(tot, end='')
    
# Для строки вывести статистику по количеству входящих в нее символов 
# (без учета регистра), сортируя по алфавиту. Игнорируйте всё, кроме букв 
# латиницы и кириллицы. Вывод: символ, пробел, количество. Приоритет вывода у 
# латиницы, вывод символов в нижнем регистре.

string = input('__: ')
string = string.lower()
my_dict = {}
for let in string:
    if ord(let) in range(97, 123) or ord(let) in range(1072, 1104):
        my_dict[let] = string.count(let)
for key, value in sorted(my_dict.items()):
    print(key, value)

# Написать программу, которая из исходной строки оставляет только уникальные 
# слова (без учета регистра), но в том порядке, в котором они первый раз 
# встретились. Слова разделены пробелом, вывод слов в нижнем регистре.

string = input('__: ')
my_list = []
for word in list(string.lower().split()):
    if word not in my_list:
        my_list.append(word)
print(*my_list)

# Дана строка текста (кириллица) со словами через пробел. Среди слов найти все 
# пары анаграмм. Пары анаграмм вывести в алфавитном порядке, среди пар 
# сортировка тоже по алфавиту. Каждая пара выводится в новой строке в нижнем 
# регистре.

string = input()
my_list = list(string.lower().split())
fin_list = set()
for word in my_list:
    for i in range(1, len(my_list)):
        if len(word) != len(my_list[i]) or word == my_list[i]:
            continue
        else:
            my_set = set()
            for j in range(len(word)):
                my_set.add(word[j])
                my_set.add(my_list[i][j])
            if len(my_set) == len(set(word)):
                fin_list.add(tuple(sorted([word, my_list[i]])))
for el in sorted(list(fin_list)):
    print(el[0], el[1])

# Написать программу для транслитерации фамилии, имени, отчества для
# загранпаспорта по установленным МВД РФ требованиям:
        
trans_d = dict(
    [("а", 'a'), ("б", "b"), ("в", 'v'), ("г", 'g'), ("д", 'd'), ("е", 'e'),
     ("ё", 'e'), ("ж", 'zh'), ("з", 'z'), ("и", 'i'), ("й", 'i'), ("к", 'k'),
     ("л", 'l'), ("м", 'm'), ("н", 'n'), ("о", 'o'), ("п", 'p'), ("р", 'r'),
     ("с", 's'), ("т", 't'), ("у", 'u'), ("ф", 'f'), ("х", 'kh'), ("ц", 'ts'),
     ("ч", 'ch'), ("ш", 'sh'), ("щ", 'shch'), ("ы", 'y'), ("ъ", 'ie'),
     ("э", 'e'), ("ю", 'iu'), ("я", 'ia'), ("ь", '')])
fio = list(input().split())
new = []
for word in fio:
    new1 = []
    for i in range(len(word)):
        if word[i].istitle():
            new1.append(trans_d[word[i].lower()].title())
        else:
            new1.append(trans_d[word[i]])
    new.append(''.join(new1))
print(*new)
#
# Во времена кнопочных телефонов была популярна система ввода символов T9. Она
# использовала список известных слов, чтобы из всех возможных комбинаций
# (каждой цифре соответствует несколько букв) оставить только "настоящие"
# слова. Осуществите фильтрацию по нажатым клавишам заданных слов и оставьте
# только те слова, начало которых может быть набрано предложенной комбинацией
# цифр. В первой строке вводится список слов, во второй сочетание клавиш.
# Учитывать только кириллицу.

t9_d = {'1': ".,-",
        "2": "абвг",
        "3": "дежз",
        "4": "ийкл",
        "5": "мноп",
        "6": "рсту",
        "7": "фхцч",
        "8": "шщъы",
        "9": "ьэюя"
        }
text = list(input().split())
num = input()
i = -1
for symb in num:
    i += 1
    for index, word in enumerate(text):
        if len(word) > i and word[i].lower() in t9_d[symb]:
            continue
        else:
            text[index] = '*' * len(word)
for word in text:
    if '*' not in word:
        print(word, end=' ')

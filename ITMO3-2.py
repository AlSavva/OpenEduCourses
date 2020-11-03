# Считать одной строкой произвольное количество пар элементов "Название книги
# Число экземпляров", второй строкой название алгоритма хеширования md5
# Aibolit 66 Barmaley 67
# md5
#
# Создать 2 класса:
# 1-й преобразует строку вида 'Aibolit 66 Babmaley 67', где название книги
# уникально, в словарь.
# 2-й осуществляет хеширования названия книги алгоритмом md5.
# Вывести отдельными операторами вывода:
# - элементы словаря, отсортированные по возрастанию ключа, например:
# Aibolit 66
# Barmaley 67
# - результаты хеширования в виде пар названия алгоритма и результатов
# хеширования ключей, отсортированных по возрастанию, представленных в
# шестнадцатеричном виде, сведенных в одну строку через пробел вида
# md5 c47.... md5 5d....' (без пробелов в начале и конце строки).

import hashlib


class New_dict(object):
    book = {}

    def __init__(self, data):
        self.data = data

    def get_dict(self):
        s = iter(self.data.split())
        for key, val in zip(s, s):
            self.book[key] = val


class Hash_md5(New_dict):

    def __init__(self, enc):
        self.enc = enc
        super(New_dict, self).__init__()

    def get_hash(self):
        for key in sorted(self.book):
            print(key, self.book[key], end="\n")
        for key in sorted(self.book):
            print("md5", hashlib.md5(key.encode()).hexdigest(), end=" ")


new_list = input()
enc = input()
a = New_dict(new_list)
a.get_dict()
b = Hash_md5(enc)
b.get_hash()

# Создайте класс, осуществляющий подсчет и изменение числа книг. Названия
# книг, их количество считываются одной строкой вида
# 'Boogeyman 66 Battleground 50', число книг - произвольное.
# В классе должен быть реализован конструктор, деструктор, методы просмотра
# числа, взятия и возвращения книг.
# Реализовать вывод начальных значений, взятие по 1 книге, возвращение по 1
# книге с выводом текущего числа после вызова каждого из методов, меняющих
# значение книг.
# Типичный ответ одной строкой: 'Boogeyman 66 65 66 Battleground 50 49 50'.


class Biblio:
    def __init__(self, bookstr=input()):
        booklst = list(bookstr.split())
        self.dct = {}
        for i in range(0, len(booklst), 2):
            self.dct[booklst[i]] = [int(booklst[i + 1])]

    def __del__(self):
        self.dct = {}

    def appbook(self, book):
        lbook = list(book.split())
        if lbook[0] in self.dct:
            self.dct[lbook[0]].append(self.dct[lbook[0]][-1] + int(lbook[1]))
        else:
            self.dct[lbook[0]] = [int(lbook[1])]
        # for key, values in self.dct.items():
        #     print(key, *values, end=' ')
        # print('')

    def popbook(self, book):
        lbook = list(book.split())
        if (self.dct[lbook[0]][-1] - int(lbook[1])) < 0:
            self.dct[lbook[0]].append(0)
        else:
            self.dct[lbook[0]].append(self.dct[lbook[0]][-1] - int(lbook[1]))
        # for key, values in self.dct.items():
        #     print(key, *values, end=' ')
        # print('')

    def showinfo(self):
        for key, values in self.dct.items():
            print(key, *values, end=' ')
        print('')


a = Biblio()
a.showinfo()
a.appbook('Boogeyman 1')
a.appbook('Battleground 1')
a.popbook('Boogeyman 1')
a.popbook('Battleground 1')
a.showinfo()
a='hello word python'
b=list('abc')
c=dict(zip(a.split(),b))
d='{a} {b} {c}'.format(**c)
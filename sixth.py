# В качестве ответа введите все строки наибольшей длины из входного файла,
# не меняя их порядок.

with open('input 6.txt', 'r', encoding='utf-8') as infile:
    mydict = {}
    for string in infile.readlines():
        if len(string) not in mydict:
            mydict[len(string)] = []
        mydict[len(string)].append(string[:-1])
    for el in sorted(mydict.items())[-1][1]:
        print(el)





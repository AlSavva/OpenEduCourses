# Ввести с клавиатуры строку латиницей (1-3 слова). Зашифровать ее с
# использованием гарантированных алгоритмов шифрования. Сформировать словарь,
# где в качестве ключа используется название гарантированного алгоритма
# шифрования, а в качестве значения - результат шифрования в шестнадцатеричном
# представлении { 'sha1': 'd0b…', 'md5', '1f3…',…}.
# Итог вывести отдельными операторами вывода в виде пар ключа и значения,
# отсортированных по возрастанию ключа:
# md5 1f3…
# sha1 d0b…

import hashlib

my_frase = input().encode()
hashdct = {'md5': hashlib.md5(my_frase),
           'sha1': hashlib.sha1(my_frase),
           'sha224': hashlib.sha224(my_frase),
           'sha256': hashlib.sha256(my_frase),
           'sha384': hashlib.sha384(my_frase),
           'sha512': hashlib.sha512(my_frase)
           }
for key, value in sorted(hashdct.items()):
    print(key, value.hexdigest())

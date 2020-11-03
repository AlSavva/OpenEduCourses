# Выведите все строки данного входного файла в обратном порядке. Для этого
# считайте список всех строк при помощи метода readlines()

with open('input 4.txt', 'r', encoding='utf-8') as infile:
    print(*infile.readlines()[::-1])

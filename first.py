# Определите, сколько уникальных слов содержится в этом тексте. Словом
# считается последовательность непробельных символов идущих подряд, слова
# разделены одним или большим числом пробелов или символами конца строки.
# Большие и маленькие буквы считаются различными.

with open('input.txt', 'r', encoding='utf-8') as infile:
    unic = []
    b=0
    for line in infile:
        lst = list(line.split())
        a = len(lst)
        b += a
        for word in lst:
            if not word in unic:
                unic.append(word)
print(len(unic), a)

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

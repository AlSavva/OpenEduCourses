# Создайте функцию, которая принимает переменное количество аргументов и находит 
# среднее арифметическое ненулевых из них.
# Обратите внимание на формат вывода

def notnull_mean(lst):
    summ = 0
    num = 0
    for el in lst:
        if el != 0:
            summ += el
            num += 1
    return summ / num if summ % num != 0 else int(summ / num)


#
#
# a = list(map(int, input().split()))
# print(notnull_mean(a))

# Напишите функцию, которая будет возвращать самое длинное слово в предложении. 
# Если найдено более одного слова, то функция возвращает первое.

def longest_word(stg):
    lst = sorted(list(stg.split()), key=lambda x: len(x))
    return lst[-1]


# print(longest_word(input()))

# Напишите функцию, которая возвращает самую длинную неповторяющуюся подстроку 
# для входной строки. Если несколько подстрок совпадают по длине, функция 
# возвращает ту, которая встречается первой.


def long_subs(stg):
    maxlen = 0
    longest = ""
    for i in range(0, len(stg)):
        subs = stg[i:]
        chars = set()
        for j, c in enumerate(subs):
            if c in chars:
                break
            else:
                chars.add(c)
        else:
            # add 1 when end of string is reached (no break)
            # handles the case where the longest string is at the end
            j += 1
        if j > maxlen:
            maxlen = j
            longest = stg[i:i + j]
    return longest


# print(long_subs(input()))

# Строка считается действительной, если все символы в строке встречаются 
# одинаковое количество раз. Также допустимо, если для выполнения этого условия 
# будет достаточно удалить 1 символ из строки. Напишите функцию, которая 
# возвращает True, если строка действительна и False, если нет.

def valid_str(stg):
    valid_set = set(stg)
    if len(stg) % len(valid_set) == 0 or (len(stg) - 1) % len(valid_set) == 0:
        return True
    else:
        return False


# print(valid_str(input()))


# Создайте функцию, которая принимает на вход римское число как строку и 
# преобразует ее в целое число, возвращая результат. Функция должна работать 
# для всех римских цифр, представляющих натуральные числа меньше 4000.

rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def tu_rom(stg):
    global rom_dict
    prev = stg[-1]
    res = rom_dict[prev]
    for cur in stg[-2::-1]:
        if rom_dict[cur] >= rom_dict[prev]:
            res += rom_dict[cur]
        else:
            res -= rom_dict[cur]
        prev = cur
    return res


# print(tu_rom(input()))

# Веб-сайт требует, чтобы пользователи вводили пароль для регистрации, 
# соответствующий определенным требованиям. Напишите программу для проверки 
# правильности ввода пароля пользователями.
# Ниже приведены критерии проверки пароля:
# 1. Минимум 1 буква латинского алфавита в нижнем регистре [az]
# 2. Минимум 1 число от [0–9]
# 3. Минимум 1 буква латинского алфавита в верхнем регистре [AZ]
# 4. Минимум 1 специальный символ
# 5. Минимальная длина пароля : 6
# 6. Максимальная длина пароля: 12
# Программа должна возвращать True или False.

def pas_valid(stg):
    if 12 < len(stg) < 6:
        return False
    valid_dict = {
        'is_symb': False,
        'is_digit': False,
        'is_upp': False,
        'is_low': False
    }
    for char in stg:
        if not char.isalnum():
            valid_dict['is_symb'] = True
        elif char.isdigit():
            valid_dict['is_digit'] = True
        elif char.isupper():
            valid_dict['is_upp'] = True
        elif char.islower():
            valid_dict['is_low'] = True
        if all(valid_dict.values()):
            return True
    return False


print(pas_valid(input()))

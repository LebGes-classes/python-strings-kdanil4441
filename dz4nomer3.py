st = input('Введите текст: ')

tempDict = {}

russian_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
russian_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
english_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
english_lower = 'abcdefghijklmnopqrstuvwxyz'

for char in st:
    if char in russian_upper:
        index = russian_upper.index(char)
        lower_st += russian_lower[index]
    elif char in english_upper:
        index = english_upper.index(char)
        lower_st += english_lower[index]
    else:
        lower_st += char

words = []
cur_word = ''

for s in lower_st:
    if s == ' ':
        if cur_word:
            words.append(cur_word)
            cur_word = ''
    else:
        cur_word += s

if cur_word:
    words.append(cur_word)

for word in words:
    if word not in tempDict:
        tempDict[word] = 1
    else:
        tempDict[word] += 1

sorted_items = []

for word, count in tempDict.items():
    sorted_items.append((count, word))

n = len(sorted_items)

for i in range(n):
    for j in range(0, n - i - 1):
        if sorted_items[j][0] < sorted_items[j + 1][0]:
            sorted_items[j], sorted_items[j + 1] = sorted_items[j + 1], sorted_items[j]

for i in range(min(5, n)):
    count, word = sorted_items[i]
    print(word, count)

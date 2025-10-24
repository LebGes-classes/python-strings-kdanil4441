text = input('Введите текст: ')

words = []
cur_word = ''
prev_char = ''

for ch in text:
    if ch == ' ':
        if prev_char != ',':
            if cur_word:
                words.append(cur_word)
                curr_word = ''
    elif ch == '.' or ch == ',':
        if cur_word:
            words.append(cur_word)
            curr_word = ""
    else:
        cur_word += ch
    prev_char = ch

if cur_word:
    words.append(cur_word)

max_len = 0
for w in words:
    if len(w) > max_len:
        max_len = len(w)

low_abc = 'abcdefghijklmnopqrstuvwxyz'
high_abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

coded_text = ''

for ch in text:
    if ch in high_abc:
        coded_text += high_abc[(high_abc.index(ch) + max_len) % 26]
    elif ch in low_abc:
        coded_text += low_abc[(low_abc.index(ch) + max_len) % 26]
    else:
        coded_text += ch

print(coded_text)
print('K =', max_len)
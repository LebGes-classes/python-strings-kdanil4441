text = input('Введите текст: ')
result_letters = ''
result_words = ''
cur_word = ''

for symbol in text:
    if symbol != ' ':
        cur_word += symbol
    else:
        reversed_word = ''

        for i in range(len(cur_word) - 1, -1, -1):
            reversed_word += cur_word[i]
        result_letters += reversed_word + ' '

        if result_words:
            result_words = cur_word + ' ' + result_words
        else:
            result_words = cur_word

        cur_word = ''

if cur_word:
    reversed_word = ''

    for i in range(len(cur_word) - 1, -1, -1):
        reversed_word += cur_word[i]
    result_letters += reversed_word

    if result_words:
        result_words = cur_word + ' ' + result_words
    else:
        result_words = cur_word

print(result_letters)
print(result_words)
def print_middle(word):
    middle = None
    word_length = len(word)
    if word_length % 2 == 1:
        middle = word[word_length // 2]
    else:
        middle_index = word_length // 2
        middle = word[middle_index-1:middle_index+1]
    print(f'word={word}. Результат: {middle}')


word = 'testing'

print_middle(word)

word = 'test'

print_middle(word)

try:
    word_num = int(input('Enter the number of words: '))
    words_list = []
    words_sum = {}
    for i in range(word_num):
        word = input('Enter the word: ')
        words_list.append(word)
        if word in words_sum:
            words_sum[word] += 1
        else:
            words_sum[word] = 1
    print(len((words_sum.keys())))
    for i in list(words_sum.values()):
        print(i, end=' ')

except (ValueError, NameError):
    print('Please enter only a natural number!')




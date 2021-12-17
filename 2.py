ex.2

def bigger_Is_greater(w):
    import itertools
    words_list = []
    for i in list(itertools.permutations(w,len(w))):
        words_list.append(''.join(i))
    res = list(set(words_list))
    res.sort()
    words = res[::-1]
    index = words.index(w)
    word = words[index-1]
    if index != 0:
        return word
    else:
        return 'no answer'


try:
    word_num = int(input('Enter the number of words: '))
    result = []
    for i in range(word_num):
        word = input('Enter the word: ')
        result.append(bigger_Is_greater(word))
    for i in result:
        print(i)

except (ValueError, NameError):
    print('Please enter only a natural number!')

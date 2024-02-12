def duplicate_encode(word):
    word = word.lower()
    result = ''

    for i in word:
        if word.count(i) > 1:
            result += ')'
        else:
            result += '('

    return result


print(duplicate_encode('recede'))
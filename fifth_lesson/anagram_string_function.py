def anagram(first_string, second_string):
    str1 = sorted(first_string.lower())
    str2 = sorted(second_string.lower())

    if str1 == str2:
        return True
    else:
        return False


print(anagram('listen', 'silent'))

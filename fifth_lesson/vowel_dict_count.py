def dict_vowel_count(*args):
    vowel_dict = dict()
    vowel = 'aeiou'
    my_string = ' '.join(i for i in args)

    for i in my_string.lower():
        if i in vowel:
            vowel_dict[i] = my_string.count(i)

    return vowel_dict


print(dict_vowel_count('serhii', 'evheniy', 'oleg'))

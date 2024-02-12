def len_of_vowel(my_string):
    vowel = 'aeiouAEIOU'

    vowel_string = ''.join(i for i in my_string if i in vowel)
    return len(vowel_string)


print(len_of_vowel('Hello Serhii! You are amazing'))

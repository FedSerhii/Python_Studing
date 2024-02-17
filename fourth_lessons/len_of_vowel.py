my_string = str(input())
vowel = 'aeiouAEIOU'

vowel_string = ''.join(i for i in my_string if i in vowel)
print(len(vowel_string))
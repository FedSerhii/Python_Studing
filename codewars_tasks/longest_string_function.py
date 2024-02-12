def longest_consec(strarr, k):

    if len(strarr) == 0 or k <=0 or k > len(strarr):
        return ''

    longest_word = ''
    for i in range(len(strarr) - k + 1):
        longest_string = ''.join(strarr[i:i + k])
        if len(longest_string) > len(longest_word):
            longest_word = longest_string

    return longest_word


print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2))
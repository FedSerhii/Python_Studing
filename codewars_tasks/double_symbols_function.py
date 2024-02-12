def accum(st):
    return '-'.join([char.upper() + char.lower() * index for index, char in enumerate(st)])


print(accum('abcdsw'))

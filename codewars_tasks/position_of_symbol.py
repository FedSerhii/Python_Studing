text = 'The sunset sets at twelve o"clock'


def alphabet_position(text):
    positions = []

    for i in text:
        if i.isalpha():
            i = i.upper()
            position = ord(i) - ord('A') + 1
            positions.append(str(position))

    return ' '.join(positions)


print(alphabet_position(text))

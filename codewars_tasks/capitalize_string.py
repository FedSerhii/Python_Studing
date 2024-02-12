string = 'How can mirrors be real if our eyes aren'


def to_jaden_case(string):
    list_of_string = string.split()
    cap_list = [i.capitalize() for i in list_of_string]
    l = ' '.join(cap_list)

    return l


print(to_jaden_case(string))

def title_case(title, minor_words=''):

    new_title = title.split()
    low_list1 = [i.lower() for i in new_title]
    low_list2 = [i.lower() for i in minor_words.split()]
    result = []

    for key, value in enumerate(low_list1):
        if key == 0 or value not in low_list2:
            result.append(value.capitalize())
        else:
            result.append(value)

    return ' '.join(result)


print(title_case('THE WIND IN THE WILLOWS', 'The In'))
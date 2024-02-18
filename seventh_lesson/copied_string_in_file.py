def copied_file(origin, copied):

    file1 = open(origin, 'r')
    text1 = file1.read()
    file1.close()

    file2 = open(copied, 'w')
    file2.write(text1)
    file2.close()



    # with open(origin, 'r') as file1:
    #     origin_text = file1.read()
    #     with open(copied, 'w') as file2:
    #         file2.write(origin_text)


copied_file('my_file.txt', 'new_file.txt')
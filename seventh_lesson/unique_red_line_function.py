def unique_line(first_file, second_file):
    try:
        file1 = open(first_file, 'r')
        lines1 = file1.readlines()
        file1.close()

        file2 = open(second_file, 'r')
        lines2 = file2.readlines()
        file2.close()

        lines1 = [line.strip() for line in lines1]
        lines2 = [line.strip() for line in lines2]

        return [line for line in lines1 if line not in lines2]

    except FileNotFoundError:
        print('File doesn"n exist!')
        return None
    except Exception as e:
        print('An error occurred while processing files: ', e)
        return None


    # with open(first_file, 'r') as file1:
    #     for line in file1:
    #         list1.append(line.strip())
    #
    # with open(second_file, 'r') as file2:
    #     for line in file2:
    #         list2.append(line.strip())
    #
    # return [i for i in list1 if i not in list2]



print(unique_line('my_file.txt', 'new_file.txt'))
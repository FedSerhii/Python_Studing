def deleted_line(file_path, del_line):
    try:
        file = open(file_path, 'r+')
        lines = file.readlines()
        file.seek(0)

        for i in lines:
            if i.strip() != del_line:
                file.write(i)

        file.truncate()
        file.close()
    except FileNotFoundError:
        print('File doesn"n exist!')
        return None
    except Exception as e:
        print('An error occurred while processing files: ', e)
        return None






    # with open(file_path, 'r+') as file:
    #     line = file.readlines()
    #     file.seek(0)
    #
    #     for i in line:
    #       if i.strip() != del_line:
    #           file.write(i)
    #
    #     file.truncate()


deleted_line('my_file.txt', 'И боишься')
def deleted_line(file_path, del_line):
    with open(file_path, 'r+') as file:
        line = file.readlines()
        file.seek(0)

        for i in line:
          if i.strip() != del_line:
              file.write(i)

        file.truncate()


deleted_line('my_file.txt', 'И боишься')
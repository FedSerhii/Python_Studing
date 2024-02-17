my_string = str(input())

sub_string = ''.join(i for i in my_string if i.isalpha())
print(sub_string)
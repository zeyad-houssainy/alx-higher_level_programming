#!/usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)
    # print(my_string)
    for i in my_string:
        print(i)
        if i == 'c':
            my_string.remove('c')
        if i == 'C':
            my_string.remove('C')
    my_string = "".join(my_string)
    return my_string


    
    
    



print(no_c("ABcCD"))
# print(no_c("Chicago"))
# print(no_c("C is fun!"))

def print_odd(some_list):
    new_list=[]

    for i in range(len(some_list)):
        if some_list[i]%2!=0:
            new_list.append(some_list[i])



    return new_list

a=[1,2,3,4,5,7]
print(print_odd(a))

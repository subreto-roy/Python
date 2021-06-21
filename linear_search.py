def linear_search(some_list,value):
    for i in range(len(some_list)):
        if some_list[i]==value:
            return "Found"
    if i==len(some_list)-1:
        return "Not Found"

a=[1,2,3,4]

print(linear_search(a,2))

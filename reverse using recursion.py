

def reverse_list(some_list):
    if len(some_list)==0:
        return []
    return [some_list[-1]]+reverse_list((some_list[:-1]))


lists=[1,2,3,4]
print(reverse_list(lists))

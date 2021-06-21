def binary_search(some_list,value):


    if value>some_list[-1]:
        return 'Not found'

    first=0
    last=len(some_list)-1

    while first<=last:
        mid=(first+last)//2

        if some_list[mid]==value:
            return 'found'
        elif some_list[mid]>value:
            first=mid+1
        elif some_list[mid]<value:
            last=mid-1

    if first > last:
     return "not found"

a=[1,2,3,4,5]
print(binary_search(a,4))


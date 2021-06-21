class Toy:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def sort_priority(self):
        return self.price

def print_toy_objects(toy_list):
    for obj in toy_list:
        print(f'Toy:{obj.name},price:{obj.price}')


toy_1=Toy('Woody',1000)
toy_2=Toy('Act-wheels',200)
toy_3=Toy('a',10)

toys=[toy_1,toy_2,toy_3]


#using the sort functions
toys.sort(key=Toy.sort_priority)

print_toy_objects(toys)

#using the sorted function
sorted_toys=sorted(toys,key=Toy.sort_priority)

print_toy_objects(sorted_toys)

result=lambda x,y,z: x + y + z

print(result(1,2,3))

#using the lambba function with sort()

toys_again=[toy_1,toy_2,toy_3]

toys_again.sort(key=lambda x: x.price)

print_toy_objects(toys_again)


sorted_toys_again=sorted(toys, key=lambda x:x.price)

print_toy_objects(sorted_toys_again)







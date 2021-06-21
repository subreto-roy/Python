"""
a={1: 1,2:2,3:1,4:34}
b={}
count={}
for i in a.values():
    count.setdefault(i,0)
    count[i]=count[i]+1

i=0

for k,v in count.items():
    if v == 1:
        b.update({i: k})
        i=i+1

for k in b.values():
    print(i,end=" ")
"""
d={"name":"m","salary":1800}
temp=d.pop("age")
print(temp)

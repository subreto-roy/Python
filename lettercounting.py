import pprint as pp
text= 'this is a simple text to TEST the code.'

letters={}

for i in text:
    letters.setdefault(i,0)
    letters[i]=letters[i]+1

pp.pprint(letters)

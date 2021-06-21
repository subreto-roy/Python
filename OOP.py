class StoryBook:

    #class VARIable
    no_of_book=0

    discount=0.5





    #dander method
    def __init__(self,name,price,author_name,author_born,no_of_pages):
       # print('I am being called with instance/object creating')
      self.name=name
      self.price=price
      self.author_name=author_name
      self.author_born=author_born
      self.publishing_year=2010
      self.no_of_pages=no_of_pages
      StoryBook.no_of_book+=1

    #regular method
    def get_book_info(self):
        print(f'The book name:{self.name},price:{self.price},pages:{self.no_of_pages}')

    def get_author_info(self):
        print(f'The author name:{self.author_name},born: {self.author_born}')


    def apply_discount(self):
        self.price=int(self.price-self.price*StoryBook.discount)


#creating an instance/object of the StoryBook class
book_1=StoryBook('kil',324,'sjia',1243,400)
book_2=StoryBook('dsad',3242,'sdf',1123,345)
#instance variable
#book_1.name='Hamlet'
#book_1.price=350

#print(book_1.name)
#print(book_2.name)

#book_1.get_book_info()
#book_1.get_author_info()
#StoryBook.get_book_info(book_1)
print(book_2.price)
book_2.apply_discount()
print(book_2.price)

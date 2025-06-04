# def get_list(numbers:list):
#     new_numbers = [num*num for num in numbers]
#     return new_numbers
# print(get_list([1,2,3,4]))


# def get_golosni(sent:str):
#     golosni = 'aeiou'
#     sent = sent.lower()
#     count = 0
#     for gl in sent:
#         if gl in golosni:
#             count+=1
#     return count
#
# print(get_golosni('123123wwawwa'))


class isPositive:
    def __set_name__(self, owner, name):
        self.private_name = f'_{name}'

    def __get__(self,obj,objtype = None):
        return getattr(obj,self.private_name)

    def __set__(self, obj, value):
        if not isinstance(value, int) or value<=0:
            print("WRONG VALUE NIGGA")
            return
        setattr(obj,self.private_name,value)


class Book:

    year = isPositive()


    def __init__(self,title,author,year):
         self.title = title
         self.author = author
         self.year = year

    @property
    def get_title(self):
        return self.title

    @property
    def get_author(self):
        return self.author




class Library:

    def __init__(self):
        self.book_shelf = []


    def add_book(self,book):
        if isinstance(book,Book):
            for bk in self.book_shelf:
                if bk.title == book.title and bk.author == book.author:
                    print("THIS BOOK IS ALREADY ADDED nigga")
                    return
            self.book_shelf.append(book)

    def find_by_author(self,author):
        return [book for book in self.book_shelf if book.author.lower() == author.lower()]

    def oldest_book(self):
        if self.book_shelf ==[]:
            return
        oldestBook = self.book_shelf[0]
        for b in self.book_shelf:
            if b.year <oldestBook.year:
                oldestBook = b
        return oldestBook

    def __call__(self):
        cnt = len(self.book_shelf)
        oldest = self.oldest_book()
        if oldest:
            return f'In library = {cnt} books \n Oldest book = {oldest.title},year = {oldest.year}'
        else:
            return "library is empty NIGGA"


lib = Library()
b1 = Book("123", "123123", 1)
b2 = Book("1", "1", 2)

lib.add_book(b1)
lib.add_book(b2)

print(lib())
print([b.title for b in lib.find_by_author("123123")])


class Book:
    def __init__(self, book_id, book_name, aut_book):
        self.book_id = book_id
        self.book_name = book_name
        self.aut_book = aut_book
class   Library(Book):
    def __init__(self,book_list,libraryAdress):
        self.book_list=book_list
        self.libraryAdress=libraryAdress
    def method1(self):
        aut_dict={}
        autLis=[]
        for obj in self.book_list:
            autLis.append(obj.aut_book.upper())
        authors=list(set(autLis))
        for aut in authors:
            aut_dict[aut]=autLis.count(aut)
        return aut_dict
    def method2(self,city_n,lib_list):
        books=[]
        for obj in lib_obj:
            for k,v in obj.libraryAdress.items():
                if v==city:
                    tempBooks=[]
                    for book_obj in obj.book_list:
                        tempBooks.append(book_obj.book_name)
                    tempBooks.reverse()
                    books=books+tempBooks
        return books
    
lib_obj=[]
n=int(input())
for _ in range(n):
        book_list=[]
        libraryAdress={}
        for _ in range(int(input())):
            book_id=int(input())
            book_name=input()
            aut_book=input()
            book_list.append(Book(book_id,book_name,aut_book))
        libraryAdress['street'] =input()
        libraryAdress['area'] =input()
        libraryAdress['city'] =input()
        libraryAdress['state'] =input()
        libraryAdress['zip_c'] =int(input())
        lib_obj.append(Library(book_list,libraryAdress))
    
city=input()
for j in range(n):
    obj=lib_obj[j]
    res=obj.method1()
    print(*res.keys(),*res.values())
books=obj.method2(city,lib_obj)
print(books)
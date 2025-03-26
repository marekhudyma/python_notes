mylist = [1,2,3]
len(mylist)

# class Sample():
#     pass
#
# mysample = Sample()
# len(mysample) # TypeError: object of type 'Sample' has no len()

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author} {self.pages} pages"
    def __del__(self):
        print("A book object has been deleted")

b = Book("Python roks", "Jose", 200)
print(b)
# <__main__.Book object at 0x10149dfd0>
# Python roks by Jose 200 pages

del b # A book object has been deleted
# print(b) # NameError: name 'b' is not defined
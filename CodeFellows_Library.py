'''
Created on Apr 16, 2014

@author: Duy Tran
'''

class Library:
    def __init__(self, name):
        self.name = name
        self.shelves = []
    def addShelf(self, shelf):
        self.shelves.append(shelf)
    def report(self):
        print "Duy's Library Content: "
        for x in self.shelves:
            x.report()

class Shelf:
    count = 0
    def __init__(self, name = count):
        self.name = name
        self.books = []
        Shelf.count += 1
    def addBook(self, book):
        self.books.append(book)
    def report(self):
        printout = self.name + ": "
        for x in self.books:
            printout += str(x.name) + " | "
        print printout
        
class Book:
    count = 0
    def __init__(self, shelf, name = "book"):
        self.name = name +"_" + str(Book.count)
        self.shelf = shelf
        Book.count += 1
    def enshelf(self, shelf):
        shelf.books.append(self)
        self.shelf = shelf
        print "Putting book "+str(self.name)+" onto shelf "+str(shelf.name)+"."
    def unshelf(self):
        self.shelf.books.remove(self)
        print "Removing book "+str(self.name)+" from shelf "+str(self.shelf.name)+"."
        self.shelf = None
        return self
    def report(self):
        print self.name
        
                
duy_lib = Library("Duy's Library")
for i in range(1, 6):
    duy_lib.addShelf(Shelf("SH"+str(i)))
for s in duy_lib.shelves:
    for i in range (1, 6):
        s.addBook(Book(s, "book"))

    
duy_lib.report()

shelf_1 = duy_lib.shelves[0]
shelf_5 = duy_lib.shelves[4]
print ""
temp = shelf_1.books[4].unshelf()
temp.enshelf(shelf_5)
print ""
temp = shelf_5.books[2].unshelf()
temp.enshelf(shelf_1)
print ""
duy_lib.report()
print "Done"
class Book:

    author=""
    title=""
    
    def __init__(self, author, title):
        self.author = author
        self.title = title
        
    def display(self):
        print('%s, written by %s' % (self.title, self.author))
        
book1 = Book('Of Mice and Men','John Steinbeck')
book2 = Book('To Kill a Mockingbird','Harper Lee')

book1.display()
book2.display()
    
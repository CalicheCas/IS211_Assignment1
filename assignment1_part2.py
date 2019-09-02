class Book:
    """
    Simple Book class to represent Book object.
    
    Parameter:
    ----------
    Author: str
        Book Author.
    
    Title: str
        Book title
    
    """

    author=""
    title=""
    
    def __init__(self, author, title):
        self.author = author
        self.title = title
        
    def display(self):
        """Print Author name and book title."""
        print('%s, written by %s' % (self.title, self.author))
        
book1 = Book('Of Mice and Men','John Steinbeck')
book2 = Book('To Kill a Mockingbird','Harper Lee')

book1.display()
book2.display()
    
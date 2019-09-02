def listDivide(numbers, divide=2):
    """Returns total number of elements in a given list (`numbers`) that are divisibe by `divide`.
    
    Parameters
    -----------
    numbers: List[]
        Lit containing integer elements.
        
    divide: int, defaultvalue = 2
        Divisor. Each element in the list will be divided by this parameter.
    
    Raises:
    -------
    ListDivideException error
        
    >>>numbers = [1 2, 3, 4]
    >>>listDivide(numbers, divide)
    >>>2
    
    >>>numbers = [3, 6, 9, 10]
    >>>3
    >>>listDivide(numbers, divide)
    >>>3
    """  
    counter = 0
    for num in numbers:
        if num % divide == 0:
            counter+=1
    return counter
    
class ListDivideException(Exception):
    """Raised when listDivide fails"""
    pass
    
def testListDivide():
    """Performs tests on function listDivide"""
    #a
    numbers = [1,2,3,4,5]
    expected = 2
    
    try:
        assert listDivide(numbers) == expected
    except AssertionError:
        raise ListDivideException("Test Failed")
        
    
    #b
    numbers = [2,4,6,8,10]
    expected = 5
    
    try:
        assert listDivide(numbers) == expected
    except AssertionError:
        raise ListDivideException("Test Failed")    
    
    #c
    numbers = [30, 54, 63, 98, 100]
    divide = 10
    expected = 2
    
    try:
        assert listDivide(numbers, divide) == expected
    except AssertionError:
        raise ListDivideException("Test Failed")    
    
    #d
    numbers = []
    expected = 0
    
    try:
        assert listDivide(numbers) == expected
    except AssertionError:
        raise ListDivideException("Test Failed")    
    
    #e
    numbers = [1, 2, 3, 4, 5]
    divide = 1
    expected = 5
    
    try:
        assert listDivide(numbers, divide) == expected
    except AssertionError:
        raise ListDivideException("Test Failed")  
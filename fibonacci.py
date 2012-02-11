#!/usr/bin/env python3.2
# encoding: utf-8
"""
implementing an iterator from scratch

+ python classes 101


an iterator is just a class that defines an __iter__() method
"""

# self
# The first argument of every class method, including the __init__() method, is
# always a reference to the current instance of the class. By convention, this
# argument is named self. 
# In all class methods, self refers to the instance whose method was called.
class Fib:
    '''iterator that yields numbers in the Fibonacci sequence'''


    # The __init__() method is called immediately after an instance of the class is
    # created. It would be tempting — but technically incorrect — to call this the
    # “constructor” of the class. It’s tempting, because it looks like a C++
    # constructor (by convention, the __init__() method is the first method defined
    # for the class), acts like one (it’s the first piece of code executed in
    # a newly created instance of the class), and even sounds like
    # one. Incorrect, because the object has already been constructed by the
    # time the __init__() method is called, and you already have a valid
    # reference to the new instance of the class.
    def __init__(self, max):
        self.max = max  #instance variable

    # The __iter__() method is called whenever someone calls iter(fib). 
    # in essense __iter__ returns an iterator object.
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self #the __iter__() method can return any object that implements a __next__() method

    # The __next__() method is called whenever someone calls next() on an iterator of an instance of a class.
    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration # this signals to the caller that the iteration is exhausted.
        self.a, self.b = self.b, self.a + self.b
        return fib


if __name__ == '__main__':
    fib = Fib(100)
    fib2 = Fib(200)

    # Every class instance has a built-in attribute, __class__, which is the object’s class.
    print( fib.__class__ )
    print(fib.__doc__)
    print(fib.max)
    print(fib2.max)
    
    for n in Fib(1000):
        print(n, end=' ')
    print()


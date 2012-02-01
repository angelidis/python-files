#!/usr/bin/env python3.2
"""
having fun with python3 tuples

The major difference between tuples and lists is that tuples can not be
changed.  Lists have methods like append(), extend(), insert(), remove(), and
pop(). Tuples have none of these methods.

Tuples are faster than lists. If you’re defining a constant set of values and
all you’re ever going to do with it is iterate through it, use a tuple instead
of a list.

check:
http://diveintopython3.ep.io/native-datatypes.html
"""

if __name__ == '__main__':

    a_tuple = ("a", "b", "mpilgrim", "z", "example")
    print(a_tuple[0])
    print(a_tuple[:])

    # convert lists <-> tuples

    # Tuples can be converted into lists, and vice-versa. The built-in tuple()
    # function takes a list and returns a tuple with the same elements, and the
    # list() function takes a tuple and returns a list. In effect, tuple() freezes a
    # list, and list() thaws a tuple.

    a_tuple = ("a", "b", "mpilgrim", "z", "example")
    a_list = [ 'a', 'b', 'c']

    b_list = list(a_tuple)
    b_tuple = tuple(a_list)
    # tuple of 1 item

    # To create a tuple of one item, you need a comma after the value. Without the
    # comma, Python just assumes you have an extra pair of parentheses, which is
    # harmless, but it doesn’t create a tuple.

    print( type((False))  ) # <class 'bool'>
    print( type((False,)) ) # <class 'tuple'>

    # Assigning Multiple Values At Once
    v = ( 'a', 2, True )
    (x, y, z) = v

    print(y)
    print(type(y) ) # <class 'int'>

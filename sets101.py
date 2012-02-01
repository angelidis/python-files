#!/usr/bin/env python3.2
"""
having fun with python3 sets


A set is an unordered “bag” of unique values. A single set can contain values
of any immutable datatype. Once you have two sets, you can do standard set
operations like union, intersection, and set difference.

check:
http://diveintopython3.ep.io/native-datatypes.html
"""

if __name__ == '__main__':

    a_set = {1, 2}
    type(a_set) # <class 'set'>
    print(a_set)
    a_list = ['a', 'b', 'mpilgrim', True, False, 42]
    a_set = set(a_list)
    print(a_set)

    # unique values
    print ('unique values')
    a_set = {1, 1}
    print(a_set) # {1}


    # empty sets
    # To create an empty set, call set() with no arguments.
    a_set = set()
    print( a_set ) # set() 
    type(a_set) # <class 'set'>
    len(a_set) # 0

    not_sure = {} #creates an empty dictionary
    type(not_sure) # <class 'dict'>

    #update sets
    a_set = {1, 2}
    a_set.add(4)
    len(a_set) 
    a_set.update({2, 4, 6})
    a_set.update({3, 6, 9}, {1, 2, 3, 5, 8, 13})
    300 in a_set  # false!
    a_set.update([100, 200, 300])
    print( a_set ) 
    300 in a_set  # true!


    # Set actions
    # union()
    # intersection()
    # difference()
    # symmetric_difference() 
    b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
    print( a_set.union(b_set) )
    print( a_set.intersection(b_set) )
    print( a_set.difference(b_set) )
    print( a_set.symmetric_difference(b_set) )
    print( b_set.union(a_set) == a_set.union(b_set)   )


    a_set = {1, 2, 3}
    b_set = {1, 2, 3, 4}
    a_set.issubset(b_set) # True
    b_set.issuperset(a_set) # True
    a_set.add(5)
    a_set.issubset(b_set) # False
    b_set.issuperset(a_set) # False

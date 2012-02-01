#!/usr/bin/env python3.2
"""
having fun with python3 lists

check:
http://diveintopython3.ep.io/native-datatypes.html
"""

if __name__ == '__main__':
    # Lists
    #python's workhorse
    a_list = ['a', 'b', '3', 'an example']

    print(a_list[0])
    print(a_list[3])
    print(a_list[-1])
    print(a_list[-2])

    #slice
    print(a_list[1:]) # the empty slot implies the length of the list ie 4
                      # if we had [:3] then we would imply 0
                      # thus [:] is shorthand for making a complete copy of a list
                      # this is not the same as the original a_list variable. It is a new list that
                      # happens to have all the same items. a_list[:] is shorthand for making a
                      # complete copy of a list.

    print(a_list[1:2]) #semi open range, thus it is the same with a_list[1]
    # The return value is a new list containing all the items of the list, in
    # order, starting with the first slice index (in this case a_list[1]), up to
    # but not including the second slice index (in this case a_list[3]).

    print(a_list[1:-1])
    # Slicing works if one or both of the slice indices is negative. If it helps, you
    # can think of it this way: reading the list from left to right, the first slice
    # index specifies the first item you want, and the second slice index specifies
    # the first item you don’t want. The return value is everything in between.

    # adding stuff to a list
    a_list = a_list + [2.0, 3]
    a_list.append(True)
    a_list.extend(['four', 'Ω'])
    a_list.insert(0, 'Ω')
    print(a_list[:])

    # adding stuff to a list (append vs extend)
    # append
    a_list = [ 'a', 'b', 'c']
    a_list.extend( ['d', 'e', 'f'])
    print( a_list[:] )
    print( len(a_list) )
    print( a_list[-1] )

    # extend
    a_list.append( ['g', 'h', 'i'])
    print( a_list[:] )
    print( len(a_list) )
    print( a_list[-1] )

    #search list
    a_list = ['a', 'b', 'new', 'mpilgrim', 'new']
    print ( a_list.count('new') )
    print ( 'new' in a_list )
    print ( a_list.index('mpilgrim') )

    # remove elements from list
    print( 'remove elements from list' )
    # (1) by positional index (2) by value instead.

    print( a_list[:] )
    print( a_list[1] )
    del a_list[1]
    print( a_list[1] )
    a_list.remove('new') #removes the first occurence
    print( a_list[:] )

    # pop() list method removes the last item in the list and returns the value it removed
    print( 'pop()' )
    a_list = ['a', 'b', 'new', 'mpilgrim']
    print( a_list[:] )
    print (a_list.pop() )
    print( a_list[:] )
    print (a_list.pop(0) )
    print( a_list[:] )

    # Empty lists are false; all other lists are true.

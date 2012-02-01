#!/usr/bin/env python3.2
# encoding: utf-8


import glob
import os

def pretty_print(list):
    """pretty print a list
    
    :list: @todo
    :returns: @todo
    """
    pass

if __name__ == '__main__':

    #########################
    #  list comprehensions  #
    #########################

    pathname = print(os.path.join(os.path.expanduser('~'), 'projects', 'python'))
    pylist = glob.glob('*.py')
    v = [os.path.realpath(pyfile) for pyfile in pylist ]
    print(v)


    # comprehensions with filters
    print('# comprehensions with filters')
    v = [ (os.path.realpath(pyfile), pyfile ) for pyfile in pylist if os.stat(pyfile).st_size > 2000 ]
    print(v)

    ###############################
    #  dictionary comprehensions  #
    ###############################
    metadata = [(f, os.stat(f)) for f in glob.glob('*.py')]
    # metadata[0] #list compreh

    metadata_dict = {f:os.stat(f) for f in glob.glob('*.py')}

    type(metadata_dict) # <class 'dict'>

    list(metadata_dict.keys())
    metadata_dict['os101.py'].st_size        


    # swap key, value in a dictionary
    a_dict = {'a': 1, 'b': 2, 'c': 3}

    a_swap = { value:key for (key, value) in a_dict.items() }
    print ( a_swap )

    ########################
    #  set Comprehensions  #
    ########################


    # Not to be left out, sets have their own comprehension syntax as well. It is
    # remarkably similar to the syntax for dictionary comprehensions. The only
    # difference is that sets just have values instead of key:value pairs.

    a_set = set(range(10))
    b_set = {x ** 2 for x in a_set}
    print ( b_set )

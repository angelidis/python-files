#!/usr/bin/env python3.2
# encoding: utf-8


def fib(max):
    a,b = 0,1
    while a < max:
        yield a
        a, b = b, a+b


if __name__ == '__main__':
    for n in fib(1000):
        print(n, end=' ')

    print('done!')


    # This is a useful idiom: pass a generator to the list() function, and it
    # will iterate through the entire generator (just like the for loop in the
    # previous example) and return a list of all the values.
    li = list( fib(1000) )
    print( li )

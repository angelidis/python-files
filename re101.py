#!/usr/bin/env python3.2
# encoding: utf-8
"""

To work around the backslash plague, you can use what is called a raw string,
by prefixing the string with the letter r. This tells Python that nothing in
this string should be escaped; '\t' is a tab character, but r'\t' is really the
backslash character \ followed by the letter t. I recommend always using raw
strings when dealing with regular expressions; otherwise, things get too
confusing too quickly (and regular expressions are confusing enough already).



The essence of the re module is the search() function, that takes a regular
expression (pattern) and a string ('M') to try to match against the regular
expression. If a match is found, search() returns an object which has various
methods to describe the match; if no match is found, search() returns None, the
Python null value



"""

import re

if __name__ == '__main__':
    # re.sub(r'\bROAD$', 'RD.', s)


    #verbose regular expression

    pattern = '''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    '''
    re.search(pattern, 'M', re.VERBOSE) 

    #subs


    print(      re.sub('[abc]','o','Mark')     )
    print(      re.sub('[abc]','o','Rock')     )
    print(      re.sub('[abc]','o','caps')     )


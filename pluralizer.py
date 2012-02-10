#!/usr/bin/env python3.2
# encoding: utf-8
"""
implementing a pluralizer
plural 5

same a version 2 but reads from a file
"""

import re


# The presence of the yield keyword in make_counter means that this is not a
# normal function. It is a special kind of function which generates values one at
# a time. You can think of it as a resumable function. Calling it will return a
# generator that can be used to generate successive values of x.

# this function returns a generator object
def rules(rules_filename):
    with open(rules_filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            # All variables, local state, &c. are saved on yield and restored on next()
            # yield:
            #   saves the state of everything and returns the current value of build_and...
            yield build_match_and_apply_functions( pattern, search, replace )

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return (matches_rule, apply_rule)

def plural(noun, rules_filename='plural4-rules.txt'):
    # Since rules() is a generator, you can use it directly in a for loop.
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun) )

if __name__ == '__main__':
    # print( rules )
    print( plural('car') )


###################################
#  benefit from using generators  #
###################################

# What have you gained over stage 4? Startup time. In stage 4, when you imported
# the plural4 module, it read the entire patterns file and built a list of all
# the possible rules, before you could even think about calling the plural()
# function. With generators, you can do everything lazily: you read the first
# rule and create functions and try them, and if that works you don’t ever read
# the rest of the file or create any other functions.

# What have you lost? Performance! Every time you call the plural() function, the
# rules() generator starts over from the beginning — which means re-opening the
# patterns file and reading from the beginning, one line at a time.

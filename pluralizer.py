#!/usr/bin/env python3.2
# encoding: utf-8
"""
implementing a pluralizer

previous implementation used generators
this version uses an iterator
"""

import re

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return (matches_rule, apply_rule)

class LazyRules:
    """Docstring for LazyRules """

    rules_filename = "plural4-rules.txt"    #class variable, shared across all 
                                            # instances of the LazyRules class

    def __init__(self):
        self.pattern_file = open(self.rules_filename, encoding='utf-8') #on instantiation read the file
        self.cache = []

    def __iter__(self):
        self.cache_index = 0
        return self
    
    def __next__(self):
        self.cache_index += 1
        if len( self.cache ) >= self.cache_index:
            return self.cache[self.cache_index - 1]

        if self.pattern_file.closed:
            raise StopIteration

        # The file pointer will stay wherever we stopped reading, waiting for the next readline() command.
        line = self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration

        pattern, search, replace = line.split(None, 3)
        funcs = build_match_and_apply_functions( pattern, search, replace )

        self.cache.append(funcs)
        return funcs

# When the module is imported, it creates a single instance of the LazyRules
# class, called rules, which opens the pattern file but does not read from it.
rules = LazyRules()


def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)

if __name__ == '__main__':
    # print( rules )
    print( plural('car') )



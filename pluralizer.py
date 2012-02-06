#!/usr/bin/env python3.2
# encoding: utf-8
"""
implementing a pluralizer

using closures!
"""

import re

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return (matches_rule, apply_rule)


patterns = \
  (
    ('[sxz]$',           '$',  'es'),
    ('[^aeioudgkprt]h$', '$',  'es'),
    ('(qu|[^aeiou])y$',  'y$', 'ies'),
    ('$',                '$',  's')
  )


rules = [ build_match_and_apply_functions(pattern, search, replace) 
            for (pattern, search, replace) in patterns ]

# here is the result
# rules = (
#         (match_sxz, apply_sxz),
#         (match_h, apply_h), 
#         (match_y, apply_y),
#         (match_default, apply_default),
#         )

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)


if __name__ == '__main__':
    # print( rules )
    print( plural('car') )


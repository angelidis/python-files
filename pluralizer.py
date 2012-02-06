#!/usr/bin/env python3.2
# encoding: utf-8
"""
implementing a pluralizer
"""

import re

#############
#  classic  #
#############

def plural_classic(noun):

    if re.search('[sxz]$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeioudgkprt]h$]', noun):      #carret means negation
        return re.sub('$', 'es', noun)
    elif re.search('[^aeiou]y$]', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'

################
#  variation1  #
################

def match_sxz(noun):
    re.search('[sxz]$', noun)

def apply_sxz(noun):
    return re.sub('$', 'es', noun)

def match_h(noun):
    re.search('[^aeioudgkprt]h$]', noun)

def apply_h(noun):
    return re.sub('$', 'es', noun)


def match_y(noun):
    re.search('[^aeiou]y$]', noun)

def apply_y(noun):
    return re.sub('y$', 'ies', noun)

def match_default(noun):
    return True

def apply_default(noun):
    return noun + 's'

rules = (
        (match_sxz, apply_sxz),
        (match_h, apply_h), 
        (match_y, apply_y),
        (match_default, apply_default),
        )

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)

if __name__ == '__main__':
    print( plural('car') )

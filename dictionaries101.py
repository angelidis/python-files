#!/usr/bin/env python3.2
"""
having fun with python3 dictionaries

A dictionary is an unordered set of key-value pairs. When you add a key to a
dictionary, you must also add a value for that key. (You can always change the
value later.) Python dictionaries are optimized for retrieving the value when
you know the key, but not the other way around.


check:
http://diveintopython3.ep.io/native-datatypes.html
"""


if __name__ == '__main__':
    a_dict = { 'server': 'db.diveintopython3.org', 'database':'mysql',
            'name':'nikos',
            'key':'value'
            }
    print( a_dict )
    print( a_dict['server'] )
    a_dict['name'] = 'aggelidis'
    a_dict['random'] = 'hello!'
    print( a_dict )

    SUFFIXES = {
            1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
            }
    len(SUFFIXES) # ==2 returns the number of keys
    1000 in SUFFIXES # True

    SUFFIXES[1024]  #its value is a list of 8 items

    SUFFIXES[1000][3] # == 'TB'

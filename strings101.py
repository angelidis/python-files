#!/usr/bin/env python3.2
# encoding: utf-8
"""
Bytes are bytes; characters are an abstraction. 

An immutable sequence of Unicode characters is called a string. 
An immutable sequence of numbers-between-0-and-255 is called a bytes object.

"""

if __name__ == '__main__':
    query = 'user=pilgrim&database=master&password=PapayaWhip'

    a_list = query.split('&')
    # ['user=pilgrim', 'database=master', 'password=PapayaWhip']
    
    a_list_of_lists = [ v.split('=', 1) for v in a_list if '=' in v ]
    # [['user', 'pilgrim'], ['database', 'master'], ['password', 'PapayaWhip']]
    a_dict = dict(a_list_of_lists)
    # a_dict ==== {'password': 'PapayaWhip', 'user': 'pilgrim', 'database': 'master'}

    print(a_dict)
    
    ######################
    #  slicing a string  #
    ######################
    a_string = 'My alphabet starts where your alphabet ends.'
    a_string[3:11]
    # 'alphabet'


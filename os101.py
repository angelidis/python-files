#!/usr/bin/env python3.2
# encoding: utf-8


import os
import glob

if __name__ == '__main__':

    # join paths
    print(os.path.join(os.path.expanduser('~'), 'projects', 'python', 'humansize.py'))


    # split paths
    pathname = os.path.join(os.path.expanduser('~'), 'projects', 'python', 'humansize.py')
    (dirname, filename) = os.path.split(pathname)

    print(dirname)
    print(filename)

    
    (shortname, extension) = os.path.splitext(filename)
    print(shortname)
    print(extension)

    pathname = os.path.join(os.path.expanduser('~'), 'projects')
    os.chdir(pathname) 
    os.chdir('python/') # the os.chdir function can also work with 
                        # relative pathnames
    print( glob.glob('*.py') )
    print('realpath')
    print(os.path.realpath('files101.py'))


    metadata = os.stat('os101.py')
    print( metadata.st_mtime )
    import time
    print( time.localtime(metadata.st_mtime) )
    #answer:
    # time.struct_time(tm_year=2009, tm_mon=7, tm_mday=13, tm_hour=17,
    # tm_min=25, tm_sec=44, tm_wday=0, tm_yday=194, tm_isdst=1)
    print( metadata.st_size )

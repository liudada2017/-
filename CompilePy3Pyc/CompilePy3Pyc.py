#!/usr/bin/env python
# coding: utf-8

"""
Module: Compile python script module
Author: sinshen
Date: 2018.6.14
"""

import os
import sys
import py_compile

excludedirs = ['modules']

def WalkerCompile(srcdir, dstdir):
    """
    Recursive compile python script
    """
    if not os.path.exists(dstdir):
        os.mkdir(dstdir)

    for filename in os.listdir(srcdir):
        if filename.startswith('.'):
            continue

        filePath = os.path.join(srcdir, filename)

        if filename.endswith('.py') and os.path.isfile(filePath):
            dstFilePath = os.path.join(dstdir, filename + 'c')
            print(filePath + ' --> ' + dstFilePath)
            ret = py_compile.compile(filePath, cfile=dstFilePath)
            if ret is None and sys.version.startswith('3'):
                print("--------------error happend, please check python src file--------------")
                sys.exit(1)

        if os.path.isdir(filePath):
            for curdir in excludedirs:
                if filename == curdir:
                    continue

            dstPath = os.path.join(dstdir, filename)
            WalkerCompile(filePath, dstPath)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        WalkerCompile(sys.argv[1], sys.argv[2])
    else:
        print('please set py srcdir and pyc dstdir')

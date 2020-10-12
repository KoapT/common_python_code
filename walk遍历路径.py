#! /usr/bin/env python
# -*- coding: utf-8 -*-

def walk(dir_path):
    import os
    for (root, dirs, files) in os.walk(dir_path):
        for file in files:
            print(os.path.join(root, file))



if __name__ == '__main__':
    dir_path='./'
    walk(dir_path)


#! /usr/bin/env python
# -*- coding: utf-8 -*-


class AttrDict(dict):
    '''
    更简化的定义字典方法：例：
    d = AttrDict()
    d.xxx = 111
    '''
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.c = 3

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        elif name in self:
            return self[name]
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if name in self.__dict__:
            self.__dict__[name] = value
        else:
            self[name] = value


if __name__ == '__main__':
    dd = AttrDict()
    dd.a=1
    dd['b']=2
    print(dd)
    print(dd.a)

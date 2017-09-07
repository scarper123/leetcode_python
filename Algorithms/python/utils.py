#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-07 17:11
# @Author  : Shanming Liu

import time


def time_record(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()

        print("Use time -> %s" % (end - start,))
        return res

    return wrapper

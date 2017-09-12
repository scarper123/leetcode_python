#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-12 15:21
# @Author  : Shanming Liu

from promise import Promise


def test_promise():
    promise = Promise(executor)


def executor(success, error):
    error("Error")


def resolve(data):
    print(data)


def reject(reason):
    print(reason)


if __name__ == '__main__':
    test_promise()

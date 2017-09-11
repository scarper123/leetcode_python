#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-11 14:29
# @Author  : Shanming Liu

import random
import re
import string

EMPTY_PATTERN = re.compile(r'[\s]+')
COMMON_SOLUTION_TYPE = [
    {
        "pattern": re.compile(r'python', re.I),
        "suffix": "py"
    },
    {
        "pattern": re.compile(r'java', re.I),
        "suffix": "java"
    },
    {
        "pattern": re.compile(r'rb', re.I),
        "suffix": "rb"
    },
    {
        "pattern": re.compile(r'javascript', re.I),
        "suffix": "js"
    },
]


def generate_valid_name(*args, **kwargs):
    position_name = "_".join(args)
    kw_name = "_".join("%s_%s" % (k, str(v)) for k, v in kwargs.iteritems())

    name = ""
    if position_name:
        name = position_name

    if kw_name:
        name = "%s_%s" % (name, kw_name)

    if not name:
        name = "_".join(random.choice(string.ascii_letters) for i in range(8))

    return EMPTY_PATTERN.sub("_", name.lower())


def generate_file_suffix(title):
    for item in COMMON_SOLUTION_TYPE:
        if item['pattern'].search(title):
            return item['suffix']

    return "txt"


def generate_file_name(title):
    suffix = generate_file_suffix(title)
    valid_name = generate_valid_name(title)

    return "%s.%s" % (valid_name, suffix)

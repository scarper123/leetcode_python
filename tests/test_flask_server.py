#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-12 16:47
# @Author  : Shanming Liu


import random

import flask

app = flask.Flask(__name__)


@app.route('/')
def home():
    random_value = random.randrange(1, 100)
    return "Random value -> %s\n" % random_value


if __name__ == '__main__':
    app.run(port=8192)

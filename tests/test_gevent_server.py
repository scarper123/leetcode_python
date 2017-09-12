#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-12 16:08
# @Author  : Shanming Liu

import random

import gevent
from gevent import wsgi, pool


# the application to handle the response
def app(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    random_value = random.randrange(1, 100)
    return "Random value -> %s\n" % random_value


def example1():
    print "The sweet thing is running on http://localhost:8912/"
    pool = gevent.pool.Pool()  # A pool of greenlets.Each greenlets runs the above defined function app for a client request
    server = wsgi.WSGIServer(("localhost", 8912), app,
                             spawn=pool)  # the server is created and runs multiple greenlets concurrently
    server.serve_forever()  # the server is made to run in loop


def example2():
    from gevent import monkey

    monkey.patch_all()

    import argparse

    parser = argparse.ArgumentParser()
    # parser.add_argument("app", help="dotted name of WSGI app callable [module:callable]")
    parser.add_argument("-b", "--bind",
                        help="The socket to bind",
                        default="localhost:8080")

    args = parser.parse_args()

    # module_name, app_name = args.app.split(':')
    # module = importlib.import_module(module_name)
    # app = getattr(module, app_name)
    bind = args.bind

    server = wsgi.WSGIServer(bind, app)
    server.serve_forever()


if __name__ == "__main__":
    example2()

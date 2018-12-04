#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/12/6
@author: shimakaze-git
'''

import responder

api = responder.API()


def hello_to(req, resp, *, who):
    resp.media = {"hello": who}

api.add_route("/hello/{who}", hello_to)

if __name__ == "__main__":
    port = 5000
    api.run(port=port)


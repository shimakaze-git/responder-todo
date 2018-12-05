#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/12/6
@author: shimakaze-git
'''

import responder
from responder import API

from todo import add_todo
from todo import delete_todo
from todo import update_todo
from todo import get_todo
from todo import get_todo_list

api = responder.API()

class Test:
    def on_get(self, req, resp):
        # print(dir(req))
        # print(req.method)
        resp.text = "test2"

# def hello_to(req, resp, *, who):
#     resp.media = {"hello": who}

# def get_todo(req, resp, *, id):
#     resp.text = ""

# def get_todo_list(req, resp):
#     resp.text = ""

# def add_todo(req, resp):
#     print(req)
#     resp.text = "test"
#     # resp.media = {"hello": who}

# def update_todo(req, resp, *, id):
#     resp.text = ""

# def delete_todo(req, resp, *, id):
#     resp.text = ""

class UpdateGetDeleteTodo:
    def on_get(self, req, resp, *, id):
        todo = get_todo(id)
        resp.media = {
            "status": True,
            "todo": todo
        }
    def on_put(self, req, resp, *, id):
        pass
    
    def on_delete(self, req, resp, *, id):
        pass

#api/todo
class AddGetTodo:

    def on_get(self, req, resp):
        todos = get_todo_list()
        resp.media = {
            "status": True,
            "todos": todos
        }

    def on_post(self, req, resp):
        # print(dir(req))
        print(req.params)
        data = req.media
        print(data)
        # print(data['username'])
        # print(dir(data))
        resp.text = ""

api.add_route("/hello", Test)
# api.add_route("/hello/{who}", hello_to)
# api.add_route("/hello/{who}", hello_to)
api.add_route("/api/todo", AddGetTodo)
api.add_route("/api/todo/{id}", UpdateGetDeleteTodo)

if __name__ == "__main__":
    port = 5000
    print('test')
    api.run(port=port)

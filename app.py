#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/12/6
@author: shimakaze-git
'''

import responder
from responder import API
import time

from todo import add_todo
from todo import delete_todo
from todo import update_todo
from todo import get_todo
from todo import get_todo_list

api = responder.API(
    cors=True,
    allowed_hosts=["*"],
)


class UpdateGetDeleteTodo:

    def on_get(self, req, resp, *, id):
        todo = get_todo(id)
        resp.media = {
            "status": True,
            "todo": todo
        }

    async def on_put(self, req, resp, *, id):
        @api.background.task
        def process_update_todo(name, text):
            time.sleep(3)
            update_todo(id, name, text)

        data = await req.media()
        name = data['name']
        text = data['text']

        process_update_todo(name, text)
        resp.media = {
            'status': True
        }

    async def on_delete(self, req, resp, *, id):
        @api.background.task
        def process_delete_todo():
            time.sleep(3)
            delete_todo(id)

        process_delete_todo()
        resp.media = {
            'status': True
        }


class AddGetTodo:

    def on_get(self, req, resp):
        todos = get_todo_list()
        resp.media = {
            "status": True,
            "todos": todos
        }

    async def on_post(self, req, resp):
        @api.background.task
        def process_add_todo(name, text):
            time.sleep(3)
            add_todo(name, text)

        data = await req.media()
        name = data['name']
        text = data['text']

        process_add_todo(name, text)
        resp.media = {
            'status': True
        }


api.add_route("/api/todo", AddGetTodo)
api.add_route("/api/todo/{id}", UpdateGetDeleteTodo)

if __name__ == "__main__":
    port = 5000
    print('test')
    api.run(port=port)

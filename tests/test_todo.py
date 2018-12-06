#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/12/6
@author: shimakaze-git
'''
import sys
import os
import unittest

path = os.path.join(os.path.dirname(__file__), '../')
sys.path.append(path)

from todo import add_todo
from todo import delete_todo
from todo import update_todo
from todo import get_todo
from todo import get_todo_list

from rdb import Base
from rdb import engine
from rdb import session

SQLITE3_NAME = "./db.sqlite3"


class TestTodo(unittest.TestCase):

    def setUp(self):
        if not os.path.isfile(path + SQLITE3_NAME):
            Base.metadata.create_all(engine)

    def tearDown(self):
        pass

    def test_add_todo(self):
        name = "test_name"
        text = "test_text"
        add_todo(name, text)

        id = 1
        task = get_todo(id)
        self.assertEqual(task['name'], name)
        self.assertEqual(task['text'], text)

    def test_get_todo(self):
        name = "test_name"
        text = "test_text"
        add_todo(name, text)

        id = 1
        task = get_todo(id)
        self.assertIsNotNone(task)

    def test_get_list_todo(self):
        name = "test_name"
        text = "test_text"
        add_todo(name, text)

        name = "test_name"
        text = "test_text"
        add_todo(name, text)

        tasks = get_todo_list()
        self.assertIsNotNone(tasks)

    def test_update_todo(self):

        id = 1
        name = "test_name2"
        text = "test_text2"
        update_todo(id, name, text)

        task = get_todo(id)
        self.assertEqual(task['name'], name)
        self.assertEqual(task['text'], text)

    def test_delete_todo(self):
        id = 1
        delete_todo(id)

        task = get_todo(id)
        self.assertEqual(task, {})


if __name__ == "__main__":
    # if not os.path.isfile(path + SQLITE3_NAME):
    #     Base.metadata.create_all(engine)

    if os.path.isfile(path + SQLITE3_NAME):
        os.remove(path + SQLITE3_NAME)
    unittest.main()

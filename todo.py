#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/12/6
@author: shimakaze-git
'''
from rdb import session
from models import Tasks

from sqlalchemy.exc import SQLAlchemyError


def add_todo(name, text, img_path):
    """ todo listの追加 """
    try:
        task = Tasks(
            name=name,
            text=text,
            img_path=img_path
        )
        session.add(task)
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    except Exception as e:
        session.rollback()
    finally:
        session.close()

def update_todo(id, name, text, img_path):
    """ todo listの更新 """
    try:
        """ SELECT 時に排他ロックを取得 """
        query = session.query(
            Tasks
        ).with_lockmode('update')

        task = query.filter(
            Tasks.id == id
        ).first()

        # time.sleep(1)

        """ name, text, img_pathの更新 """
        task.name = name
        task.text = text
        task.img_path = img_path
        
        session.commit()

    except SQLAlchemyError as e:
        session.rollback()
    except Exception as e:
        session.rollback()
    finally:
        session.close()

def delete_todo(id):
    """ todo listの削除 """
    try:
        task = session.query(
            Tasks
        ).filter(
            Tasks.id == id
        ).first()

        session.delete(task)
        session.commit()
    except SQLAlchemyError:
        session.rollback()
    except Exception as e:
        session.rollback()
    finally:
        session.close()

def get_todo_list():
    """ todo listを全て取得 """
    task_list = []
    try:
        tasks = session.query(
            Tasks
        ).all()

        for task in tasks:
            created_at = task.created_at
            updated_at = task.updated_at

            task_list.append({
                "id": task.id,
                "img_path": task.img_path,
                "name": task.name,
                "text": task.text,
                "created_at": created_at.strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": updated_at.strftime('%Y-%m-%d %H:%M:%S')
            })
    except Exception as e:
        print(e)
    finally:
        session.close()
        return task_list

def get_todo(id):
    """ todo listを取得 """
    task_dict = {}
    try:
        task = session.query(
            Tasks
        ).filter(
            Tasks.id == id
        ).first()

        if task:
            created_at = task.created_at
            updated_at = task.updated_at
            task_dict = {
                "id": task.id,
                "img_path": task.img_path,
                "name": task.name,
                "text": task.text,
                "created_at": created_at.strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": updated_at.strftime('%Y-%m-%d %H:%M:%S')
            }

    except Exception as e:
        print(e)
    finally:
        session.close()
        return task_dict

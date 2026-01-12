from domain.models.itodo_repository import ITodoRepository
from domain.models.todo import Todo
from typing import List, Optional
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config
from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases.base import Base
from sqlalchemy.orm import Session
from infrastructure.models.todo_model import TodoModel
from infrastructure.databases.supa import get_supabase_client
load_dotenv()

class TodoRepository(ITodoRepository):
    def __init__(self, supabase = get_supabase_client()):
        self._todos = []
        self._id_counter = 1
        self.supabase = supabase

    def add(self, todo: Todo) -> TodoModel:
        try:
            #Manual mapping from Todo to TodoModel
            todo = TodoModel(
                title=todo.title,
                description=todo.description,
                status=todo.status,
                created_at=todo.created_at,
                updated_at=todo.updated_at
            )
            self.supabase.table("todos").insert(todo.dict()).execute() #chua hoan tat
            return todo
        except Exception as e:
            self.supabase.rollback()
            raise ValueError('Todo not found')
        finally:
            self.session.close()
    
    # def add(self, todo: Todo) -> Todo:
    #     todo.id = self._id_counter
    #     self._id_counter += 1
    #     self._todos.append(todo)
    #     return todo

    def get_by_id(self, todo_id: int) -> Optional[TodoModel]:
        return self.supabase.table("todos").select("*").eq("id", todo_id).execute().data[0] #chua hoan tat


    # def list(self) -> List[Todo]:
    #     self._todos
    #     return self._todos
    def list(self) -> List[TodoModel]:
        self._todos = self.supabase.table("todos").select("*").execute().data #chua hoan tat
        # select * from todos
        return self._todos


    def update(self, todo: TodoModel) -> TodoModel:
        try:
             #Manual mapping from Todo to TodoModel
            todo = TodoModel(
                id = todo.id,
                title=todo.title,
                description=todo.description,
                status=todo.status,
                created_at=todo.created_at,
                updated_at=todo.updated_at
            )
            self.supabase.table("todos").update(todo.dict()).eq("id", todo.id).execute()
            self.supabase.commit() #chua hoan tat
            return todo
        except Exception as e:
            self.supabase.rollback()
            raise ValueError('Todo not found')
        finally:
            self.supabase.close()

    def delete(self, todo_id: int) -> None:
        # self._todos = [t for t in self._todos if t.id != todo_id] 
        try:
            todo = self.supabase.table("todos").select("*").eq("id", todo_id).execute().data[0]
            if todo:
                self.supabase.table("todos").delete().eq("id", todo_id).execute()
                self.supabase.commit() #chua hoan tat
            else:
                raise ValueError('Todo not found')
        except Exception as e:
            self.supabase.rollback()
            raise ValueError('Todo not found')
        finally:
            self.supabase.close()


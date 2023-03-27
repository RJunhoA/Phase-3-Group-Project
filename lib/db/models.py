from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///mydb.db')
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    # todo_id = Column(Integer(), ForeignKey('todo.id'))

    # def __init__(self, first_name, last_name):
    #     self.first_name = first_name
    #     self.last_name = last_name

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class Tasks(Base):

    __tablename__ = "tasks"
    # __tableargs__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer(), primary_key=True)
    task = Column(String())
    
    def __repr__(self):
        return f"{self.id} {self.task}"

    # todo_id = Column(Integer(), ForeignKey('todo.id')) #try todo.user_id

class UserTask(Base): #Join Table!!!!!!
    __tablename__ = "list"
    __tableargs__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    task_id = Column(String(), ForeignKey('tasks.id'))
    user_id = Column(Integer(), ForeignKey('users.id'))
    tasks = relationship('Tasks', backref=backref('User'))
    user = relationship('User', backref=backref('Tasks'))

    def __repr__(self):
        return f"{self.id} {self.tasks} {self.user}"


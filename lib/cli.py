from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

Base = declarative_base()

#each time a User or Tasks instance is created it will generate a foreign key to the todo (join table) table relating it to a matching instance of either user or Tasks
#every time a todo instance is created it will generate a relationship between a user and a Tasks
#hopefully having a foriegn key in both User and Tasks pointing to todo will create the many to many relationship

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
    
    # todo_id = Column(Integer(), ForeignKey('todo.id')) #try todo.user_id

class UserTask(Base): #Join Table!!!!!!
    __tablename__ = "list"
    __tableargs__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    task_id = Column(String(), ForeignKey('tasks.id'))
    user_id = Column(Integer(), ForeignKey('users.id'))
    Tasks = relationship('Tasks', backref=backref('User'))
    user = relationship('User', backref=backref('Tasks'))




engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

#________________CODE______________________

user = User("Billy", "Bob")
session.add(user)

tasks = Tasks("Take out trash")
session.add(tasks)

join = UserTask()

session.commit()



    


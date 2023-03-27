from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column("id", Integer, primary_key=True)
    first_name = Column("firstname", String)
    last_name = Column("lastname", String)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

user = User("Billy", "Bob")
session.add(user)
session.commit()

class ToDo(Base):
    __tablename__ = "list"

    id = Column("id", Integer, primary_key=True)
    task_id = Column("task_id", String)
    user_id = Column(Integer, ForeignKey(User.id))

    


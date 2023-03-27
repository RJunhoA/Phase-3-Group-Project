from sqlalchemy.orm import sessionmaker
from models import *

Session = sessionmaker(bind=engine)
session = Session()

#________________CODE______________________

user = User("Billy", "Bob")
session.add(user)

tasks = Tasks("Take out trash")
session.add(tasks)

join = UserTask()

session.commit()

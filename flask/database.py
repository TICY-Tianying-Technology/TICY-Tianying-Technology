from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:77777777.*@localhost/students')
Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class StudentInfo(Base):
    __tablename__ = "student_info"
    id = Column(Integer, primary_key=True)
    name = Column()
    age = Column()
    lesson = Column()
    grade = Column()
    gender = Column()



class Tr(Base):
    __tablename__ = "tr3"
    id = Column(Integer, primary_key=True)
    username = Column()
    password = Column()


from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Sequence

from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///my.db', echo=False)

Base = declarative_base()


class User(Base):
    __tablename__ = 'Texts'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    text = Column(String())

    def __repr__(self):
        return "<User(text='%s')>" % self.text


Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

Base.metadata.create_all(engine)


def add_text(text):
    text_object = User(text=text)
    session.add(text_object)
    session.commit()


def clear():
    for instance in session.query(User):
        session.delete(instance)
    session.commit()


def add_text_form():
    text = input("Input your text to add it to database: ")
    add_text(text)


def get_text_by_id(id_):
    return session.query(User).get(id_).text


def get_id():
    return session.query(User).count()

# clear()
# print(get_id())
# add_text_form()
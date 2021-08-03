from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Sequence

from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///my.db', echo=False)

Base = declarative_base()


class Texts(Base):
    __tablename__ = 'Texts'
    id = Column(Integer, Sequence('text_id_seq'), primary_key=True)
    text = Column(String())

    def __repr__(self):
        return "<Texts(text='%s')>" % self.text


class Quotes(Base):
    __tablename__ = 'Quotes'
    id = Column(Integer, Sequence('quotes_id_seq'), primary_key=True)
    text = Column(String())

    def __repr__(self):
        return "<Quotes(text='%s')>" % self.text


Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

Base.metadata.create_all(engine)


def add_text(cls, text):
    text_object = cls(text=text)
    session.add(text_object)
    session.commit()


def clear(cls):
    for instance in session.query(cls):
        session.delete(instance)
    session.commit()


def add_text_form(cls):
    text = input("Input your text to add it to database: ")
    add_text(text, cls)


def get_text_by_id(id_, cls):
    return session.query(cls).get(id_).text


def get_id(cls):
    return session.query(cls).count()

# clear()
# print(get_id())
# add_text_form()

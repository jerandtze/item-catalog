#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Genre(Base):

    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""

        return {'title': self.title, 'id': self.id}


class BookItem(Base):

    __tablename__ = 'book_item'

    title = Column(String(80))
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    coverUrl = Column(String(450))
    author = Column(String(250))
    edition = Column(String(20))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    genre = relationship("BookItem", cascade="all, delete-orphan")
    genre = relationship(Genre)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""

        return {
            'title': self.title,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'coverUrl': self.coverUrl,
            'author': self.author,
            'edition': self.edition,
            }


engine = create_engine('sqlite:///bookstoremenuwithusers.db')

Base.metadata.create_all(engine)

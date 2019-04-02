import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()


# Two classes for Genre and Album, both serializable for JSON
class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    creator = Column(String(150), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class Album(Base):
    __tablename__ = 'album'

    artist = Column(String(80), nullable=False)
    title = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    creator = Column(String(150), nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    genre = relationship(
        Genre, backref=backref(
            'children', cascade='all,delete'))

    @property
    def serialize(self):
        return {
            'artist': self.artist,
            'title': self.title,
            'id': self.id,
            'description': self.description,
            'price': self.price,
        }


engine = create_engine('sqlite:///musiccatalog.db')
Base.metadata.create_all(engine)

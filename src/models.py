import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(), unique=False, nullable=False) 
    gender = Column(String(), unique=False, nullable=False)
    hair_color = Column(String(200), unique=False, nullable=False)
    eye_color = Column(String(), unique=False, nullable=False)

    def to_dict(self):
        return {
        '<Character %s>' % self.characters
        }


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hairColor": self.hair_color,
            "eyeColor": self.eye_color,
            
        }

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(), unique=False, nullable=False)
    model = Column(String(), unique=False, nullable=False)
    vehicle_class = Column(String(), unique=False, nullable=False)

    def to_dict(self):
        return {
        '<vehicle %s>' % self.vehicles
        }


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "vehicleClass": self.vehicle_class,
            
        }


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(), unique=False, nullable=False)
    population = Column(Integer(), unique=True, nullable=False)
    terrain = Column(String(), unique=False, nullable=False)

    def to_dict(self):
        return {
        '<planet %s>' % self.planets
        }


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            
        }

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(), unique=False, nullable=False)
    first_name = Column(String(), unique= True, nullable=False)
    last_name = Column(String(), unique=False, nullable=False)
    email = Column(String(), unique=False, nullable=False)

    def to_dict(self):
        return {
        '<user %s>' % self.users
        }


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            
        }

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer(), unique=True, nullable=False)
    vehicle_id = Column(String(), unique= True, nullable=False)
    planet_id = Column(String(), unique=True, nullable=False)
    user_id = Column(String(), unique=True, nullable=False)

    def to_dict(self):
        return {
        '<favorite %s>' % self.favorites
        }


    def serialize(self):
        return {
            "id": self.id,
            "characterId": self.character_id,
            "vehicleId": self.vehicle_id,
            "planetId": self.planet_id,
            "userid": self.user_id,
            
        }
        

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
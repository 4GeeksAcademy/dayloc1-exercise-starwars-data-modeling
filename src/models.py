import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    Id= Column(Integer, primary_key= True)
    Username= Column(String(16), nullable= False, unique = True)
    Email = Column(String(40), nullable= False, unique = True)

    def serialize(self):
        return {
            Id: self.Id,
            Username: self.Username,
            Email: self.Email
        }

    

class Planets(Base):
    __tablename__ = 'planets'

    Id = Column(Integer, primary_key = True)
    Name= Column(String(60), nullable = False, unique = True)
   

    def serialize(self):
        return {
            Id: self.Id,
            Name: self.Name,
            
        }
class People(Base):
    __tablename__ = 'people'

    Id = Column(Integer, primary_key= True)
    Name= Column(String(60), nullable= False, unique= True)
    Planet= Column(String(60), ForeignKey(Planets.Name))

    def serialize(self):
        return {
            Id: self.Id,
            Name: self.Name,
            Planet: self.Planet
        }
    

class Favorites(Base):
    __tablename__ = 'favorites'

    Id = Column(Integer, primary_key = True)
    User_Id = Column(Integer, ForeignKey(User.Id))
    People_Id = Column(Integer, ForeignKey(People.Id))
    Planets_Id = Column(Integer, ForeignKey(Planets.Id))



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

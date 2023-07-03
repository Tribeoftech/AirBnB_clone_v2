#!/usr/bin/python3
'''This modules defines DBStorage class'''

from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    '''Defining class DBStorage'''

    __engine = None
    __session = None

    def __init__(self):
        '''Init for class DBStorage'''
        USER = getenv('HBNB_MYSQL_USER')
        PWD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')
        ENV = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(USER, PWD, HOST, DB),
                                      pool_pre_ping=True)

        if ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method to retrieve all objects depending on the class name"""
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.base_model import BaseModel
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }

        if cls:
            newDict = {}
            allClassObjs = self.__session.query(classes[cls]).all()
            for obj in allClassObjs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                newDict[key] = obj
            return newDict
        else:
            allDicts = {}
            dictList = []
            for cls_name, cls in classes.items():
                dictList.append(self.all(cls_name))
            for dicts in dictList:
                allDicts.update(dicts)
            return allDicts

    def new(self, obj):
        '''Adds a new object to the database session'''
        self.__session.add(obj)

    def save(self):
        '''Commits the current state of the database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''Deletes an object from the database session'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.base_model import BaseModel
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity
        '''Reloads the database'''
        Base.metadata.create_all(self.__engine)

        sessionFactory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sessionFactory)
        self.__session = Session()

    def close(self):
        '''Closes the session'''
        self.__session.close()

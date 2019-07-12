from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///categoryproject.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

category1 = Category(id=1, name='Fruit')
session.add(category1)
session.commit()


category2 = Category(id=2, name='Vegetables')
session.add(category2)
session.commit()


category3 = Category(id=3, name='Meat')
session.add(category3)
session.commit()


category4 = Category(id=4, name='Drinks')
session.add(category4)
session.commit()


category5 = Category(id=5, name='Dairy')
session.add(category5)
session.commit()


category6 = Category(id=6, name='Spices')
session.add(category6)
session.commit()


category7 = Category(id=7, name='Other')
session.add(category7)
session.commit()

print("Success")
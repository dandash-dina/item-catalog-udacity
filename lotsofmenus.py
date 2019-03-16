from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Catalog, Base, MenuItem, User

engine = create_engine('sqlite:///catalogmenuwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Dina ", email="dinadaa@yahoo.com",
             picture='https://www.facebook.com/photo.php?fbid=10153242747161326&set=a.423189906325&type=3&theater')


session.add(User1)
session.commit()




# Menu for Alatlas
catalog1 = Catalog(user=User1, name="Alatlas")

session.add(catalog1)
session.commit()

menuItem2 = MenuItem(user=User1, name="2017 Volvo XC60 Automatic", color="Bright Silver Metallic",
                     price="$27,350", brand="Volvo", catalog=catalog1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(user=User1, name="2016 Volvo XC60 Automatic", color="Ice White",
                     price="$15,950", brand="Volvo", catalog=catalog1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user=User1, name="2017 Volvo S90", color="Mussel Blue Metallic",
                     price="$36,500", brand="Volvo", catalog=catalog1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user=User1, name="2016 Volvo XC60 Automatic", color="Ice White",
                     price="$15,950", brand="Volvo", catalog=catalog1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user=User1, name="2017 BMW X5 Automatic", color="Mineral White Metallic",
                     price="$24,990", brand="BMW", catalog=catalog1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="2016 BMW X3 Automatic", color="Silver Metallic",
                     price="$30,950", brand="BMW", catalog=catalog1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="2018 Audi A4 Automated_manual", color="Gray Metallic",
                     price="$32,990", brand="Audi", catalog=catalog1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="2018 Audi A5 Automated_manual",
                     color="Black Metallic", price="$38,490", brand="Audi", catalog=catalog1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="2017 Ford Mustang Automatic", color="Blue Metallic",
                     price="$16,900", brand="Ford", catalog=catalog1)

session.add(menuItem8)
session.commit()


# Menu for Alsafeer
catalog2 = Catalog(user_id=1, name="Alsafeer")

session.add(catalog2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="2016 Audi Q3 Automatic", color="Blue Metallic",
                     price="$23,880", brand="Audi", catalog=catalog2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="2015 Ford Edge Automatic",
                     color="Tuxedo Black Metallic", price="$19,950", brand="Ford", catalog=catalog2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="2013 Honda Civic Automatic", color="Taffeta White ",
                     price="$7,600", brand="Honda", catalog=catalog2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="2018 Toyota Camry Automatic", color="Galactic Aqua Mica",
                     price="23,750", brand="Toyota", catalog=catalog2)

session.add(menuItem4)
session.commit()


# Menu for Alsultan
catalog1 = Catalog(user_id=1, name="Alsulan")

session.add(catalog1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="2017 Volvo V90 Automatic", color="Maple Brown Metallic",
                     price="$34,990", brand="Volvo", catalog=catalog1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="2009 Toyota Camry Automatic", color="Desert Sand Mica",
                     price="$3,950", brand="Toyota", catalog=catalog1)

session.add(menuItem2)
session.commit()



# Menu for Sayartak for that
catalog1 = Catalog(user_id=1, name="Sayartak")

session.add(catalog1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="2018 Volvo S60 Automatic", color="Grey Metallic",
                     price="$26,880", brand="Volvo", catalog=catalog1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="2005 Toyota Sienna Automatic", color="Phantom Gray Pearl",
                     price="$3,900", brand="Toyota", catalog=catalog1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="2015 BMW 7 Series",
                     color="Dark Graphite Metallic", price="$38,500", brand="BMW", catalog=catalog1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="2007 BMW X5 Automatic", color="Jet Black",
                     price="$8,800", brand="BMW", catalog=catalog1)

session.add(menuItem4)
session.commit()



# Menu for Alsidebad
catalog1 = Catalog(user_id=1, name="Alsidebad")

session.add(catalog1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="2015 Audi A5", color="Red",
                     price="$29,950", brand="Audi", catalog=catalog1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="1998 BMW M3 Manual", color="Bright Red",
                     price="$9,900", brand="BMW", catalog=catalog1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="2012 BMW 5 Series", color="Jet Black",
                     price="$17,950", brand="BMW", catalog=catalog1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="2016 Audi S7",
                     color="Black", price="$51,900", brand="Audi", catalog=catalog1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="2018 Ford Escape Automatic", color="Blak",
                     price="$18,800", brand="Ford", catalog=catalog1)

session.add(menuItem5)
session.commit()


# Menu for Almadena
catalog1 = Catalog(user_id=1, name="Almadena")

session.add(catalog1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="2014 Ford F-150 Automatic", color="Black",
                     price="$16,000", brand="Ford", catalog=catalog1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="2016 Ford Focus ST Manul", color="Black",
                     price="$16,950", brand="Ford", catalog=catalog1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="2014 Toyota Tacoma Automatic", color="Silver Sky Metallic",
                     price="$10,000", brand="Toyota", catalog=catalog1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="2011 Honda Civic manual", color="Dyno Blue Pearl",
                     price="$8,950", brand="Honda", catalog=catalog1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(user_id=1, name="2015 Honda Accord Automatic", color="Red",
                     price="$14,000", brand="Honda", catalog=catalog1)

session.add(menuItem2)
session.commit()


# Menu for Secrets Agency
catalog1 = Catalog(user_id=1, name="Secrets Agency")

session.add(catalog1)
session.commit()

menuItem9 = MenuItem(user_id=1, name="2008 Honda Civic Manual",
                     color="Royal Blue Pearl", price="$4,000", brand="Honda", catalog=catalog1)

session.add(menuItem9)
session.commit()


print "added menu items!"

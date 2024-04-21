from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

DATABASE_URL = "mysql+pymysql://mar03:Jfk$oqO@localhost/IT_STEP"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    profile = relationship("Profile", back_populates="user")

class Profile(Base):
    __tablename__ = 'Profile'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    bio = Column(String(200))
    profile_picture = Column(String(255))

    user = relationship("User", back_populates="profile")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user_data = [
    User(username="Mari04", email="Mari4@gmail.com"),
    User(username="Ana707", email="anaana@gmail.com"),
    User(username="MK", email="MK9@gmail.com"),
    User(username="DavidM", email="david303@gmail.com"),
    User(username="Arthur", email="arthur@gmail.com")
]
session.add_all(user_data)

profile_data = [
    Profile(id=1, bio="Bio for Mari04", profile_picture="Mari04_profile_picture.jpg", user_id=1),
    Profile(id=2, bio="Bio for Ana707", profile_picture="Ana707_profile_picture.jpg", user_id=2),
    Profile(id=3, bio="Bio for MK", profile_picture="MK_profile_picture.jpg", user_id=3),
    Profile(id=4, bio="Bio for DavidM", profile_picture="DavidM_profile_picture.jpg", user_id=4),
    Profile(id=5, bio="Bio for Arthur", profile_picture="Arthur_profile_picture.jpg", user_id=5)
]
session.add_all(profile_data)

session.commit()

session.close()
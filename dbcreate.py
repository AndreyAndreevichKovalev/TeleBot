import os
import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, join
from dotenv import load_dotenv

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = sq.Column(sq.Integer, primary_key=True)
    c_id = sq.Column(sq.String(length=10))

class Word(Base):
    __tablename__ = "word"

    id = sq.Column(sq.Integer, primary_key=True)
    rus_word = sq.Column(sq.String(length=50))
    eng_word = sq.Column(sq.String(length=50))

class UserWord(Base):
    __tablename__ = "user_word"

    id = sq.Column(sq.Integer, primary_key=True)
    id_user = sq.Column(sq.Integer, sq.ForeignKey("user.id"), nullable=False)
    id_word = sq.Column(sq.Integer, sq.ForeignKey("word.id"), nullable=False)

    user = relationship(User, backref="user_word")
    word = relationship(Word, backref="user_word")

def create_tables(engine):
    Base.metadata.create_all(engine)

load_dotenv()
TOKEN = os.getenv("TTB")
DSN = os.getenv("DSN")
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# # Запись данных в базу
# Us1 = User(c_id="6047390436")
# Us2 = User(c_id="7198064751")

# Wd1 = Word(rus_word="Мир", eng_word="Peace")
# Wd2 = Word(rus_word="Война", eng_word="War")
# Wd3 = Word(rus_word="Красный", eng_word="Red")
# Wd4 = Word(rus_word="Черный", eng_word="Black")
# Wd5 = Word(rus_word="Кто", eng_word="Who")
# Wd6 = Word(rus_word="Что", eng_word="What")
# Wd7 = Word(rus_word="Машина", eng_word="Car")
# Wd8 = Word(rus_word="Автобус", eng_word="Bus")
# Wd9 = Word(rus_word="Самолет", eng_word="Airplane")
# Wd10 = Word(rus_word="Космос", eng_word="Space")
# Wd11 = Word(rus_word="Вода", eng_word="Water")
# Wd12 = Word(rus_word="Земля", eng_word="Earth")
# Wd13 = Word(rus_word="Страна", eng_word="Сountry")
# Wd14 = Word(rus_word="Государство", eng_word="State")
# Wd15 = Word(rus_word="Животное", eng_word="Animal")
# Wd16 = Word(rus_word="Человек", eng_word="Person")
# Wd17 = Word(rus_word="Мужчина", eng_word="Man")
# Wd18 = Word(rus_word="Женщина", eng_word="Woman")
# Wd19 = Word(rus_word="Ребенок", eng_word="Kid")
# Wd20 = Word(rus_word="Дети", eng_word="Children")
#
# Uw1 = UserWord(id_user=1, id_word=1)
# Uw2 = UserWord(id_user=1, id_word=2)
# Uw3 = UserWord(id_user=1, id_word=3)
# Uw4 = UserWord(id_user=1, id_word=4)
# Uw5 = UserWord(id_user=1, id_word=5)
# Uw6 = UserWord(id_user=1, id_word=6)
# Uw7 = UserWord(id_user=1, id_word=7)
# Uw8 = UserWord(id_user=1, id_word=8)
# Uw9 = UserWord(id_user=1, id_word=9)
# Uw10 = UserWord(id_user=1, id_word=10)
# Uw11 = UserWord(id_user=2, id_word=1)
# Uw12 = UserWord(id_user=2, id_word=2)
# Uw13 = UserWord(id_user=2, id_word=3)
# Uw14 = UserWord(id_user=2, id_word=4)
# Uw15 = UserWord(id_user=2, id_word=5)
# Uw16 = UserWord(id_user=2, id_word=6)
# Uw17 = UserWord(id_user=2, id_word=7)
# Uw18 = UserWord(id_user=2, id_word=8)
# Uw19 = UserWord(id_user=2, id_word=9)
# Uw20 = UserWord(id_user=2, id_word=10)

# session.add_all([Us1, Us2,
#                  Wd1, Wd2, Wd3, Wd4, Wd5, Wd6, Wd7, Wd8, Wd9, Wd10,
#                  Wd11, Wd12, Wd13, Wd14, Wd15, Wd16, Wd17, Wd18, Wd19, Wd20,
#                  Uw1, Uw2, Uw3, Uw4, Uw5, Uw6, Uw7, Uw8, Uw9, Uw10,
#                  Uw11, Uw12, Uw13, Uw14, Uw15, Uw16, Uw17, Uw18, Uw19, Uw20])
# session.commit()

def get_Word(txt):
    q = session.query(
        User, Word, Word,
    ).select_from(Word). \
        join(UserWord, UserWord.id_word == Word.id). \
        join(User, User.id == UserWord.id_user). \
        filter(User.c_id == txt). \
        all()

    for _user, _word, _word in q:
        print(f"{_user.c_id: <12} | {_word.rus_word: <12} | {_word.eng_word: <12}")

    return _user.c_id, _word.rus_word, _word.eng_word

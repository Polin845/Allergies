from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String

# строка подключения
sqlite_database = "sqlite:///metanit.db"
# создаем движок SqlAlchemy
engine = create_engine(sqlite_database, echo=True)


# создаем модель, объекты которой будут храниться в бд
class Base(DeclarativeBase): pass


class Person(Base):
    __tablename__ = "Allergies"

    login = Column(String, primary_key=True, index=True)
    email = Column(String)
    pasword = Column(String)
    allerg = Column(String)


# создаем таблицы
Base.metadata.create_all(bind=engine)

# создаем сессию подключения к бд
def Log(log, em, pas, al, error=0):
    with Session(autoflush=False, bind=engine) as db:
        if error:  #проверяем ошибки
            db.rollback()
        # создаем объект Person для добавления в бд
        person = Person(email=em, login=log, pasword=pas, allergens=al)
        db.add(person)  # добавляем в бд
        db.commit()  # сохраняем изменения

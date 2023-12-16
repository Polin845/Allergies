from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String

# строка подключения
sqlite_database = "sqlite:///meta.db"
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
def Per(log, pas, func, em='', al=''):
    with Session(autoflush=False, bind=engine) as db:
        if func == 'creat':
            # создаем объект Person для добавления в бд
            person = Person(email=em, login=log, pasword=pas, allerg='')
            db.add(person)  # добавляем в бд
            db.commit()  # сохраняем изменения
        elif func == 'check':
            x = db.query(Person).get(log)
            if x.pasword == pas:
                return True
            return False
        elif func == 'change':
            x = db.query(Person).filter(Person.login == log).first()
            x.allerg=al
            db.commit()
        elif func == 'ret':
            return db.query(Person).get(log).allerg
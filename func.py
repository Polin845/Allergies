from data.base import Person
from sqlalchemy.orm import Session



with Session(autoflush=False, bind=engine) as db:
    # получение всех объектов
    people = db.query(Person).all()
    for p in people:
        print(f"{p.id}.{p.name} ({p.age})")
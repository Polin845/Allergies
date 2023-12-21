from dase import SqlAlchemyBase
import sqlalchemy

class User(SqlAlchemyBase):     __tablename__ = 'users'

class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    allergens = sqlalchemy.Column(sqlalchemy.String, nullable=True)
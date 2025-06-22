# db.py
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://mouls017:KHJEg7HL22hGg8PO1mfPNyZlk0Hq4Q3A@dpg-d1ab8r2dbo4c73camu10-a.oregon-postgres.render.com/expense_app_db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    value = Column(Float, default=0)

    def __repr__(self):
        return f'Name: {self.name} | Value: {self.value}'

Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    session = SessionLocal()
    items = session.query(Expense).all()
    total = sum(item.value for item in items)
    names = [item.name for item in items]
    values = [item.value for item in items]
    print("test")


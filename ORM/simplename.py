import sqlalchemy
from sqlalchemy.orm import sessionmaker

from Creattable import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:****@localhost:5432/shop'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

# сессия
Session = sessionmaker(bind=engine)
session = Session()

session.close()

publisher1 = Publisher(name=input('Введите название издателя один: '))
publisher2 = Publisher(name=input('Введите название издателя два: '))
session.add_all([publisher1, publisher2])
session.commit()


b1 = Book(title='Как выучить Python за один день', publisher=publisher1)
b2 = Book(title='Как не перегореть уча Python за один день', publisher=publisher1)

session.add_all([b1, b2])
session.commit()

for c in session.query(Book).all():
    print(c)

for d in session.query(Book).filter(Book.title.like('%не%')).all():
    print(d)

shop1 = Shop(name='Книжный')
shop2 = Shop(name='Пэйпэ')

session.add_all([shop1, shop2])
session.commit()

for b in session.query(Shop).all():
    print(b)

stock1 = Stock(id_book=1, id_shop=1, count=5)
stock2 = Stock(id_book=2, id_shop=2, count=7)

session.add_all([stock1, stock2])
session.commit()

for e in session.query(Stock).all():
    print(e)

sale1 = Sale(price=100, date_sale='2022-11-01 23:59:59', id_stock=1)
sale2 = Sale(price=45, date_sale='2022-11-10 23:59:59', id_stock=2)

session.add_all([sale1, sale2])
session.commit()

for f in session.query(Sale).all():
    print(f)


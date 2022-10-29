import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:****@localhost:5432/shop'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

# сессия
Session = sessionmaker(bind=engine)
session = Session()

#Не могу понять как написать рабочий код для автоматической загрузки в БД?!?
# with open('fixtures/tests_data.json', 'r', encoding='utf-8') as fd:
#     data = json.load(fd)
#
# for record in data:
#     model = {
#         'publisher': Publisher,
#         'shop': Shop,
#         'book': Book,
#         'stock': Stock,
#         'sale': Sale,
#     }[record.get('model')]
#     session.add(model(id=record.get('pk'), **record.get('fields')))
# session.commit()

publisher1 = Publisher(name=input('Введите название издателя один: '))
publisher2 = Publisher(name=input('Введите название издателя два: '))
session.add_all([publisher1, publisher2])
session.commit()


b1 = Book(title='Как выучить Python за один день', publisher=publisher1)
b2 = Book(title='Как не перегореть уча Python за один день', publisher=publisher1)

session.add_all([b1, b2])
session.commit()

for k in session.query(Book).all():
    print(k)

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

#почему то не работает код ниже?!??!
# subq = session.query(Publisher).filter(Publisher.name == input('Введите название издателя: ')).subquery()
# for c in session.query(Shop).join(Stock.shop).join(Book.stock).join(Publisher.book).join(subq, Shop.id == subq.c.id).all():
#     print(c)

# Выводим в каких магазинах присутствуют книги издателя
subq = session.query(Publisher).filter(Publisher.name == input('Введите название издателя: ')).subquery()
result = session.query(Shop).join(Stock).join(Book).join(Publisher).join(subq).all()
for c in result:
    print(c)


session.close()
# import necessary packages
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Numeric, Integer, VARCHAR
from sqlalchemy.engine import result

# establish connections
engine = create_engine("database+dialect://username:password0@host:port/databasename")

# initialize the Metadata Object
meta = MetaData(bind=engine)
MetaData.reflect(meta)

# create a table schema
books = Table(
    "books",
    meta,
    Column("bookId", Integer, primary_key=True),
    Column("book_price", Numeric),
    Column("genre", VARCHAR),
    Column("book_name", VARCHAR),
)

meta.create_all(engine)

# insert records into the table
statement1 = books.insert().values(
    bookId=1, book_price=12.2, genre="fiction", book_name="Old age"
)
statement2 = books.insert().values(
    bookId=2, book_price=13.2, genre="non-fiction", book_name="Saturn rings"
)
statement3 = books.insert().values(
    bookId=3, book_price=121.6, genre="fiction", book_name="Supernova"
)
statement4 = books.insert().values(
    bookId=4, book_price=100, genre="non-fiction", book_name="History of the world"
)
statement5 = books.insert().values(
    bookId=5, book_price=1112.2, genre="fiction", book_name="Sun city"
)

# execute the insert records statement
engine.execute(statement1)
engine.execute(statement2)
engine.execute(statement3)
engine.execute(statement4)
engine.execute(statement5)

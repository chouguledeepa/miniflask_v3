"""

engine = create_engine("dialect+driver://user:password@host:port/db")


dialect :: mysql, postgres, oracle, windowsSQL, SQLLite


"""

from pymysql.err import Error
from sqlalchemy import create_engine

user = "adam"
password = "qwerty"
host = "127.0.0.1"
port = 3306
database = "starwarsDB"


def get_connection():

    try:
        engine = create_engine(
            "mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
            "".format(
                user=user, password=password,
                host=host, port=int(port), database=database
            )
        )
    except Error as ex:
        print(f"[ ERROR ] details {ex}")

    return engine


if __name__ == "__main__":
    engine = get_connection()
    table_names = engine.table_names()
    print(table_names)
    breakpoint()

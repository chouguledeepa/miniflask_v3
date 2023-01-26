"""


# TO grant permissions to user

GRANT ALL PRIVILEGES ON starwarsDB. * TO adam@localhost;


"""

import sqlalchemy
from pymysql.err import Error
from sqlalchemy import create_engine
import sqlalchemy as db  # alias for sqlalchemy is `db`


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
        meta_data_obj = db.MetaData()
    except Error as ex:
        print(f"[ ERROR ] details {ex}")

    return engine, meta_data_obj


if __name__ == "__main__":
    engine, meta_data_obj = get_connection()
    profile_ = db.Table(
        "profile",
        meta_data_obj,
        db.Column("name", db.String(250)),
        db.Column("email", db.String(250)),
        db.Column("contact", db.Integer)
    )

    from sqlalchemy.sql import select
    s = select(profile_)
    result = engine.execute(s)
    breakpoint()

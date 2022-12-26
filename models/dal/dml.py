"""
DML stands for Data Manipulation Language

This module contains generic functions to insert data into sql tables
"""
from models.dal.db_conn_helper import get_db_conn
from typing import List


def insert_resource(
    table_name: str, primary_key_: str, primary_value: int, columns_: List, values: List
):
    """
    Inserts a record in the database using primary key

    Args:
        table_name (str):
        primary_key_ (str):
        primary_value (int):
        columns_ (list):
        values (list):

    Returns:
        number of records inserted in DB table
    """

    column_names = ", ".join(columns_)
    value_fields = ", ".join(values)

    column_names.rstrip(", ")
    value_fields.rstrip(", ")

    value_fields = ""
    for value in values:
        if isinstance(value, str):
            value_fields = value_fields + '''"''' + value + '''"''' + """, """
        elif isinstance(value, int):
            value_fields = value_fields + str(value) + ""","""

    value_fields = value_fields.rstrip(""", """)

    result = None
    with get_db_conn() as conn:
        cursor = conn.cursor()

        sql_magic = f"""insert into 
        starwarsDB.{table_name} ({primary_key_}, {column_names}) 
        values ({primary_value}, {value_fields});"""

        result = cursor.execute(sql_magic)
        conn.commit()
    return result

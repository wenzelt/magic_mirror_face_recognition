from tinydb import TinyDB, Query
from os import path


def query_db_for_encodings():
    pass


def init_db(db_path: str):
    db = TinyDB(db_path)
    encoding_table = db.table("encodings")
    encoding_table.insert({"type": "apple", "count": 7})
    encoding_table.insert({"type": "peach", "count": 3})
    content = encoding_table.all()
    encoding_table.truncate()
    db.close()
    return content

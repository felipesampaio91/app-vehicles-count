import mariadb
from config.settings import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME


def get_connection():
    return mariadb.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        port=DB_PORT
    )
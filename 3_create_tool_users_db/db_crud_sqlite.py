from db_connect import DatabaseConnSQLite
from config import sqlite_connect
from config_sql import tb_name, tb_users, sql_create_user


def db_create_tb(projects):
    with DatabaseConnSQLite(**sqlite_connect) as db:
        cursor = db.cursor()
        for project in projects:
            cursor.execute(tb_users(tb_name(project)))


def db_store(project, first_name, last_name, email, password):
    with DatabaseConnSQLite(**sqlite_connect) as db:
        cursor = db.cursor()
        cursor.execute(sql_create_user(project, first_name, last_name, email, password))


def db_get(sql):
    with DatabaseConnSQLite(**sqlite_connect) as db:
        cursor = db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

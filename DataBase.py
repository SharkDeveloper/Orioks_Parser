from tkinter import SEL
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config import user,password

connection = psycopg2.connect(user = user,password = password,host = "127.0.0.1", port = "5432",database="orioks_parser")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)    
cursor = connection.cursor()

def create_database():
    create_database_query = "create database orioks_parser"
    cursor.execute(create_database_query)

def create_table(Table):
    create_table_query = f"CREATE TABLE {Table} (QUESTION VARCHAR, ANSWER VARCHAR,CORRECT BOOLEAN);"
    cursor.execute(create_table_query)
    print("Таблица создана")

def set_data(Table, QUESTION, ANSWER, CORRECT):
    insert_query = f" INSERT INTO {Table} (QUESTION, ANSWER, CORRECT)VALUES ('{QUESTION}', '{ANSWER}' ,'{CORRECT}');"
    #insert_query = "INSERT INTO Test1 (ID) VALUES (2);"
    cursor.execute(insert_query)
    print(f"Запись добавлена в {Table}")

def get_data(TABLE,QUESTION, ANSWER):
    select_query = f"SELECT {ANSWER} FROM {TABLE} WHERE QUESTION = '{QUESTION}'"
    cursor.execute(select_query)
    print("Данные получены")
    return cursor.fetchone

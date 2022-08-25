import datetime
import json
from xmlrpc.client import boolean
import psycopg2
from psycopg2._psycopg import connection
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import fastapi
import uvicorn
import models
import threading
import os

electronic_database_name = 'electronic_devices_db'
path = os.path.dirname(os.path.abspath(__file__))


def initialize():
    initialize_database()
    initialize_api()
    initialize_timer()


def initialize_database():
    global conn, cursor
    # Connect to (PostgreSQL) database and get the connection object
    try:
        conn = create_connection_to_database(electronic_database_name)
        cursor = conn.cursor()

    except:
        conn = create_connection_to_database('postgres')
        cursor = conn.cursor()
        cursor.execute("create database electronic_devices_db")
        cursor.close()
        conn.close()
        conn = create_connection_to_database(electronic_database_name)
        cursor = conn.cursor()
    cursor.execute(
        "create table if not exists electronic_device_details(name varchar(50) primary key,quantity numeric);")
    cursor.execute(
        "create index if not exists electronic_device_details_name_idx on electronic_device_details(name);")


def initialize_api():
    global app
    app = fastapi.FastAPI()


def initialize_timer():
    config_file = open(f"{path}\\config.json", "r")
    config_file_content = json.load(config_file)
    limit = config_file_content["limit"]
    start_timer(limit)


def start_timer(limit: int):
    timer = threading.Timer(2, check_if_limit_has_exceeded_and_print, [limit])
    timer.daemon = True
    timer.start()


def check_if_limit_has_exceeded_and_print(limit: int):
    try:
        cursor.execute("SELECT COUNT(*) FROM electronic_device_details;")
        count = cursor.fetchall()
        row_count = count[0][0]
        if row_count > limit:
            write_to_application_log(limit)
    finally:
        start_timer(limit)


def write_to_application_log(limit: int):
    application_log_file = open(f"{path}\\application.log", "a")
    application_log_file.write(
        f"{datetime.datetime.now()} --- Electronic device details table exceeded the limit of {limit} rows \n")
    application_log_file.close()


def create_connection_to_database(database_name: str) -> connection:
    conn = psycopg2.connect(
        host='localhost',
        port=5433,
        user='postgres',
        password='pokemon123',
        database=database_name
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return conn


def check_electronic_device_exists(electronic_device_name: str) -> boolean:
    cursor.execute("select name from electronic_device_details;")
    name_rows = cursor.fetchall()
    for row in name_rows:
        if electronic_device_name in row:
            return True
    return False


initialize()


@app.post('/add')
def add(body: models.AddBody):
    if check_electronic_device_exists(body.name):
        return "Add Failed - Electronic device already exists"
    cursor.execute(
        f"INSERT INTO public.electronic_device_details(name, quantity) VALUES ('{body.name}','{body.quantity}');")
    return 'Add successfull'


@app.post('/update_quantity')
def update(body: models.UpdateBody):
    if not check_electronic_device_exists(body.name):
        return "Update Failed - Electronic device does not exist"
    cursor.execute(
        f"UPDATE electronic_device_details SET quantity='{body.quantity}' WHERE name='{body.name}';")
    return 'Update successfull'


@app.post('/delete_device')
def delete(body: models.DeleteBody):
    if not check_electronic_device_exists(body.name):
        return "Delete Failed - Electronic device does not exist"
    cursor.execute(
        f"DELETE FROM electronic_device_details WHERE name='{body.name}';")
    return 'Delete successfull'


@app.get('/get_all_devices')
def get_all_devices():
    cursor.execute("select * from electronic_device_details;")
    rows = cursor.fetchall()
    return rows


uvicorn.run(app, host='localhost', port=1000)
# cursor.close()
# conn.close()

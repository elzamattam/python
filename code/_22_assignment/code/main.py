from xmlrpc.client import boolean
import psycopg2
from psycopg2._psycopg import connection
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import fastapi
import uvicorn
import models
import threading

app = None
conn = None
cursor = None
electronic_database_name = 'electronic_devices_db'


def initialize():
    initialize_database()
    initialize_api()
    initialize_timer()
    uvicorn.run(app, host='localhost', port=1000)


def initialize_database():
    global conn,cursor
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
    timer = threading.Timer(2.0, check_if_limit_has_exceeded_and_print())
    timer.start()


def check_if_limit_has_exceeded_and_print():
    cursor.execute("SELECT COUNT(*) FROM electronic_device_details;")
    count = cursor.fetchall()
    print(count)


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


cursor.close()
conn.close()

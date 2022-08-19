import psycopg2
from psycopg2._psycopg import connection
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import fastapi
import uvicorn
import models

electronic_database_name = 'electronic_devices_db'

# Function to create database


def create_connection_to_database(database_name: str) -> connection:
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        user='postgres',
        password='pokemon123',
        database=database_name
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return conn


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

conn.commit()
cursor.close()
conn.close()

app = fastapi.FastAPI()


@app.post('/add')
def add(body:models.AddBody):
    return 'Add successfull'


@app.post('/update_quantity')
def update(body:models.UpdateBody):
    return 'Update successfull'


@app.post('/delete_device')
def delete(body:models.DeleteBody):
    return 'Delete successfull'


@app.get('/get_all_devices')
def get_all_devices():
    return 'Get successfull'


uvicorn.run(app, host='localhost', port=1000)

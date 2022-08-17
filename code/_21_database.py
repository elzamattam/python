import psycopg2


# Connect to (PostgreSQL) database and get the connection object
connection = psycopg2.connect(
    host='localhost',
    port = 5432,
    user = 'postgres',
    password = 'postgres',
    database = 'postgres'
)

# Create the cursor object
cursor = connection.cursor()

# Execute SQL query - create table
cursor.execute('create table if not exists fruit(id numeric,name varchar(50),colour varchar(50));')

# Execute SQL query - insert row
cursor.execute("insert into fruit(id,name,colour) values(1,'Apple','Red')")

# Execute SQL query - get all rows
cursor.execute('select * from fruit')
rows = cursor.fetchall()  # Get the result of the previously executed query
print(rows)

# Commit the uncommitted transactions which change the database
connection.commit()

# Important! - Close the cursor object as well as connection object after use; better yet, put this in a finally block (and the code above in try block)
cursor.close()
connection.close()
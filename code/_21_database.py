import psycopg2


connection = psycopg2.connect(host='localhost',port = 5432,user = 'postgres',password = 'postgres',database = 'postgres')
cursor = connection.cursor()
cursor.execute('create table if not exists fruit(id numeric,name varchar(50),colour varchar(50));')
cursor.execute("insert into fruit(id,name,colour) values(1,'Apple','Red')")
cursor.execute('select * from fruit')
rows = cursor.fetchall()
print(rows)













connection.commit()

















cursor.close()
connection.close()
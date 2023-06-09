import psycopg2

host = '127.0.0.1'
user = 'postgres' 
password = 'YOU_PSG-CODE'
db_name = 'for_bot'


try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name    
    )
    connection.autocommit = True
    
    # the cursor for perfoming database operations
    # cursor = connection.cursor()
    
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        
        print(f"Server version: {cursor.fetchone()}")
        
    # create a new table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE users(
    #             id serial PRIMARY KEY,
    #             first_name varchar(50) NOT NULL,
    #             nick_name varchar(50) NOT NULL);"""
    #     )
        
    #     # connection.commit()
    #     print("[INFO] Table created successfully")
        
    # insert data into a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO users (first_name, nick_name) VALUES
    #         ('Oleg', 'barracuda');"""
    #     )
        
    #     print("[INFO] Data was succefully inserted")

    # get data from a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT nick_name FROM users WHERE first_name = 'Oleg';"""
    #     )

    #     print(cursor.fetchone())

    # Delete a table
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE users;"""
        )
    print('[INFO] Table was deleted')


except Exception as _ex:
    print('[INFO] Error while working with PostgreSql', _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSql connections closed")

import pyodbc

# Function to create a new database
def createdb(conn, dbname):
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE {dbname};")
    conn.commit()
    cursor.close()

# Function to create a new table
def createtable(conn, tablename):
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE {tablename} (id INT, name VARCHAR(255));")
    conn.commit()
    cursor.close()

# Function to insert data into a table
def createdata(conn, tablename, data):
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {tablename} (id, name) VALUES (?, ?);", data)
    conn.commit()
    cursor.close()

# Function to query data from a table
def querydata(conn, tablename):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tablename};")
    rows = cursor.fetchall()
    cursor.close()
    return rows

# Function to delete data from a table
def deletedata(conn, tablename, condition):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {tablename} WHERE {condition};")
    conn.commit()
    cursor.close()

# Function to drop a table
def droptable(conn, tablename):
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE {tablename};")
    conn.commit()
    cursor.close()

# Function to drop a database
def dropdb(conn, dbname):
    cursor = conn.cursor()
    cursor.execute(f"DROP DATABASE {dbname};")
    conn.commit()
    cursor.close()

# Main function
def main():
    try:
        conn = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=your_server;DATABASE=your_database;UID=your_username;PWD=your_password'
        )
        createdb(conn, "test_db")
        createtable(conn, "test_table")
        createdata(conn, "test_table", (1, "John"))
        rows = querydata(conn, "test_table")
        print(rows)
        deletedata(conn, "test_table", "id=1")
        droptable(conn, "test_table")
        dropdb(conn, "test_db")
        conn.close()
    except pyodbc.Error as e:
        print("Error connecting to SQL Server:", e)

# Run the main function if the script is executed
if __name__ == "__main__":
    main()

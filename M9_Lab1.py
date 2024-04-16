#!/usr/bin/env python3
# William Geesey
# M9_Lab1.py
# query data from a SQL Server DB

import pyodbc

# Function to create a new database
def createdb(conn, dbname):
    """ create db using conn, name, and sqlserver parameters
        parameters:
            conn: open connection
            dbname: database name"""
    # if it already exists, drop the database
    stmt = 'IF DB_ID(\''+ dbname +'\') IS NOT NULL DROP DATABASE '+ dbname
    conn.execute(stmt)
    # create the database
    conn.execute('CREATE DATABASE ' + dbname)
    conn.execute('ALTER DATABASE ' + dbname + ' SET AUTO_CLOSE OFF')
        
    print(f'Database: {dbname} created.')


# Function to create a new table
def createtable(conn, tablename):
    createTableSQL = (f'CREATE TABLE {tablename} ('
        'CustomerID varchar(10),'
        'LastName varchar(255),'
        'FirstName varchar(255),'
        'Address varchar(255),'
        'City varchar(127),'
        'State varchar(2),'
        'Zip varchar(9) );')
    # create the table
    conn.execute(createTableSQL)
    
    print(f'Table: {tablename} created.')


# Function to insert data into a table
def createdata(conn, tablename):
    # create SQL script to insert a row
    
    conn.execute("INSERT INTO " + tablename + 
        " VALUES ('A10001', 'Smith', 'John', '1 Elm St.,', 'Jacksonville', 'FL', '32242')")
    conn.execute("INSERT INTO " + tablename + 
        " VALUES ('B10002', 'Brown', 'Sally', '3 Oak St.,', 'Orlando', 'FL', '32806')")

    print('Data inserted.')


# Function to query data from a table
def querydata(conn, tablename):
    # get a cursor
    cursor = conn.cursor()
    # execute the query
    cursor.execute(f'SELECT * FROM {tablename};')
    # loop through the returned data
    while True:
        cust = cursor.fetchone()
        if cust == None:
            break
        print("Customer:")
        print("\tID: " + cust[0])
        print("\tLName: " + cust[1])
        print("\tFname: " + cust[2])
        
    print('Query complete.')



# Function to delete data from a table
def deletedata(conn, tablename):

    # create SQL script to delete all rows
    conn.execute(f'DELETE FROM {tablename};')
    
    print('Data delete complete.')


# Function to drop a table
def droptable(conn, tablename):
    
    conn.execute(f'DROP TABLE {tablename};')

    print('Table drop complete.')

# Function to drop a database
def dropdb(conn, dbname):
    
    conn.execute(f'DROP DATABASE {dbname};')
    print('Database drop complete.')


# Main function
def main():
    dataB = "Module9"
    table = dataB + ".dbo.table1"
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'
            'Trusted_Connection=yes;',  # use Windows Authentication
            autocommit = True
        )
        createdb(conn, dataB)
        createtable(conn, table)
        createdata(conn, table)
        querydata(conn, table)
        deletedata(conn, table)
        droptable(conn, table)
        dropdb(conn, dataB)
        conn.close()
    except pyodbc.Error as e:
        print("Error connecting to SQL Server:", e)

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
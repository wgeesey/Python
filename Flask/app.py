import pyodbc
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Database connection settings (replace with your SQL Server connection details)
server = 'your_sql_server_address'  # e.g., 'localhost' or IP address
database = 'your_database_name'     # e.g., 'SchoolDB'
username = 'your_username'          # e.g., 'sa'
password = 'your_password'          # e.g., 'password123'

# Establish the connection
def get_db_connection():
    conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                          f'SERVER={server};'
                          f'DATABASE={database};'
                          f'UID={username};'
                          f'PWD={password}')
    return conn

# Home route to display the form
@app.route('/')
def home():
    return render_template('add_student.html')

# Route to handle form submission and add a new student to the database
@app.route('/add_student', methods=['POST'])
def add_student():
    # Get data from the form
    name = request.form['name']
    student_id = request.form['student_id']
    phone = request.form['phone']

    # Validate the phone number (basic check)
    if len(phone) < 10:
        return "Invalid phone number. Please make sure it has at least 10 digits.", 400

    # Insert data into the SQL Server database
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # SQL query to insert a new student
        cursor.execute("""
            INSERT INTO Student (Name, Student_ID, Parents_Phone_Num)
            VALUES (?, ?, ?)
        """, (name, student_id, phone))
        
        # Commit changes and close the connection
        conn.commit()
        cursor.close()
        conn.close()

        # Redirect to home page after successful entry
        return redirect(url_for('home'))

    except Exception as e:
        return f"An error occurred while adding the student: {e}", 500


if __name__ == '__main__':
    app.run(debug=True)

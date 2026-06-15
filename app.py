from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            role TEXT NOT NULL,
            salary REAL NOT NULL,
            join_date TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():

    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    conn.close()

    return render_template(
        'index.html',
        employees=employees
    )

@app.route('/add', methods=['POST'])
def add_employee():

    name = request.form['name']
    department = request.form['department']
    role = request.form['role']
    salary = request.form['salary']
    join_date = request.form['join_date']

    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO employees
        (name, department, role, salary, join_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, department, role, salary, join_date))

    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete_employee(id):

    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/edit/<int:id>')
def edit_employee(id):

    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM employees WHERE id=?",
        (id,)
    )

    employee = cursor.fetchone()

    conn.close()

    return render_template(
        'edit.html',
        employee=employee
    )

@app.route('/update/<int:id>', methods=['POST'])
def update_employee(id):

    name = request.form['name']
    department = request.form['department']
    role = request.form['role']
    salary = request.form['salary']
    join_date = request.form['join_date']

    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE employees
        SET
        name=?,
        department=?,
        role=?,
        salary=?,
        join_date=?
        WHERE id=?
    ''',
    (
        name,
        department,
        role,
        salary,
        join_date,
        id
    ))

    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
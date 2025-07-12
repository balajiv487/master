import sqlite3

def update_employee_salaries(update_rows=None):
    conn=sqlite3.connect('employee.db')
    cur=conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            salary REAL
    """)

    cur.execute("SELECT COUNT(*) FROM employees")
    if  cur.fetchone()[0]==0:
        sample_data = [
            (1, "Alice", 50000),
            (2, "Bob", 60000),
            (3, "Charlie", 70000)
        ]
        cur.executemany(" insert into employees values(???)",sample_data)
        conn.commit()
        cur.execute("SELECT id, name, salary FROM employees")
        rows=cur.fetchall()
        updated_rows = []
        for row in rows:
            id,name,salary=row
            new_salary = salary * 1.10
            updated_rows.append((new_salary,id))
        cur.executemany("UPDATE employees SET salary = ? WHERE id = ?", updated_rows)
        conn.commit()

        cur.execute("SELECT * FROM employees")
        print("Updated employee records:")
        for row in cur.fetchall():
            print(row)

        # 8. Close connection
        conn.close()
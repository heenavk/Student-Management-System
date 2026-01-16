import sqlite3

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"

def add_student(roll, name, marks):
    grade = calculate_grade(marks)
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO student (roll, name, marks, grade) VALUES (?, ?, ?, ?)",
        (roll, name, marks, grade)
    )
    conn.commit()
    conn.close()

def view_students():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student ORDER BY name ASC")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_student(roll):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE roll = ?", (roll,))
    conn.commit()
    conn.close()

import sqlite3 as db

def connection():
    conn = db.connect("student.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS STUDENT 
                    (
                        id INTEGER PRIMARY KEY,
                        studentID TEXT, 
                        student_first_name TEXT,
                        student_surname TEXT, 
                        student_gender TEXT, 
                        student_phone_no TEXT, 
                        student_address TEXT,
                        student_date_of_birth TEXT, 
                        student_age TEXT
                    )''')
    cur.close()
    conn.commit()
    conn.close()


def AddRec(studentID, student_fname, student_surname, student_gender, student_age, studentphone_no,  student_dateofbirth,
           student_address):
    conn = db.connect("student.db")
    cur = conn.cursor()
    cur.execute(" insert into STUDENT values (NULL, ?,?,?,?,?,?,?,?)", (studentID, student_fname, student_surname,
                                                                    student_gender, student_age, studentphone_no,
                                                                    student_dateofbirth, student_address))
    conn.commit()
    conn.close()

def DisplayRec():
    conn = db.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM STUDENT")
    row = cur.fetchall()
    conn.close()
    return row

def deleteRec(id):
    conn = db.connect("student.db")
    cur = conn.cursor()
    cur.execute("delete from STUDENT where id=?", (id,))
    conn.commit()

def searchRec(studentID, student_fname, student_surname, student_gender, student_age, studentphone_no,
           student_dateofbirth, student_address):
    conn = db.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM STUDENT WHERE studentID=? OR student_first_name=? OR student_surname=? OR "
                "student_gender=? OR student_age=? OR student_phone_no=? OR student_date_of_birth=? "
                "OR student_address=?",
                (studentID, student_fname, student_surname, student_gender, student_age, studentphone_no,
                 student_dateofbirth, student_address))
    rows = cur.fetchall()
    conn.close()
    return rows

def updateRec(studentID, student_fname, student_surname, student_gender, studentphone_no, student_address,
           student_dateofbirth, student_age):
    conn = db.connect("student.db")
    cur = conn.cursor()
    cur.execute('UPDATE STUDENT SET studentID=?, student_first_name=?, student_surname=?,'
                'student_gender=?, student_phone_no=?, student_address=?,'
                ' student_date_of_birth=?, student_age=?, WHERE id=?',
                (studentID, student_fname, student_surname,
                 student_gender, studentphone_no, student_address,
                 student_dateofbirth, student_age))
    conn.commit()
    conn.close()


connection()























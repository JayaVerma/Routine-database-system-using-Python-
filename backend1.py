import sqlite3

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY , date text , gaming integer , exercise text , study text , yoga text ,coding text)")
    conn.commit()
    conn.close()

def insert(date , gaming , exercise , study , yoga , coding):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL , ?,?,?,?,?,?)" , (date , gaming , exercise , study , yoga , coding))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=? ", (id,))
    conn.commit()
    conn.close()

def search(date='' , gaming='' , exercise='' , study='' , yoga='' , coding=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=?  OR gaming=? OR exercise=? OR study=? OR yoga=? OR coding=?" , (date , gaming , exercise , study , yoga , coding))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()
print("backend is working")
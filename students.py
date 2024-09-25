import sqlite3

import requests
from data_dict import random_users




# CREATE TABLE
def createTable():
    with sqlite3.connect('students.db') as conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS students
            (id INTEGER PRIMARY KEY , 
            first_name TEXT, 
            last_name TEXT,
            birth_date TEXT,
            email TEXT,
            phonenumber TEXT,
            address TEXT,
            nationality TEXT,
            active BOOLEAN,
            github_username TEXT
            )""")
       
    

    conn.executemany('''INSERT INTO students (
             first_name,
             last_name,
             birth_date,
             email,
             phonenumber,
             address,
             nationality,
             active,
             github_username
             ) VALUES (:first_name, :last_name, :birth_date, :email, :phonenumber, :address, :nationality, :active, :github_username)''', random_users)
    
    conn.commit()

#createTable()




# GET ALL STUDENTS    
def read():
    students = []
    with sqlite3.connect('students.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM students')

        for i in cur.fetchall():
            students.append(i)

    return students




# DELETE A STUDENT
def delete_student_by_id(id):
    with sqlite3.connect('students.db') as conn:
        cur = conn.cursor()

        cur.execute('DELETE FROM students WHERE id = ?', (id,))
        conn.commit()

        if cur.rowcount == 0:
            return {"error": "Student not found"}, 404
        
        return {"message": "Student deleted succesfully"}, 200






# UPDATE GITHUB_USERNAME
def update_github_username(id, github_username):

   with sqlite3.connect('students.db') as conn:
        cur = conn.cursor()

        cur.execute('UPDATE students SET github_username = ? WHERE id = ?', (github_username, id))
        conn.commit()

        if cur.rowcount == 0:
            return {"error": "Student not found"}, 404
        
        return {"message": "GitHub username updated successfully"}, 200





# (SPECIFY) GET ALL STUDENTS
def all_students():

    with sqlite3.connect('students.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT id, first_name, last_name, github_username FROM students')
        students = cur.fetchall()
    
    return students





# FETCH REPO
def fetch_github_repos(username):
    url = f'https://api.github.com/users/{username}/repos'
    headers = {
        "Authorization": " " # Ens GitHub-Token skal indsættes her.
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repos_data = response.json()

        return [{"name": repo["name"], "url": repo["html_url"]} for repo in repos_data]
    elif response.status_code == 404:
        return {"error": "GitHub username not found"}
    
    else:
        return {"error": f"Failed to fetch repositories (status code: {response.status_code})"}
        
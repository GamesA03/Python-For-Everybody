import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
                  
CREATE TABLE User (
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name        TEXT Unique
);
                  
CREATE TABLE Course (
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title       TEXT Unique              
);
 
CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)              
)                                                     
''')

fname = input('Enter file name:  ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0];
    title = entry[1];
    role = entry[2];

    print((name, title, role))

    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES ( ? )''', ( name, ))
    cur.execute('SELECT id FROM User WHERE name = ? ', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES ( ? )''', ( title, ))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id) VALUES ( ?, ? )''', ( user_id, course_id ))
    cur.execute('''INSERT OR REPLACE INTO Member (role) VALUES (?)''', (role,))

    cur.execute('''SELECT user.name, member.role, course.title from user JOIN Member JOIN Course 
                on member.user_id = user.id and member.course_id = course.id ORDER by course.title, member.role DESC, 
                user.name''')

conn.commit()
  

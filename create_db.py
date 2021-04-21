# -*- coding: utf-8 -*- 
import sqlite3

# الاتّصال بقاعدة البيانات 
# You can create a new database by changing the name within the quotes
db = sqlite3.connect('database.db')

# إنشاء مُؤشّر في قاعدة البيانات لنتمكّن من تنفيذ استعلامات 
# The database will be saved in the location where your 'py' file is saved
cursor = db.cursor()

# إنشاء الجدول 
# Create table - CLIENTS
cursor.execute('''CREATE TABLE posts
             (
                 [id] INTEGER PRIMARY KEY,
                 [title] CHAR(200),
                 [content] TEXT
            )
        ''')


# إدخال القيم إلى الجدول 
cursor.execute('''INSERT INTO posts(title, content) VALUES(?,?)''', (u'عنوان المقال الأول', u'محتوى المقال الأول'))
cursor.execute('''INSERT INTO posts(title, content) VALUES (?,?)''', (u'عنوان المقال الثّاني', u'مُحتوى المقال الثّاني'))


db.commit()
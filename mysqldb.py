import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="chatbot"
)

cursor = mydb.cursor()

cursor.execute("""CREATE DATABASE IF NOT EXISTS chatbot""")

cursor.execute("""CREATE TABLE IF NOT EXISTS parent_replay
    (parent_id VARCHAR(255) PRIMARY KEY,
     comment_id VARCHAR(255) UNIQUE,
     parent VARCHAR(255),
     comment VARCHAR(255),
     subreddit VARCHAR(255),
     unix INTEGER,
     score INTEGER
     )""")

mydb.commit()
mydb.close()

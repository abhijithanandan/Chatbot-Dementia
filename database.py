import sqlite3
import json
from datetime import datetime

timeframe = '2018-01'
sql_transaction = []

connection = sqlite3.connect('{}.db'.format(timeframe))
c = connection.cursor()


def create_table():
    c.execute("""CREATE TABLE IF NOT EXIST parent_replay
    (parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT,
     comment TEXT, subreddit TEXT, unix INT, score INT)""")


if __name__ == "__main__":
    create_table()

import sqlite3
import os

def create_nial():
    db = sqlite3.connect(os.path.realpath('../database/counters.db'))
    c = db.cursor()
    c.execute('DROP TABLE IF EXISTS NialCount')
    c.execute('''CREATE TABLE IF NOT EXISTS NialCount(
                guildID BLOB NOT NULL,
                userID BLOB NOT NULL,
                nialCount INTEGER,
                PRIMARY KEY(guildID, userID)
                )''')
    c.execute(('''CREATE UNIQUE INDEX giduid ON NialCount(guildID, userID)'''))
    db.close

create_nial()
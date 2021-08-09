from datetime import datetime
import time
import mysql.connector as mysql
import random


class DB_Conn:
    def __init__(self):
        self.conn=mysql.connect(
            host = "localhost",
            user = "root",
            passwd ="",
            database = "insurance_db")
        self.cursor = self.conn.cursor()


def read_last_min(cursor):
    current = get_current_timestamp()
    start = current - random.randint(1,10)
    
    query = "SELECT * FROM user_tab WHERE timestamp > " + str(start)

    cursor.execute(query)

    records = cursor.fetchall()
    return records

def get_current_timestamp():
    now = datetime.now()
    timestamp = int(datetime.timestamp(now))
    return timestamp

def get_random_age():
    return random.randint(45,90)
    

def main():
    
    while True:
        db = DB_Conn() 
        r=read_last_min(db.cursor)
        time.sleep(random.randint(1,100)/500)
        


if __name__ == "__main__":
    main()

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
        print(self.conn)
        self.cursor = self.conn.cursor()


def random_insert(cursor):
    query = "INSERT INTO user_tab (timestamp, age) VALUES (%s , %s)"
    values = (get_current_timestamp(), get_random_age())

    cursor.execute(query,values)

def get_current_timestamp():
    now = datetime.now()
    timestamp = int(datetime.timestamp(now))
    return timestamp

def get_random_age():
    return random.randint(45,90)
    

def main():
    
    db = DB_Conn() 
    
    while True:
        random_insert(db.cursor)
        db.conn.commit()
        time.sleep(random.randint(0,100)/1000)        


if __name__ == "__main__":
    main()

#!/usr/bin/env python

# module mysql-connector-python
import mysql.connector
from mysql.connector import errorcode

HOSTNAME = "localhost"
PORT = 3306
USERNAME = "user"
PASSWORD = "__puser__"
DBNAME = "data"

def get_connector(hostname:str, port:int, db_name:str, username:str, password:str):
    conn = mysql.connector.connect(
        host = hostname,
        port = port,  # by default
        user = username,
        password = password,
        database = db_name
    )
    return conn

def execute_cmd(conn, cmd:str) -> list:
    cursor = conn.cursor()
    print(cmd)
    cursor.execute(cmd)
    lresults = cursor.fetchall()
    cursor.close()
    conn.commit()
    
    return lresults

if __name__ == "__main__":
    
    conn = get_connector(HOSTNAME, PORT, DBNAME, USERNAME, PASSWORD)
    
    prompt = "Enter a sql command: "
    cmd = input(prompt)
    while cmd.strip() != "":
        lresult = execute_cmd(conn, cmd)
        print(lresult)
        cmd = input(prompt)

    print("Good bye")
    conn.close()


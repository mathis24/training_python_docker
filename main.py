#!/usr/bin/env python

from datetime import datetime
import time
import logging
import logging.handlers
import requests
import argparse

import mysql.connector

# #################################
# Global vars

CURRENCIES = ["EUR", "USD", "CHF", "GBP", "JPY", "TRY"]
WAITING_TIME = 60

# for DB
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "data"
TABLENAME = "quotes" # assumed: create table quotes (time DATETIME, currency VARCHAR(16), exrate DECIMAL)
USERNAME = "user"
PASSWORD = "__puser__"

# for rest API
ACCESS_KEY = "9036b7da90ca089457b0a4183d7579a1"
URL = "http://apilayer.net/api/live?access_key={}&currencies={}&source=USD"

# logger

g_logger = logging.getLogger("logger")
DEFAULT_LEVEL = logging.INFO

# #################################
# Parse command line

parser = argparse.ArgumentParser()

parser.add_argument('-l', '--level', action='store',
                    dest='logging_level',
                    default="info",
                    help='level of logging')

results = parser.parse_args()

# # #################################
# Logger

def get_level(levelname:str):
    # could be simpler with logging._nameToLevel
    
    levelname = levelname.lower()
    dlevel = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }
    if levelname in dlevel:
        return dlevel[levelname]
    else:
        return DEFAULT_LEVEL


def set_logger(g_logger, level):
    formatter = logging.Formatter("[%(name)s %(levelname)s]-%(asctime)s %(message)s","%Y-%m-%d %H:%M:%S") 
    
    # file handler
    fileHandler = logging.handlers.RotatingFileHandler('myserver.log', maxBytes=1024*1024, backupCount=3)
    fileHandler.setFormatter(formatter)

    # console output handler
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    # attach handler to logger
    g_logger.addHandler(fileHandler)
    g_logger.addHandler(streamHandler)

    g_logger.setLevel(level) # by default warning is the lowest (CRITICAL 50, ERROR 40, WARNING 30, INFO 20, DEBUG 10)
    

# #################################
# DB connection

def get_connector(hostname:str, port:int, db_name:str, username:str, password:str):
    conn = mysql.connector.connect(
        host = hostname,
        port = port,  # by default
        user = username,
        password = password,
        database = db_name
    )
    return conn

# #################################
# DB insertion

def insert_values_in_db(conn, ts:int, dvalues:dict[str,float]) -> None:
    """insert data in table

    Args:
        conn (_type_): _description_
        ts (int): timestamp returned by api call
        dvalues (dict[str,float]): [country code: exchange rate value]
    """
    dt = datetime.utcfromtimestamp(ts)
    sdt = dt.strftime("%Y-%m-%d %H:%M:%S")
    
    cursor = conn.cursor()
    for k, v in dvalues.items():
        cmd = f'INSERT INTO {TABLENAME} VALUES ("{sdt}", "{k}", {v})'
        cursor.execute(cmd)
    cursor.close()
    conn.commit()
    

# #################################
# Rest API call

def get_url():
    return URL.format(ACCESS_KEY, ",".join(CURRENCIES))

def get_currencies(url:str, lcurrencies:list[str]) -> tuple[int, dict[str, float]]:
    """get exchange rate

    Args:
        url (str): url
        lcurrencies (list[str]): list of currencies to get

    Returns:
        tuple[int, dict[str, float]]: (timestamp, dict[currency code, exchange rate])
    """
    
    response = requests.get(url)
    
    if response.status_code >= 300:
        g_logger.error(f"get {url} failed")
        return (None, None)
    
    drep = response.json()

    # put result in dictionary
    dretval = {}
    for currency, val in drep["quotes"].items(): # currency s.a. "USDEUR"
        dretval[currency.lstrip('USD')] = val
        
    return (drep["timestamp"], dretval)

# #################################
# Main

if __name__ == "__main__":
    # set logger level and attach handlers
    level = get_level(results.logging_level)
    set_logger(g_logger)
    
    conn = get_connector(DB_HOST, DB_PORT, DB_NAME, USERNAME, PASSWORD)
    g_logger.info("db connected")
    
    url = get_url()
    g_logger.debug(f"url is: {url}")
    
    while True:
        g_logger.info("Get exchange rates ...")
        timestamp, dvalues = get_currencies(url, CURRENCIES)
        if timestamp:
            insert_values_in_db(conn, timestamp, dvalues)
            g_logger.info(f"Insert done: {len(dvalues)} exchange rates")
            
        g_logger.info(f"Wait {WAITING_TIME} secs ...")
        time.sleep(WAITING_TIME)
            

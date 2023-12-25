import os
import socket
import shutil
import psutil
import mysql.connector
from dotenv import load_dotenv
import time
load_dotenv()


def print_with_time(str):
    print(time.ctime() + ": " + str)

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_memory_usage():
    mu = psutil.virtual_memory().available
    total = mu / (1024.0 ** 2)
    return total > 500

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 80

def check_mysql():
    print_with_time("Connect to mysql server:" + os.environ.get('DB_HOST') + " username:" + os.environ.get('DB_USERNAME'))
    try:
        cnx = mysql.connector.connect(
            host= os.environ.get('DB_HOST'),
            user=os.environ.get('DB_USERNAME'),
            password=os.environ.get('DB_PASSWORD')
)
    except:
       return False
    
    return True

def check_liveness():
    return True, 'it works'

def check_readness():
    if not check_cpu_usage():
      return False, 'In Sufficient CPU'
    
    if not check_memory_usage():
      return False, 'In Sufficient Memory'  

    if not check_mysql():
      return False, 'SQL Fail'  

    if not check_disk_usage('/'):
      return False, 'In Sufficient Disk'  
    
    return True, 'Working Properly'

import os
import socket
import shutil
import psutil


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

def check_liveness():
    return True, 'it works'

def check_readness():
    if not check_cpu_usage():
      return False, 'In Sufficient CPU'
    
    if not check_memory_usage():
      return False, 'In Sufficient Memory'  
    
    return True, 'Working Properly'



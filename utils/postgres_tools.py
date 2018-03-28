import platform
from .which import which

sufix = ""
if platform.system() == "Windows":
    sufix = ".exe"

def get_program(program):    
    temp = which(program + sufix)
    if temp is None:
        raise Exception("[ERROR] Postgres Tools must be installed to use this application. Check if they're are installed and are in your path.")
    return temp

def pg_dump():                
    return get_program("pg_dump")

def pg_restore():
    return get_program("pg_restore")
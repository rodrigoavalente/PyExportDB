import os
from enum import Enum

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

class ItensIDs(Enum):
    NEW_DB_CONN = 1
    MANAGE_DBS_CONN = 2
    ABOUT = 3    

from .base_service import BaseService
from dbaccessor.db import HostModel

class HostService(BaseService):

    def __init__(self):
        super(HostService, self).__init__(HostModel)

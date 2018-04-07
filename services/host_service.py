from .base_service import BaseService
from dbaccessor.db import HostModel


class HostService(BaseService):
    def __init__(self):
        super(HostService, self).__init__(HostModel)

    def flattern_hosts_to_list(self):
        hosts = self.get_all()
        return [[host.description, host.username, host.password, host.host_url] for host in hosts]

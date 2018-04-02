from wx import ID_EXIT
from .base_menu import BaseMenu
from configuration import ItensIDs

class FileMenu(BaseMenu):
    def __init__(self, *args, **kwargs):
        super(BaseMenu, self).__init__(*args, **kwargs)
        self.create_items()

    def create_items(self):
        self.new_database_connection_item()
        self.manage_database_connections_item()
        self.exit_item()

    def new_database_connection_item(self):
        self.Append(ItensIDs.NEW_DB_CONN.value, "&Adicionar Nova Connexão...\tCtrl-N",
            "Adiciona uma nova conexão de banco de dados.")

    def manage_database_connections_item(self):
        self.Append(ItensIDs.MANAGE_DBS_CONN.value, "&Gerenciar Conexões...\tCtrl-M",
            "Gerencie suas conexões de banco de dados.")

    def exit_item(self):
        self.Append(ID_EXIT, "&Sair...\tCtrl-Q",
            "Encerra a aplicação.")
from wx import MenuBar
from .items.file_menu import FileMenu
from .items.help_menu import HelpMenu


class ExportDBMenuBar(MenuBar):
    file_menu = None
    help_menu = None

    def __init__(self, *args, **kwargs):
        super(ExportDBMenuBar, self).__init__(*args, **kwargs)

        self.file_menu = FileMenu()
        self.help_menu = HelpMenu()

        self.Append(self.file_menu, "&Arquivo")
        self.Append(self.help_menu, "&Ajuda")

    def get_item(self, menu_name, item_id):
        if menu_name == "file":
            return self.file_menu.get_item_by_id(item_id)
        elif menu_name == "help":
            return self.help_menu.get_item_by_id(item_id)

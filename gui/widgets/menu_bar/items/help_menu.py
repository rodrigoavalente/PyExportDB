from .base_menu import BaseMenu
from configuration import ItensIDs

class HelpMenu(BaseMenu):
    def __init__(self, *args, **kwargs):
        super(HelpMenu, self).__init__(*args, **kwargs)
        self.about_item()

    def about_item(self):
        self.Append(ItensIDs.ABOUT.value, "&Sobre...\tCtrl-H",
            "Informações sobre essa aplicação.")

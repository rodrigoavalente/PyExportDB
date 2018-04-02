from wx import Menu

class BaseMenu(Menu):
    def __init__(self, *args, **kwargs):
        super(BaseMenu, self).__init__(*args, **kwargs)

    def get_item_by_id(self, item_id):
        return self.FindItemById(item_id)
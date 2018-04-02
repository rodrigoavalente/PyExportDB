import wx
from configuration import ItensIDs
from dbaccessor.db import disconnect_from_local_db
from gui.widgets.menu_bar.menu_bar import ExportDBMenuBar
from gui.widgets.dialogs.connection_dialog import AddNewConnectionDialog


class MainFrame(wx.Frame):
    menu = None

    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)

        panel = wx.Panel(self)

        self.menu = ExportDBMenuBar()
        self.SetMenuBar(self.menu)
        self.append_events()
        self.CreateStatusBar()
        self.SetStatusText("Bem Vindo ao PyExportDB")

    def append_events(self):
        self.Bind(wx.EVT_MENU, self.on_exit,
                  self.menu.get_item("file", wx.ID_EXIT))
        self.Bind(wx.EVT_MENU, self.on_about, self.menu.get_item(
            "help", ItensIDs.ABOUT.value))
        self.Bind(wx.EVT_MENU, self.on_add_new_connection,
                  self.menu.get_item("file", ItensIDs.NEW_DB_CONN.value))

    def on_exit(self, event):
        """Close the frame, terminating the application."""
        disconnect_from_local_db()
        self.Close(True)

    def on_about(self, event):
        wx.MessageBox("Assistente para gerenciar importação e exportação de arquivos de banco de dados.",
                      "PyExportDB",
                      wx.OK | wx.ICON_INFORMATION)

    def on_add_new_connection(self, event):
        dialog = AddNewConnectionDialog(None)
        dialog.ShowModal()
        dialog.Destroy()

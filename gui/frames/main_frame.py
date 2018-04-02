import wx
from configuration import ItensIDs
from dbaccessor.db import disconnect_from_local_db
from gui.widgets.menu_bar.menu_bar import ExportDBMenuBar


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
        self.Bind(wx.EVT_MENU, self.OnExit,
                  self.menu.get_item("file", wx.ID_EXIT))
        self.Bind(wx.EVT_MENU, self.OnAbout, self.menu.get_item(
            "help", ItensIDs.ABOUT.value))

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        disconnect_from_local_db()
        self.Close(True)

    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")

    def OnAbout(self, event):
        wx.MessageBox("Assistente para gerenciar importação e exportação de arquivos de banco de dados.",
                      "PyExportDB",
                      wx.OK | wx.ICON_INFORMATION)

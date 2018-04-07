import wx
from .application import BaseFrame
from .dialogs import NewConnectionDialog, ManageConnectionDialog


class MainFrame(BaseFrame):
    def on_close(self, event):
        self.Close(True)

    def on_show_about(self, event):
        wx.MessageBox("Assistente para gerenciar importação e exportação de arquivos de banco de dados.",
                      "PyExportDB",
                      wx.OK | wx.ICON_INFORMATION)

    def on_open_new_connection(self, event):
        dialog = NewConnectionDialog(None)
        dialog.ShowModal()
        dialog.Destroy()

    def on_open_manage_connection(self, event):
        dialog = ManageConnectionDialog(None)
        dialog.ShowModal()
        dialog.Destroy()

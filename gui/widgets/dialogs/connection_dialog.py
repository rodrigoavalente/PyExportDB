import wx


class AddNewConnectionDialog(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super(AddNewConnectionDialog, self).__init__(*args, **kwargs)

        self.init_ui()
        self.SetSize((250, 250))
        self.SetTitle("Adicionar Nova Conexão")

    def init_ui(self):
        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        static_box = wx.StaticBox(pnl, label="Dados da Conexão")
        static_box_sizer = wx.StaticBoxSizer(static_box, orient=wx.VERTICAL)

        pnl.SetSizer(static_box_sizer)

        vbox.Add(pnl, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)

        self.SetSizer(vbox)

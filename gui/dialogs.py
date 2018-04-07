import wx
from peewee import DoesNotExist
from dbmanager.dbmanager import DatabaseManager
from services.host_service import HostService
from .application import BaseConnectionDialog, BaseManageConnection


class NewConnectionDialog(BaseConnectionDialog):
    host_service = None

    def __init__(self, *args, **kwargs):
        super(NewConnectionDialog, self).__init__(*args, **kwargs)
        self.host_service = HostService()

    def on_save_db_connection(self, event):
        data = {
            'username': self.username_field.GetValue(),
            'password': self.password_field.GetValue(),
            'host_url': self.host_url_field.GetValue(),
            'description': self.description_field.GetValue()
        }

        try:
            dbmanager = DatabaseManager(user=data.get('username'), password=data.get(
                'password'), host=data.get('host_url'))
            dbmanager.test_connection()
            self.host_service.add(data)
            wx.MessageBox("A conexão foi adicionada com sucesso.",
                          "Conexão Salva com Sucesso",
                          wx.OK | wx.ICON_INFORMATION)
            self.clean_fields()
        except Exception as e:
            wx.MessageBox("Não foi possível se comunicar com o banco de dados. Verifique os dados e tente novamente.",
                          "Falha ao se Comunicar com o Banco de Dados",
                          wx.OK | wx.ICON_ERROR)

    def clean_fields(self):
        self.username_field.SetValue("")
        self.password_field.SetValue("")
        self.host_url_field.SetValue("")
        self.description_field.SetValue("")

    def on_close_modal(self, event):
        self.Destroy()


class ManageConnectionDialog(BaseManageConnection):
    update_item = None
    host_service = None

    def __init__(self, *args, **kwargs):
        super(ManageConnectionDialog, self).__init__(*args, **kwargs)

        self.host_service = HostService()
        connections = self.host_service.get_all(order_by_field="description")
        self.connections_choices.AppendItems([connection.description for connection in connections])
        for data in [[str(connection.id), connection.description, connection.username, connection.host_url] for
                     connection in connections]:
            self.connections_data_view.AppendItem(data)

    def on_selected_connection(self, event):
        index = self.connections_choices.GetCurrentSelection()
        connection_name = self.connections_choices.GetString(index)

        try:
            self.update_item = self.host_service.get_by_field(field="description", value=connection_name)
            if self.update_item:
                self.username_field.SetValue(self.update_item.username)
                self.password_field.SetValue(self.update_item.password)
                self.host_url_field.SetValue(self.update_item.host_url)
                self.description_field.SetValue(self.update_item.description)
        except DoesNotExist:
            self.clean_fields()

    def on_update_connection(self, event):
        data = {
            'username': self.username_field.GetValue(),
            'password': self.password_field.GetValue(),
            'host_url': self.host_url_field.GetValue(),
            'description': self.description_field.GetValue()
        }

        try:
            self.host_service.update(self.update_item.id, data)
            wx.MessageBox("A conexão foi atualizada com sucesso.",
                          "Conexão Atualizada com Sucesso",
                          wx.OK | wx.ICON_INFORMATION)
            self.clean_fields()
        except Exception as e:
            wx.MessageBox("Não foi possível atualizar a conexão. Verifique os dados e tente novamente.",
                          "Falha ao sAtualizar Conexão",
                          wx.OK | wx.ICON_ERROR)

    def on_delete_connections(self, event):
        dialog = wx.MessageDialog(self, "Tem certeza de que deseja deletar estas conexões?", "Removendo Conexões",
                                  wx.YES_NO | wx.ICON_QUESTION)

        result = dialog.ShowModal() == wx.ID_YES
        if result:
            self.do_delete_connections()
        dialog.Destroy()

    def do_delete_connections(self):
        rows = [self.connections_data_view.ItemToRow(connection) for connection in
                self.connections_data_view.GetSelections()]
        ids = [self.connections_data_view.GetValue(row, 0) for row in rows]
        rows_ids = list(zip(rows, ids))
        errors = []

        for row, model_id in rows_ids:
            try:
                self.host_service.delete_by_id(model_id)
            except Exception:
                errors.append("Não foi possível excluir a conexão '%s'." % self.connections_data_view.GetValue(row, 1))
                rows.remove(row)
        for row in rows:
            self.connections_data_view.DeleteItem(row)
        if len(errors) > 0:
            wx.MessageBox("\n".join(errors) + "\n As conexões não mencionadas foram excluídas com sucesso.",
                          "Falha ao excluir conexões",
                          wx.OK | wx.ICON_ERROR)
        else:
            wx.MessageBox("As conexões foram removidas com sucesso.",
                          "Conexões Removidas com Sucesso",
                          wx.OK | wx.ICON_INFORMATION)
        self.remake_choices()

    def remake_choices(self):
        self.connections_choices.Clear()
        connections = self.host_service.get_all(order_by_field="description")
        self.connections_choices.AppendItems(
            ["Escolha uma Conexão"] + [connection.description for connection in connections])
        self.connections_choices.SetSelection(0)
        self.clean_fields()

    def clean_fields(self):
        self.username_field.SetValue("")
        self.password_field.SetValue("")
        self.host_url_field.SetValue("")
        self.description_field.SetValue("")

    def on_close_modal(self, event):
        self.Destroy()

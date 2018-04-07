# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Apr  2 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class BaseFrame
###########################################################################

class BaseFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyExportDB", pos = wx.DefaultPosition, size = wx.Size( 775,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.menu_bar = wx.MenuBar( 0 )
		self.file_menu = wx.Menu()
		self.new_db_connection = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Nova Conexão"+ u"\t" + u"Ctrl+N", u"Crie Novas Conexões de Banco de Dados", wx.ITEM_NORMAL )
		self.file_menu.Append( self.new_db_connection )
		
		self.manage_connection = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Gerenciar Conexões"+ u"\t" + u"Ctrl+M", u"Gerencie suas Conexões de Banco de Dados", wx.ITEM_NORMAL )
		self.file_menu.Append( self.manage_connection )
		
		self.file_menu.AppendSeparator()
		
		self.exit_application = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Sair"+ u"\t" + u"Ctrl+Q", u"Encerrar a Aplicação", wx.ITEM_NORMAL )
		self.file_menu.Append( self.exit_application )
		
		self.menu_bar.Append( self.file_menu, u"Arquivo" ) 
		
		self.tools_menu = wx.Menu()
		self.new_backup = wx.MenuItem( self.tools_menu, wx.ID_ANY, u"Novo Backup"+ u"\t" + u"Ctrl+B", u"Realiza um novo backup a partir de uma conexão existente.", wx.ITEM_NORMAL )
		self.tools_menu.Append( self.new_backup )
		
		self.manage_backups = wx.MenuItem( self.tools_menu, wx.ID_ANY, u"Gerenciar Backups"+ u"\t" + u"Ctrl+O", u"Gerencia os backups já criados.", wx.ITEM_NORMAL )
		self.tools_menu.Append( self.manage_backups )
		
		self.tools_menu.AppendSeparator()
		
		self.export_database_or_backup = wx.MenuItem( self.tools_menu, wx.ID_ANY, u"Exportar Banco de Dados/Backup"+ u"\t" + u"Ctrl+X", u"Exporta um banco de dados ou backup para de uma conexão existente para outra.", wx.ITEM_NORMAL )
		self.tools_menu.Append( self.export_database_or_backup )
		
		self.tools_menu.AppendSeparator()
		
		self.open_backup_folder = wx.MenuItem( self.tools_menu, wx.ID_ANY, u"Abrir Pasta de Backups"+ u"\t" + u"Ctrl+T", u"Abre a pasta em que os backups estão armazenados.", wx.ITEM_NORMAL )
		self.tools_menu.Append( self.open_backup_folder )
		
		self.menu_bar.Append( self.tools_menu, u"Ferramentas" ) 
		
		self.help_menu = wx.Menu()
		self.about_pyexport_db = wx.MenuItem( self.help_menu, wx.ID_ANY, u"Sobre"+ u"\t" + u"Ctrl+H", u"Sobre o PyExportDB", wx.ITEM_NORMAL )
		self.help_menu.Append( self.about_pyexport_db )
		
		self.menu_bar.Append( self.help_menu, u"Ajuda" ) 
		
		self.SetMenuBar( self.menu_bar )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.on_open_new_connection, id = self.new_db_connection.GetId() )
		self.Bind( wx.EVT_MENU, self.on_open_manage_connection, id = self.manage_connection.GetId() )
		self.Bind( wx.EVT_MENU, self.on_close, id = self.exit_application.GetId() )
		self.Bind( wx.EVT_MENU, self.on_show_about, id = self.about_pyexport_db.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_open_new_connection( self, event ):
		event.Skip()
	
	def on_open_manage_connection( self, event ):
		event.Skip()
	
	def on_close( self, event ):
		event.Skip()
	
	def on_show_about( self, event ):
		event.Skip()
	

###########################################################################
## Class BaseConnectionDialog
###########################################################################

class BaseConnectionDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Nova Conexão", pos = wx.DefaultPosition, size = wx.Size( 452,396 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Dados da Conexão" ), wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Nome de Usuário", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		sbSizer3.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.username_field = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.username_field, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Senha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		sbSizer3.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.password_field = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		sbSizer3.Add( self.password_field, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"URL do Host", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		sbSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.host_url_field = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.host_url_field, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText8 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Descrição", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		sbSizer3.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.description_field = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.description_field, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer3, 1, wx.ALL|wx.EXPAND, 5 )
		
		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1Apply = wx.Button( self, wx.ID_APPLY )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Apply )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();
		
		bSizer2.Add( m_sdbSizer1, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_sdbSizer1Apply.Bind( wx.EVT_BUTTON, self.on_save_db_connection )
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.on_close_modal )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_save_db_connection( self, event ):
		event.Skip()
	
	def on_close_modal( self, event ):
		event.Skip()
	

###########################################################################
## Class BaseManageConnection
###########################################################################

class BaseManageConnection ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Gerenciar Conexões", pos = wx.DefaultPosition, size = wx.Size( 613,556 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook4 = wx.Notebook( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebook4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		self.m_panel4 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel4, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Conexão", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		sbSizer3.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		connections_choicesChoices = [ u"Escolha uma Conexão " ]
		self.connections_choices = wx.Choice( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, connections_choicesChoices, wx.CB_SORT )
		self.connections_choices.SetSelection( 0 )
		sbSizer3.Add( self.connections_choices, 0, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Dados da Conexão" ), wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Nome de Usuário", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		sbSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.username_field = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.username_field, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Senha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		sbSizer4.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.password_field = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		sbSizer4.Add( self.password_field, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText8 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"URL do Host", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		sbSizer4.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.host_url_field = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.host_url_field, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.description_static = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Descrição", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.description_static.Wrap( -1 )
		sbSizer4.Add( self.description_static, 0, wx.ALL, 5 )
		
		self.description_field = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.description_field, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer3.Add( sbSizer4, 1, wx.ALL|wx.EXPAND, 5 )
		
		m_sdbSizer3 = wx.StdDialogButtonSizer()
		self.m_sdbSizer3Apply = wx.Button( sbSizer3.GetStaticBox(), wx.ID_APPLY )
		m_sdbSizer3.AddButton( self.m_sdbSizer3Apply )
		self.m_sdbSizer3Cancel = wx.Button( sbSizer3.GetStaticBox(), wx.ID_CANCEL )
		m_sdbSizer3.AddButton( self.m_sdbSizer3Cancel )
		m_sdbSizer3.Realize();
		
		sbSizer3.Add( m_sdbSizer3, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer6.Add( sbSizer3, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel4.SetSizer( bSizer6 )
		self.m_panel4.Layout()
		bSizer6.Fit( self.m_panel4 )
		self.m_notebook4.AddPage( self.m_panel4, u"Editar Conexões", True )
		self.m_panel5 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel5, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.connections_data_view = wx.dataview.DataViewListCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_MULTIPLE|wx.dataview.DV_ROW_LINES|wx.dataview.DV_VERT_RULES )
		self.m_dataViewListColumn5 = self.connections_data_view.AppendTextColumn( u"ID" )
		self.m_dataViewListColumn1 = self.connections_data_view.AppendTextColumn( u"Descrição" )
		self.m_dataViewListColumn2 = self.connections_data_view.AppendTextColumn( u"Usuário" )
		self.m_dataViewListColumn4 = self.connections_data_view.AppendTextColumn( u"URL do Host" )
		sbSizer5.Add( self.connections_data_view, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer7.Add( sbSizer5, 1, wx.ALL|wx.EXPAND, 5 )
		
		m_sdbSizer4 = wx.StdDialogButtonSizer()
		self.m_sdbSizer4Apply = wx.Button( self.m_panel5, wx.ID_APPLY )
		m_sdbSizer4.AddButton( self.m_sdbSizer4Apply )
		self.m_sdbSizer4Cancel = wx.Button( self.m_panel5, wx.ID_CANCEL )
		m_sdbSizer4.AddButton( self.m_sdbSizer4Cancel )
		m_sdbSizer4.Realize();
		
		bSizer7.Add( m_sdbSizer4, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel5.SetSizer( bSizer7 )
		self.m_panel5.Layout()
		bSizer7.Fit( self.m_panel5 )
		self.m_notebook4.AddPage( self.m_panel5, u"Remover Conexões", False )
		
		bSizer4.Add( self.m_notebook4, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel3.SetSizer( bSizer4 )
		self.m_panel3.Layout()
		bSizer4.Fit( self.m_panel3 )
		bSizer3.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.connections_choices.Bind( wx.EVT_CHOICE, self.on_selected_connection )
		self.m_sdbSizer3Apply.Bind( wx.EVT_BUTTON, self.on_update_connection )
		self.m_sdbSizer3Cancel.Bind( wx.EVT_BUTTON, self.on_close_modal )
		self.m_sdbSizer4Apply.Bind( wx.EVT_BUTTON, self.on_delete_connections )
		self.m_sdbSizer4Cancel.Bind( wx.EVT_BUTTON, self.on_close_modal )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_selected_connection( self, event ):
		event.Skip()
	
	def on_update_connection( self, event ):
		event.Skip()
	
	def on_close_modal( self, event ):
		event.Skip()
	
	def on_delete_connections( self, event ):
		event.Skip()
	
	


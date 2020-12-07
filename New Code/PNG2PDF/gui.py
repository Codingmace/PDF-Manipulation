# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PNG to PDF", pos = wx.DefaultPosition, size = wx.Size( 575,522 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.WhatsThis = wx.StaticText( self, wx.ID_ANY, u"Please choose a directory to convert.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WhatsThis.Wrap( -1 )
		self.WhatsThis.SetFont( wx.Font( 20, 73, 90, 90, False, "Comic Sans MS" ) )
		
		bSizer1.Add( self.WhatsThis, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"All files must be in the .PNG format.\nIn addition, their names must be in alphanumerical order.\nFor example:\nimage1.png\nimage2.png\nimage3.png\n...\nimage15.png\n\nPlease proofread PDFs created using this tool.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 14, 73, 93, 90, False, "Comic Sans MS" ) )
		self.m_staticText2.SetForegroundColour( wx.Colour( 128, 0, 64 ) )
		
		bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.DirPicker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer2.Add( self.DirPicker, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"                               ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( 14, 71, 90, 90, False, "Harrington" ) )
		self.m_staticText3.SetForegroundColour( wx.Colour( 128, 0, 64 ) )
		
		bSizer3.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.StartConversion = wx.Button( self, wx.ID_ANY, u"Convert", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.StartConversion.SetFont( wx.Font( 20, 73, 90, 90, False, "Forte" ) )
		self.StartConversion.SetForegroundColour( wx.Colour( 200, 26, 6 ) )
		self.StartConversion.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer3.Add( self.StartConversion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.StartConversion.Bind( wx.EVT_BUTTON, self.TransformFile )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def TransformFile( self, event ):
		event.Skip()
	


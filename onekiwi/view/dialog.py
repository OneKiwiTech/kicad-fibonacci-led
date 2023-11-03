# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FibonacciLedDialog
###########################################################################

class FibonacciLedDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Fibonacci LED", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Unit:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer19.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceUnitChoices = [ u"mm", u"mil", u"in" ]
		self.choiceUnit = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceUnitChoices, 0 )
		self.choiceUnit.SetSelection( 0 )
		bSizer19.Add( self.choiceUnit, 1, wx.ALL, 5 )


		bSizer18.Add( bSizer19, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Number of LEDs:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer7.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editNumber = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.editNumber, 1, wx.ALL, 5 )


		bSizer18.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Scaling factor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer8.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editScaling = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.editScaling, 1, wx.ALL, 5 )

		self.textUnit = wx.StaticText( self, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textUnit.Wrap( -1 )

		bSizer8.Add( self.textUnit, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer18.Add( bSizer8, 1, wx.EXPAND, 5 )

		self.buttonCreate = wx.Button( self, wx.ID_ANY, u"Create", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.buttonCreate, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer18, 0, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonCopy = wx.Button( self, wx.ID_ANY, u"Copy Logs", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.buttonCopy, 1, wx.ALL, 5 )

		self.buttonClear = wx.Button( self, wx.ID_ANY, u"Clear Logs", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.buttonClear, 1, wx.ALL, 5 )


		bSizer10.Add( bSizer12, 0, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )


		bSizer10.Add( bSizer17, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer10, 0, wx.EXPAND, 5 )

		self.staticline = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.staticline, 0, wx.EXPAND |wx.ALL, 5 )

		self.textLog = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,100 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer1.Add( self.textLog, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass



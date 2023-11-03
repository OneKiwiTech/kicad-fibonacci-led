import wx
from .dialog import *

VERSION = '0.0.1'

class FibonacciLedDialogView(FibonacciLedDialog):
    def __init__(self):
        FibonacciLedDialog.__init__(self, None)
        self.SetTitle('Fibonacci LED v%s' % VERSION)
        self.window = wx.GetTopLevelParent(self)

    def HighResWxSize(self, window, size):
        """Workaround if wxWidgets Version does not support FromDIP"""
        if hasattr(window, "FromDIP"):
            return window.FromDIP(size)
        else:
            return size

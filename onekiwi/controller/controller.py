from ..model.model import Model
from ..view.view import FibonacciLedDialogView
from .logtext import LogText
import wx
import sys
import logging
import logging.config

class Controller:
    def __init__(self, board):
        self.view = FibonacciLedDialogView()
        self.board = board
        self.logger = self.init_logger(self.view.textLog)
        self.model = Model(self.board, self.logger)
        self.logger.info('init done')

        # Connect Events
        self.view.buttonCreate.Bind(wx.EVT_BUTTON, self.OnCreatePressed)
        self.view.buttonClear.Bind(wx.EVT_BUTTON, self.OnClearPressed)
        self.view.buttonCopy.Bind(wx.EVT_BUTTON, self.OnCopyPressed)
        

    def Show(self):
        self.view.Show()
    
    def Close(self):
        self.view.Destroy()
    
    def OnCreatePressed(self, event):
        self.logger.info('OnCreatePressed')
        layer = self.view.choiceLayer.GetSelection()
        number = int(str(self.view.editNumber.GetValue()))
        scale = float(str(self.view.editScaling.GetValue()))
        self.model.init_data(layer, number, scale)
        self.model.generate()

    def OnCopyPressed(self, event):
        self.logger.info('OnCopyPressed')

    def OnClearPressed(self, event):
        self.view.textLog.SetValue('')

    def init_logger(self, texlog):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        # Log to stderr
        handler1 = logging.StreamHandler(sys.stderr)
        handler1.setLevel(logging.DEBUG)
        # and to our GUI
        handler2 = LogText(texlog)
        handler2.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(funcName)s -  %(message)s",
            datefmt="%Y.%m.%d %H:%M:%S",
        )
        handler1.setFormatter(formatter)
        handler2.setFormatter(formatter)
        root.addHandler(handler1)
        root.addHandler(handler2)
        return logging.getLogger(__name__)

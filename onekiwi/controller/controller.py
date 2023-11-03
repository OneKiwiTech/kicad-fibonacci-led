from ..model.model import Model
from ..view.view import FibonacciLedDialogView
from .logtext import LogText
import wx
import sys
import math
import pcbnew
import logging
import logging.config
from ..kicad.board import get_current_unit

class Controller:
    def __init__(self, board):
        self.view = FibonacciLedDialogView()
        self.board = board
        self.logger = self.init_logger(self.view.textLog)
        self.model = Model(self.board, self.logger)
        self.page = 0

        self.cur_unit = get_current_unit()
        if self.cur_unit == None:
            self.cur_unit = 'mm'
        self.view.textUnit.SetLabel(self.cur_unit)
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
        origin = self.board.GetDesignSettings().GetGridOrigin()
        x0 = origin.Get()[0]
        y0 = origin.Get()[1]
        circle = pcbnew.PCB_SHAPE(self.board, pcbnew.SHAPE_T_CIRCLE)
        circle.SetCenter(pcbnew.VECTOR2I(x0,y0))
        circle.SetStart(pcbnew.VECTOR2I(x0,y0))
        circle.SetEnd(pcbnew.VECTOR2I(x0+1000000,y0))
        circle.SetWidth(25400) #1mil
        circle.SetLayer(pcbnew.F_SilkS)
        self.board.Add(circle)

        text = pcbnew.PCB_TEXT(self.board)
        text.SetText('999')
        text.SetPosition(pcbnew.VECTOR2I(x0,y0))
        text.SetHorizJustify(pcbnew.GR_TEXT_H_ALIGN_CENTER)
        text.SetTextSize(pcbnew.VECTOR2I(508000,508000)) #20mil
        text.SetTextThickness(25400) #1mil
        text.SetLayer(pcbnew.F_SilkS)
        self.board.Add(text)
        pcbnew.Refresh()

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

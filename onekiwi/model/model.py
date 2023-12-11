import pcbnew
import math
from typing import List

class Model:
    def __init__(self, board, logger):
        self.logger = logger
        self.board:pcbnew.BOARD = board
        origin = self.board.GetDesignSettings().GetGridOrigin()
        self.leds = Fibonacci(origin)
        self.layer = pcbnew.F_SilkS
        self.layers = [pcbnew.F_SilkS, pcbnew.B_SilkS, pcbnew.F_Fab,
                       pcbnew.B_Fab, pcbnew.Dwgs_User, pcbnew.Cmts_User,
                       pcbnew.User_1, pcbnew.User_2]
    
    def init_data(self, layer, number, scale):
        self.layer = self.layers[layer]
        self.leds.n = number
        self.leds.c = scale
    
    def add_circle(self, radius, pos):
        circle = pcbnew.PCB_SHAPE(self.board, pcbnew.SHAPE_T_CIRCLE)
        circle.SetCenter(pos)
        circle.SetStart(pos)
        circle.SetEnd(radius)
        circle.SetWidth(25400) #1mil
        circle.SetLayer(self.layer)
        self.board.Add(circle)

    def add_rect(self, start, end):
        rect = pcbnew.PCB_SHAPE(self.board, pcbnew.SHAPE_T_RECT)
        rect.SetFilled(False)
        rect.SetStart(start)
        rect.SetEnd(end)
        rect.SetWidth(25400) #1mil
        rect.SetLayer(self.layer)
        self.board.Add(rect)

    def add_line(self, start, end):
        line = pcbnew.PCB_SHAPE(self.board, pcbnew.SHAPE_T_SEGMENT)
        line.SetStart(start)
        line.SetEnd(end)
        line.SetWidth(25400) #1mil
        line.SetLayer(self.layer)
        self.board.Add(line)
    
    def add_text(self, txt, pos):
        text = pcbnew.PCB_TEXT(self.board)
        text.SetText(txt)
        text.SetPosition(pos)
        #text.SetPosition(pcbnew.VECTOR2I(x,y))
        text.SetHorizJustify(pcbnew.GR_TEXT_H_ALIGN_CENTER)
        text.SetTextSize(pcbnew.VECTOR2I(508000,508000)) #20mil
        text.SetTextThickness(25400) #1mil
        text.SetLayer(self.layer)
        self.board.Add(text)

    def plot_lines(self):
        for delta in [21, 34]:
            for start in range(34):
                x0, y0 = self.leds.coordinates[0]
                i = start
                while i < len(self.leds.coordinates):
                    x1, y1 = self.leds.coordinates[i]
                    s = pcbnew.VECTOR2I(x0, y0)
                    e = pcbnew.VECTOR2I(x1, y1)
                    self.add_line(s, e)
                    x0 = x1; y0 = y1
                    i += delta
    
    def generate(self):
        i = 0
        self.leds.calculate_coordinates()
        for x,y in self.leds.coordinates:
            pos = pcbnew.VECTOR2I(x,y)
            # radius = 1mm
            radius = pcbnew.VECTOR2I(x+1000000,y)
            self.add_circle(radius, pos)
            text = str(i)
            self.add_text(text, pos)
            i = i+1
        self.plot_lines()
        pcbnew.Refresh()
        
class Fibonacci():
    def __init__(self, origin):
        self.origin = origin
        self.n = 64
        self.c = 3
        self.coordinates = []

    def spiral(self):
        # φ = (1+√5)/2
        # θ = 360*n/φ^2
        # r = c*√n
        n = self.n
        r = self.c
        spirals = []
        for i in range(n+1):
            radius = r*(i**0.5)
            angle = ((i*(360)/(((5**0.5)+1)/2)**2)%360)
            spirals.append(((radius,angle)))
        return spirals

    def polar2cartesian(self, r, theta):
        x = r * math.cos(math.radians(theta))
        y = r * math.sin(math.radians(theta))
        return x,y

    def calculate_coordinates(self):
        x0 = self.origin.Get()[0]
        y0 = self.origin.Get()[1]
        for r, t in self.spiral():
            x,y = self.polar2cartesian(r, t)
            x = int(1000000*round(x, 4))
            y = int(1000000*round(y, 4))
            self.coordinates.append([x0+x,y+y0])

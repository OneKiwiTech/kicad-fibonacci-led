import pcbnew
import math
from typing import List

class Model:
    def __init__(self, board, logger):
        self.logger = logger
        self.board:pcbnew.BOARD = board
        

class Fibonacci():
    def spiral(self, n, r): # works better for first direction
        spirals = []
        for i in range(n+1):
            radius = r*(i**0.5)
            angle = ((i*(360)/(((5**0.5)+1)/2)**2)%360)
            spirals.append(((radius,angle)))
        return spirals

    def pol2cart(self, r, theta):
        x = r * math.cos(math.radians(theta))
        y = r * math.sin(math.radians(theta))
        return x,y

    def calculate_coordinates(self, num_points = 64, distance = 20):
        # do the cartesian conversion
        self.coordinates = [self.pol2cart(r, t) for r, t in self.spiral(num_points, distance)]

        # center for the canvas
        self.coordinates = [(x+250,y+250) for x, y in self.coordinates]

    def plot_numbers(self, canvas):
        h = 1
        self.calculate_coordinates(num_points = 64, distance = 20)
        for x, y in self.coordinates:
            canvas.create_oval(x+7, y+7, x-7, y-7)
            canvas.create_text(x, y, text = h)
            h += 1

    def plot_lines(self, canvas):
        for delta in [21, 34]:
            for start in range(34):
                x0, y0 = self.coordinates[0]
                i = start
                while i < len(self.coordinates):
                    x1, y1 = self.coordinates[i]
                    canvas.create_line(x0, y0, x1, y1)
                    x0 = x1; y0 = y1
                    i += delta

    def clear_highlight_net(self):
        for track in self.tracks:
            track.ClearBrightened()
        pcbnew.Refresh()
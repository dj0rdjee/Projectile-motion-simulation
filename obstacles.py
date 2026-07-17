import numpy
import matplotlib.pyplot as plt

class Wall:
    def __init__(self,x,height):
        self.x = x
        self.height = height
    def check_collision(self, bullet):
        if bullet.x >= self.x and bullet.y <= self.height:
             return True
        return False
    def draw(self, plt):
         plt.plot([self.x, self.x],[0, self.height], color="red", linewidth=3)

class H_Target:
    def __init__(self,x,top,bottom):
            self.x = x
            self.top = top
            self.bottom = bottom
    def check_collision(self, bullet):
        if bullet.x >= self.x and (bullet.x <= self.top and bullet.x >= self.bottom):
            return True
        return False
    def draw(self, plt):
         plt.plot([self.x, self.x], [self.bottom, self.top], color="red", linewidth=3)

class Ceiling:
    def __init__(self,y):
            self.y = y
    def check_collision(self, bullet):
        if bullet.y >= self.y:
             return True
        return False
    def draw(self, plt):
        plt.axhline(y=self.y, color="red", linestyle="-")

class V_Target:
    def __init__(self,y,left,right):
        self.y = y
        self.left = left
        self.right = right
    def check_collision(self, bullet):
        if bullet.y >= self.y and (bullet.x >= self.left and bullet.x <= self.right):
            return True
        return False
    def draw(self, plt):
        plt.plot([self.left, self.right],[self.y, self.y],color="red", linewidth = 3)

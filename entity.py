from gameobject import *
from tools import *

class Entity(Game_object):

    list_object_inrun = []
    def __init__(self, imageup, bank_image, x, y):
        Game_object.__init__(self, imageup, bank_image, x, y)
        Entity.list_object_inrun.append(self)
        self.width = self.imageup.get_width()
        self.height = self.imageup.get_height()

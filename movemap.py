from player import *
from entity import *

class Movemap:

        def up(speed):
            for object in Entity.list_object_inrun:
                object.y += int(speed/2)

        def upleft(speed):
            for object in Entity.list_object_inrun:
                object.y += int(speed /2)
                object.x += int(speed /2)

        def upright(speed):
            for object in Entity.list_object_inrun:
                object.y += int(speed /2)
                object.x -= int(speed /2)

        def down(speed):
            for object in Entity.list_object_inrun:
                object.y -= int(speed /2)

        def downleft(speed):
            for object in Entity.list_object_inrun:
                object.y -= int(speed /2)
                object.x += int(speed /2)

        def downright(speed):
            for object in Entity.list_object_inrun:
                object.y -= int(speed /2)
                object.x -= int(speed /2)

        def left(speed):
            for object in Entity.list_object_inrun:
                object.x += int(speed /2)

        def right(speed):
            for object in Entity.list_object_inrun:
                object.x -= int(speed /2)

import pygame as pg
import glfw as gw
from OpenGL.GL import *
import numpy as np
import Manage_physics as manph
import time
from math import *
gw.init()

class MainSim:

    global ObjectsDico
    ObjectsDico = {}

    def __init__(self, Width, Height):

        self.width = Width
        self.height = Height
        Window = gw.create_window(Width, Height, "Test Simu", None, None)
        self.create_window = Window
        gw.make_context_current(Window)
        glViewport(0, 0, Width, Height)
        while not gw.window_should_close(Window):

            error = glGetError()
            if error != GL_NO_ERROR:
                print(f"Ya une erreur : erreur {error}")
            glClearColor(0, 0, 0, 0)
            glClear(GL_COLOR_BUFFER_BIT)
            self.Run(Window)
            gw.swap_buffers(Window)
            gw.poll_events()
            time.sleep(0.025)
        gw.terminate()
        return None
    
    def Circle(self, x, y, radius, color=[1, 0, 0], segments=30):

        if (WinX := self.width) > (WinY := self.height):

            radius_y = radius
            radius_x = radius_y*(WinY/WinX)
        else :

            radius_x = radius
            radius_y = radius_x*(WinX/WinY)
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(color[0], color[1], color[2])
        glVertex2f(x, y)
        for i in range(segments+1):

            angle = 2.0 * pi * i / segments
            glVertex2f(x+cos(angle)*radius_x, y+sin(angle)*radius_y)
        glEnd()
    
#    def DisplayText(self, x, y, color=[1, 1, 1], Window):
        
    def Run(self, Window):      # Objects and dynamic interactions of the window

        cursor_pos = gw.get_cursor_pos(Window)
        cursor_pos_X = (cursor_pos[0] / self.width) * 2 - 1  # Convert in [-1, 1]
        cursor_pos_Y = 1 - (cursor_pos[1] / self.height) * 2  # Invert Y axis
        self.Circle(0, 0, 0.1, segments=50)
        self.Circle(cursor_pos_X, cursor_pos_Y, 0.05, color=[1, 1, 1])
        if gw.get_key(Window, key=gw.KEY_ENTER) == gw.PRESS:      #If enter key is pressed

            event = input("Event : ")
            event.replace(" ", "")
            event.lower()
            if "create" in event and "object" in event:

                NewObject = self.DefObject(mass=float(input("Masse de l'objet : ")))
                ObjectsDico[NewObject[0]] = NewObject[1]
            else :
                print(f"Nothing was called or the input is incorrect.")
        if gw.get_mouse_button(Window, gw.MOUSE_BUTTON_LEFT()) == gw.PRESS :        # Initialize the StartPosCursor to set the coordinates from the begin of the click

            global StartPosCursor
            StartPosCursor = gw.get_cursor_pos(Window)
        elif gw.get_mouse_button(Window, gw.MOUSE_BUTTON_LEFT()) == gw.REPEAT:      # SwipeDistance is the distance from the last click to move the camera

            global SwipeDistance
            SwipeDistance = [0, 0]
            for i in range(2):
                SwipeDistance[i] = gw.get_cursor_pos(Window)[i] - StartPosCursor[i]
            tuple(SwipeDistance)

    def DefObject(self, name=input("Nom de l'objet : "), x:float=0, y:float=0, mass:float=0, color:list=[1, 1, 1]):

        return [name, [mass, [x, y]], color]
    
    def ShowInfos(self, objects:list):

        for obj in objects:

            print(f"{obj[0]}\n\tMass : {obj[1][0]}\n\tPosition : {obj[1][1]}\n\tCouleur : {obj[2]}\n")
    
WinTest = MainSim(1200, 800)
WinTest.create_window

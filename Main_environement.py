import pygame as pg
import glfw as gw
from OpenGL.GL import *
import numpy as np
import Manage_physics as manph
import time
from math import *
gw.init()

class MainSim:

    def __init__(self, Width, Height):

        Window = gw.create_window(Width, Height, "Test Simu", None, None)
        self.create_window = Window
        gw.make_context_current(Window)
        glViewport(0, 0, Width, Height)
        while not gw.window_should_close(Window):

            glClearColor(1, 1, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT)
            if cursor_pos := gw.get_cursor_pos(Window):

                glBegin(GL_TRIANGLE_FAN)

            gw.swap_buffers(Window)
            gw.poll_events()
            time.sleep(0.05)
        gw.terminate()
        return None
    
    def Circle(self, x, y, radius, color=[1, 0, 0], segments=30):
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(color[0], color[1], color[2])
        glVertex2f(x, y)
        for i in range(segments+1):
            angle = 2.0 * pi * i / segments
            glVertex2f(x+cos(angle)*radius, y+sin(angle)*radius)
        glEnd()
    
WinTest = MainSim(400, 400)

WinTest.create_window

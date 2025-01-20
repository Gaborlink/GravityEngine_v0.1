import pygame as pg
import glfw as gw
from OpenGL.GL import *
import numpy as np
import Manage_physics as manph
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
            gw.swap_buffers(Window)
            gw.poll_events()
        gw.terminate()
        return None
    
WinTest = MainSim(400, 400)

WinTest.create_window
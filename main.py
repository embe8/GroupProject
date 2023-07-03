import time

import pygame
import moderngl as mgl
import sys
from model import *
from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene

class GraphicsEngine:
    def __init__(self, win_size=(1600, 900)):
        # init pygame modules
        pygame.init()
        # window size
        self.WIN_SIZE = win_size
        # set opengl attr
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        # create opengl context
        pygame.display.set_mode(self.WIN_SIZE, flags=pygame.OPENGL | pygame.DOUBLEBUF)
        # mouse settings
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        # detect and use existing opengl context
        self.ctx = mgl.create_context()
        # self.ctx.front_face = 'cw'
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        # create an object to help track time
        self.clock = pygame.time.Clock()
        self.time = 0
        self.delta_time = 0
        # light
        self.light = Light()
        # camera
        self.camera = Camera(self)
        # mesh
        self.mesh = Mesh(self)
        # model added
        self.model = BlueFish(self, pos=(0,0,0), rot=(0,0,0), scale=(1,1,1), vao_name='blue_fish', tex_id='blue_fish')
        # scene
        self.scene = Scene(self, self.camera, self.model)

    def check_events(self, last_time):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.mesh.destroy()
                pygame.quit()
                sys.exit()

        '''now = time.perf_counter()
        tick_amt = now - last_time
        last_time = now'''

        #self.scene.update()

    def render(self, tick_amt):
        # clear framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        # render scene
        # added scene update
        self.scene.render(tick_amt)
        #self.camera.move()

        # swap buffers
        pygame.display.flip()



    def get_time(self):
        self.time = pygame.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            last_time = time.perf_counter()
            self.check_events(last_time)
            self.camera.update()
            now = time.perf_counter()
            tick_amt = now - last_time
            last_time = now
            self.render(tick_amt)
            self.delta_time = self.clock.tick(60)


if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()


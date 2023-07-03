from model import *
import glm
import time

SPEED = 0.00005
class Scene:
    def __init__(self, app, camera, model):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = SkyBox(app)
        self.cam = camera
        self.model = model

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        add(BlueFish(self.app, pos=(0.6, 0, -5), scale=(0.2, 0.2, 0.2)))
        add(BlueFish(self.app, pos=(0.8, 0, -5), scale=(0.2, 0.2, 0.2)))
        add(BlueFish(self.app, pos=(0.5, 0.2, -5.5), scale=(0.2, 0.2, 0.2)))
        add(BlueFish(self.app, pos=(0.55, 0, -4), scale=(0.2, 0.2, 0.2)))
        add(BlueFish(self.app, pos=(0.54, 0.5, -3), scale=(0.2, 0.2, 0.2)))
        add(BlueFish(self.app, pos=(0.6, 0.4, -3.6), scale=(0.2, 0.2, 0.2)))
        add(BlueFish(self.app, pos=(0.5, 0.4, -5), scale=(0.2, 0.2, 0.2)))
        add(BlueFish(self.app, pos=(0.3, 0.5, -2), scale=(0.2, 0.2, 0.2)))
        add(BlueFish(self.app, pos=(0.4, 0.5, -3), scale=(0.2, 0.2, 0.2)))
        add(AngelFish(self.app, pos=(2.5, 2, -5), scale=(0.2, 0.2, 0.2)))
        add(AngelFish(self.app, pos=(2.8, 2, -5.5), scale=(0.2, 0.2, 0.2)))
        add(AngelFish(self.app, pos=(2.8, 2.35, -4), scale=(0.2, 0.2, 0.2)))
        add(AngelFish(self.app, pos=(2.9, 2.3, -4), scale=(0.2, 0.2, 0.2)))
        add(AngelFish(self.app, pos=(2.7, 2.2, -4), scale=(0.2, 0.2, 0.2)))
        add(AngelFish(self.app, pos=(2.7, 2.5, -5), scale=(0.2, 0.2, 0.2)))
        add(AngelFish(self.app, pos=(2.7, 2.8, -5), scale=(0.2, 0.2, 0.2)))
        add(AngelFish(self.app, pos=(2.9, 2.38, -4.1), scale=(0.2, 0.2, 0.2)))
        add(MoorFish(self.app, pos=(-2, 1, -1), scale=(0.2, 0.2, 0.2)))
        add(MoorFish(self.app, pos=(-2.2, 1.2, -1), scale=(0.2, 0.2, 0.2)))
        add(MoorFish(self.app, pos=(-2.3, 1.2, -1), scale=(0.2, 0.2, 0.2)))
        add(MoorFish(self.app, pos=(-2.2, 1.3, -1), scale=(0.2, 0.2, 0.2)))

    def render(self, time_amt):
        velocity = SPEED * self.app.delta_time
        for obj in self.objects:
            self.cam.position += self.cam.forward * velocity
            obj.render()
        self.skybox.render()
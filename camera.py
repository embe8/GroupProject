import glm
import pygame
import math

FOV = 50  # deg
NEAR = 0.1
FAR = 100
SPEED = 0.0005
SENSITIVITY = 0.04


class Camera:
    def __init__(self, app, position=(0, 0, 4), yaw=-90, pitch=0):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.yaw = yaw
        self.pitch = pitch
        # view matrix
        self.m_view = self.get_view_matrix()
        # projection matrix
        self.m_proj = self.get_projection_matrix()

    def rotate(self):
        '''rel_x, rel_y = pygame.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY
        self.pitch = max(-89, min(89, self.pitch))'''
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.yaw += -0.5
        if keys[pygame.K_d]:
            self.yaw += 0.5
        if keys[pygame.K_s]:
            self.pitch += -0.5
        if keys[pygame.K_w]:
            self.pitch += 0.5


    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self):
        self.move()
        self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()

    def move(self):

        velocity = SPEED * self.app.delta_time
        keys = pygame.key.get_pressed()
        #if bool == True:
        # if keys[pygame.K_w]:
            #  self.position += self.forward * velocity
            # if keys[pygame.K_s]:
            #self.position -= self.forward * velocity
        # if keys[pygame.K_a]:
            #self.position -= self.right * velocity
        # if keys[pygame.K_d]:
        '''side_to_side = 0.5
            self.position += self.right * velocity
            self.forward.x += math.cos(self.app.time*2) * side_to_side'''
        # if keys[pygame.K_q]:
            #self.position += self.up * velocity
        # if keys[pygame.K_e]:
            #self.position -= self.up * velocity
        # blue fish coming towards screen

        '''side_to_side = 0.3
        self.forward.x += math.cos(self.app.time*2) * side_to_side
        self.position += self.forward * velocity

        pivot = 0.1
        pivot_angle = math.cos(self.app.time) * 0.1 * pivot
        rotation_matrix = glm.mat2(glm.vec2(math.cos(pivot_angle), -math.sin(pivot_angle)),
                                                glm.vec2(math.sin(pivot_angle), -math.cos(pivot_angle)))'''

        '''self.forward.xz = rotation_matrix * self.forward.xz
        body = (self.forward.z + 1.0) / 2.0
        wave = 0.5
        self.forward.x += math.cos(self.app.time + body) * wave'''

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)
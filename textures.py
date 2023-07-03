import pygame
import moderngl as mgl


class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {}
        self.textures['skybox'] = self.get_texture_cube(dir_path='textures/', ext='jpg')
        self.textures['rainbow_fish'] = self.get_texture(path='models/fish/12999_Boesemani_Rainbow_diff.jpg')
        self.textures['moor_fish'] = self.get_texture(path='models/fish/12990_Black_Moor_Goldfish_diff.jpg')
        self.textures['angel_fish'] = self.get_texture(path='models/fish/13009_Coral_Beauty_Angelfish_v1_diff.jpg')
        self.textures['chromis_fish'] = self.get_texture(path='models/fish/13004_Bicolor_Blenny_v1_diff.jpg')
        self.textures['blue_fish'] = self.get_texture(path='models/fish/13006_Blue_Tang_v1_diff.jpg')
        self.textures['fish_school'] = self.get_texture(path='textures/material_0_diffuse.png')
        self.textures['coral_form1'] = self.get_texture(path='textures/GEN_EXT_CoralFormation_Small_Diffuse.png')
        self.textures['yellow_coral'] = self.get_texture(path='textures/internal_ground_ao_texture.jpeg')








    def get_texture_cube(self, dir_path, ext='jpg'):
        faces = ['right', 'left', 'top', 'bottom'] + ['front', 'back'][::-1]
        # textures = [pg.image.load(dir_path + f'{face}.{ext}').convert() for face in faces]
        textures = []
        for face in faces:
            texture = pygame.image.load(dir_path + f'{face}.{ext}').convert()
            if face in ['right', 'left', 'front', 'back']:
                texture = pygame.transform.flip(texture, flip_x=True, flip_y=False)
            elif face in ['top']:
                texture = pygame.transform.flip(texture, flip_x=False, flip_y=True)
                texture = pygame.transform.rotate(texture, 90)
            else:
                texture = pygame.transform.flip(texture, flip_x=True, flip_y=False)
                texture = pygame.transform.rotate(texture, 90)
            textures.append(texture)

        size = textures[0].get_size()
        texture_cube = self.ctx.texture_cube(size=size, components=3, data=None)

        for i in range(6):
            texture_data = pygame.image.tostring(textures[i], 'RGB')
            texture_cube.write(face=i, data=texture_data)

        return texture_cube

    def get_texture(self, path):
        texture = pygame.image.load(path).convert()
        texture = pygame.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pygame.image.tostring(texture, 'RGB'))
        # mipmaps
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        # AF
        texture.anisotropy = 32.0
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]
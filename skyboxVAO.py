from skyboxVBO import VBO
from shader_program import ShaderProgram


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # skybox vao
        self.vaos['skybox'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo=self.vbo.vbos['skybox'])
        # fish vao
        self.vaos['rainbow_fish'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['rainbow_fish'])

        self.vaos['chromis_fish'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['chromis_fish'])

        self.vaos['angel_fish'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['angel_fish'])

        self.vaos['blue_fish'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['angel_fish'])

        self.vaos['moor_fish'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['angel_fish'])

        self.vaos['fish_school'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['fish_school'])

        self.vaos['coral_form1'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['coral_form1'])

        self.vaos['yellow_coral'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['yellow_coral'])

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
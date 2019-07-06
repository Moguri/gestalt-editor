import panda3d.core as p3d

FP_VERT = """
#version 120

uniform mat4 p3d_ModelViewProjectionMatrix;

attribute vec4 p3d_Vertex;

varying vec2 vertpos;

void main() {
    gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
    vertpos = p3d_Vertex.xy;
}
"""

FP_FRAG = """
#version 120

uniform vec4 grid_color;

varying vec2 vertpos;

void main() {
    float x = abs(mod(vertpos.x, 1.0) - 0.5);
    float y = abs(mod(vertpos.y, 1.0) - 0.5);
    float alphafac = smoothstep(0.46, 0.5, max(x, y));
    float colfac = smoothstep(0.47, 0.49, max(x, y));
    gl_FragColor = vec4(grid_color.rgb * colfac, grid_color.a * alphafac);
}
"""


class FloorPlane:
    def __init__(self, *, scale=10, grid_color=None):
        self.scale = scale

        if grid_color is None:
            grid_color = p3d.LColor(1, 1, 1, 0.8)

        # Create a plane
        cardmaker = p3d.CardMaker('Floor Plane')
        geom = cardmaker.generate()
        geomnp = p3d.NodePath(geom)

        # Transform the plane
        geomnp.set_scale(scale)
        geomnp.set_p(-90)
        half_scale = scale / 2
        geomnp.set_x(-half_scale)
        geomnp.set_y(-half_scale)

        # Push transforms to the geometry
        geomnp.flatten_strong()

        # Add a shader to draw grid lines
        geomnp.set_transparency(p3d.TransparencyAttrib.M_alpha)
        shader = p3d.Shader.make(p3d.Shader.SL_GLSL, FP_VERT, FP_FRAG)
        geomnp.set_shader(shader)
        geomnp.set_shader_input('grid_color', grid_color)

        self.nodepath = geomnp

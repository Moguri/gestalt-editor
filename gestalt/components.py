import panda3d.core as p3d
from direct.showbase.DirectObject import DirectObject

import gestalt.floorplane


class EditorComponent(DirectObject):
    '''Base class for editor components'''
    def __del__(self):
        self.ignore_all()

    def setup(self, _showbase):
        pass


class ViewportComponent(EditorComponent):
    '''Handle rendering the scene and navigation'''

    def __init__(self):
        super().__init__()

        self.floorplane = gestalt.floorplane.FloorPlane(scale=1_000)
        self.camera = None
        self.viewport_widgets = p3d.NodePath('Viewport Widgets')

    def setup(self, showbase):
        self.camera = showbase.cam
        self.camera.set_pos(10, -10, 10)
        self.camera.look_at(0, 0, 0)
        self.floorplane.nodepath.reparent_to(self.viewport_widgets)
        self.viewport_widgets.reparent_to(showbase.render)

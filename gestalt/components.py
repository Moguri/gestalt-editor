import sys

import panda3d.core as p3d
from direct.showbase.DirectObject import DirectObject

import gestalt.assetlibrary
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

        self.assetlib = gestalt.assetlibrary.AssetLibrary()
        self.camera = None

        # Viewport Widgets
        self.viewport_widgets = p3d.NodePath('Viewport Widgets')
        self.floorplane = gestalt.floorplane.FloorPlane(scale=1_000)
        self.floorplane.nodepath.reparent_to(self.viewport_widgets)

        # Scene
        self.scene_root = p3d.NodePath('Scene Root')

    def setup(self, showbase):
        self.viewport_widgets.reparent_to(showbase.render)
        self.scene_root.reparent_to(showbase.render)

        # Add a better starting camera position
        self.camera = showbase.cam
        self.camera.set_pos(10, -10, 10)
        self.camera.look_at(0, 0, 0)

        # Try to load a model
        if len(sys.argv) > 1:
            modelpath = sys.argv[1]
            self.assetlib.import_file(modelpath)
            model_root = self.assetlib.libraries[0]
            self.scene_root.attach_new_node(model_root)

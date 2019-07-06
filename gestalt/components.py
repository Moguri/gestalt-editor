import panda3d.core as p3d
from direct.showbase.DirectObject import DirectObject

import gestalt.floorplane


class EditorComponent(DirectObject):
    '''Base class for editor components'''
    def __del__(self):
        self.ignore_all()

    def setup(self, _showbase):
        pass

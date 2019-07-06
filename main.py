import sys

from direct.showbase.ShowBase import ShowBase
import panda3d
import pman.shim

import gestalt.floorplane


panda3d.core.load_prc_file(
    panda3d.core.Filename.expand_from('$MAIN_DIR/settings.prc')
)


class EditorApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        pman.shim.init(self)
        self.accept('escape', sys.exit)

        self.cam.set_pos(10, -10, 10)
        self.cam.look_at(0, 0, 0)

        # Attach all editor widgets to this NodePath to get them separate
        # from the scene rendering.
        self.render_editor = self.render.attach_new_node('Editor Widgets')
        self.render_editor.reparent_to(self.render)

        floorplane = gestalt.floorplane.FloorPlane(scale=1_000)
        floorplane.nodepath.reparent_to(self.render_editor)


def main():
    app = EditorApp()
    app.run()

if __name__ == '__main__':
    main()

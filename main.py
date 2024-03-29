import sys

from direct.showbase.ShowBase import ShowBase
import panda3d
import pman.shim

from gestalt import components


panda3d.core.load_prc_file(
    panda3d.core.Filename.expand_from('$MAIN_DIR/settings.prc')
)


class EditorApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        pman.shim.init(self)
        self.accept('escape', sys.exit)

        # Load components
        self.components = [
            components.ViewportComponent(),
        ]
        for comp in self.components:
            comp.setup(self)


def main():
    app = EditorApp()
    app.run()

if __name__ == '__main__':
    main()

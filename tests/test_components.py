#pylint:disable=redefined-outer-name
import inspect

import panda3d.core as p3d
from direct.showbase.ShowBase import ShowBase


import pytest


from gestalt import components


@pytest.fixture(scope='session')
def showbase():
    p3d.load_prc_file_data('', 'window-type none')
    base = ShowBase()
    base.cam = p3d.NodePath('camera')
    return base


EDITOR_COMPONENTS = [
    memb[1]()
    for memb in inspect.getmembers(components, inspect.isclass)
    if issubclass(memb[1], components.EditorComponent)
]


@pytest.mark.parametrize('component', EDITOR_COMPONENTS)
def test_component_setup(component, showbase):
    component.setup(showbase)

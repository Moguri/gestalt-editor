#pylint:disable=redefined-outer-name
import inspect

from direct.showbase.ShowBase import ShowBase


import pytest


from gestalt import components


@pytest.fixture(scope='session')
def showbase():
    return ShowBase()


EDITOR_COMPONENTS = [
    memb[1]()
    for memb in inspect.getmembers(components, inspect.isclass)
    if issubclass(memb[1], components.EditorComponent)
]


@pytest.mark.parametrize('component', EDITOR_COMPONENTS)
def test_component_setup(component, showbase):
    component.setup(showbase)

#pylint:disable=redefined-outer-name
import inspect
import unittest.mock


import pytest


from gestalt import components


@pytest.fixture
def showbase():
    return unittest.mock.MagicMock()


EDITOR_COMPONENTS = [
    memb[1]()
    for memb in inspect.getmembers(components, inspect.isclass)
    if issubclass(memb[1], components.EditorComponent)
]


@pytest.mark.parametrize('component', EDITOR_COMPONENTS)
def test_component_setup(component, showbase):
    component.setup(showbase)

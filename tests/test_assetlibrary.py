#pylint:disable=redefined-outer-name
import os


import pytest


from gestalt.assetlibrary import AssetLibrary


@pytest.fixture
def assetlib():
    return AssetLibrary()


@pytest.fixture
def assetfile():
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname, 'box.egg')


def test_assetlib_import(assetlib, assetfile):
    numlibs = len(assetlib.libraries)
    assetlib.import_file(assetfile)
    assert len(assetlib.libraries) == numlibs + 1

def test_assetlib_import_fail(assetlib, assetfile):
    assetfile += '.foo'
    with pytest.raises(Exception):
        assetlib.import_file(assetfile)

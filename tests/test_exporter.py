#pylint:disable=redefined-outer-name
import os

import panda3d.core as p3d

import pytest


from gestalt.sceneexporter import SceneExporter


@pytest.fixture
def sceneexporter():
    return SceneExporter()


@pytest.fixture
def exportfile(tmpdir):
    return os.path.join(tmpdir, 'scene.bam')


@pytest.fixture
def sceneroot():
    return p3d.NodePath('scene_root')


def test_exporter_export(sceneexporter, sceneroot, exportfile):
    sceneexporter.export(sceneroot, exportfile)
    assert os.path.exists(exportfile)


def test_exporter_export_fail(sceneexporter, sceneroot, exportfile):
    exportfile += '.foo'
    with pytest.raises(Exception):
        sceneexporter.export(sceneroot, exportfile)

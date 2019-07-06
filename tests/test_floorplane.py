#pylint:disable=redefined-outer-name
import panda3d.core as p3d

import pytest


from gestalt.floorplane import FloorPlane

@pytest.fixture
def floorplane():
    return FloorPlane()


def test_floorplane_transform(floorplane):
    fpnp = floorplane.nodepath
    assert fpnp.get_pos() == (0, 0, 0)
    assert fpnp.get_hpr() == (0, 0, 0)


def test_floorplane_bounds(floorplane):
    fpnp = floorplane.nodepath
    bounds_min, bounds_max = fpnp.get_tight_bounds()
    bounds = bounds_max - bounds_min
    assert bounds.x == pytest.approx(floorplane.scale)
    assert bounds.y == pytest.approx(floorplane.scale)
    assert bounds.z == pytest.approx(0, abs=1e-6)


def test_floorplane_attach(floorplane):
    fpnp = floorplane.nodepath
    root = p3d.NodePath('root')
    fpnp.reparent_to(root)

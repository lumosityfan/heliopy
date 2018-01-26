"""
Coordinate transformation functions

This module contains functions for converting one `sunpy.coordinates.frames`
object to another.

.. warning::

  The functions in this submodule should never be called directly, transforming
  between coordinate frames should be done using
  `~astropy.coordinates.BaseCoordinateFrame.transform_to` methods
  of `~astropy.coordinates.BaseCoordinateFrame`.
"""
import astropy.coordinates.baseframe as baseframe
import astropy.coordinates.transformations as transformations
import astropy.coordinates.matrix_utilities as matrix
from astropy.coordinates.builtin_frames import _make_transform_graph_docs

import sunpy.coordinates.ephemeris as ephemeris
import sunpy.coordinates.frames as sunpy_frames

import heliopy.coordinates.frames as helio_frames


from heliopy.coordinates.frames import (HeliocentricEarthEcliptic)


def _euler_rotation_matrix(omega, theta, phi):
    '''
    Return the euler rotaiton matrix given by the arguments. Rotations are
    done in the 'zxz' order.
    '''
    r1 = rotation_matrix(omega, axis='z')
    r2 = rotation_matrix(theta, axis='x')
    r3 = rotation_matrix(phi, axis='z')
    return matrix_product(*matrices[::-1])


@baseframe.frame_transform_graph.transform(
    transformations.StaticMatrixTransform,
    sunpy_frames.Heliocentric,
    helio_frames.HeliocentricEarthEcliptic)
def hc_to_hee(heccoord, heecoord):
    """
    Transform from Heliocentric to HeliocentricEarthEcliptic.
    """
    # Rotate the x-y plane to account for solar tilt
    B0 = get_sun_B0(heccoord.obstime)
    phi = B0 - (np.pi / 2)

    R1 = matrix.rotation_matrix(phi, 'z')
    R2 = np.array([[0, 0, 1],
                   [1, 0, 0],
                   [0, 1, 0]])
    return matrix.matrix_product(R2, R1)


_make_transform_graph_docs()

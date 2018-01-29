"""
Coordinate transformation functions

This module contains functions for converting one
:mod:`heliopy.coordinates.frames` object to another.

.. warning::

  The functions in this submodule should never be called directly, transforming
  between coordinate frames should be done using
  :meth:`~astropy.coordinates.BaseCoordinateFrame.transform_to` on coordinate
  frame objects.
"""
import astropy.coordinates.baseframe as baseframe
import astropy.coordinates.transformations as transformations
import astropy.coordinates.builtin_frames as astropy_frames
import numpy as np

import heliopy.coordinates.frames as helio_frames


@baseframe.frame_transform_graph.transform(
    transformations.StaticMatrixTransform,
    helio_frames.HeliocentricEarthEcliptic,
    helio_frames.GeocentricSolarEcliptic)
def hee_to_gse():
    '''
    Convert from HEE to GSE coordinates.
    '''
    return np.array([[-1, 0, 0],
                     [0, -1, 0],
                     [0, 0, 1]])


__doc__ += astropy_frames._make_transform_graph_docs()

"""
Common space physics coordinate systems.

This submodule contains various space physics coordinate frames for use with
the `astropy.coordinates` module.
"""
import astropy.coordinates.baseframe as baseframe
import astropy.coordinates.representation as r
import astropy.coordinates as coords


class HeliocentricEarthEcliptic(baseframe.BaseCoordinateFrame):
    """
    A coordinate frame in the Heliocentric Earth Ecliptic (HEE) system.

    The x-y plane is the Earth mean ecliptic, the x-axis points from the
    Sun to the Earth, and the z-axis points North out of the ecliptic plane.
    """
    name = 'heliocentric_earth_ecliptic'
    default_representation = coords.CartesianRepresentation
    obstime = coords.TimeAttribute(default=None)

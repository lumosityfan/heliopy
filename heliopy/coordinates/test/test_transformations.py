import heliopy.coordinates.transformations as trans
import heliopy.coordinates.frames as frames
import astropy.coordinates as astro_coords
import astropy.units as u
from datetime import datetime


def test_hee_to_gse():
    hee = frames.HeliocentricEarthEcliptic(x=1*u.km, y=1*u.km, z=1*u.km)
    gse = hee.transform_to(frames.GeocentricSolarEcliptic)
    assert gse.z == hee.z
    assert gse.y == -hee.y
    assert gse.x == -hee.x

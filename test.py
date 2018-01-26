import sunpy.coordinates.frames as sunpy_frames
import astropy.units as u
import astropy.constants as const

import heliopy.coordinates.frames as helio_frames

frame = sunpy_frames.Heliocentric(x=0 * u.m, y=0 * u.m, z=const.au, obstime='now')
import pdb; pdb.set_trace()
trans = frame.transform_to(helio_frames.HeliocentricEarthEcliptic)

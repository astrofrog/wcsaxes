from astropy.wcs import WCS
from astropy.wcs.utils import skycoord_to_pixel, proj_plane_pixel_scales


def linear_offset_coords(wcs, center):
    """
    Returns a locally linear offset coordinate system.
    
    Given a 2-d celestial WCS object and a central coordinate, return a WCS
    that describes an 'offset' coordinate system, assuming that the
    coordinates are locally linear (that is, the grid lines of this offset
    coordinate system are always aligned with the pixel coordinates, and
    distortions from spherical projections and distortion terms are not taken
    into account)
    
    Parameters
    ----------
    wcs : `~astropy.wcs.WCS`
        The original WCS, which should be a 2-d celestial WCS
    center : `~astropy.coordinates.SkyCoord`
        The coordinates on which the offset coordinate system should be
        centered.
    """

    # Convert center to pixel coordinates
    xp, yp = skycoord_to_pixel(center, wcs)
        
    # Set up new WCS
    new_wcs = WCS(naxis=2)
    new_wcs.wcs.crpix = xp + 1, yp + 1
    new_wcs.wcs.crval = 0., 0.
    new_wcs.wcs.cdelt = proj_plane_pixel_scales(wcs)
    new_wcs.wcs.ctype = 'XOFFSET', 'YOFFSET'
    new_wcs.wcs.cunit = 'deg', 'deg'

    return new_wcs
import numpy as np
import scipy
import scipy.ndimage
from scipy.interpolate import griddata
import matplotlib.gridspec as gridspec


def get_contours(ra, dec, data, sigma = [0.01, 0.01]):

    """Function to get contours of hexagrid spaced data
    ra:    from PyStructure ["ra_deg"]
    dec:   from PyStructure
    data:  ints/ucs
    sigma: Standard deviation for Gaussian kernel.
    """

    # regular grid of interpolation points
    x, y = np.linspace(ra.min(), ra.max(), 100), np.linspace(dec.min(), dec.max(), 100)
    x, y = np.meshgrid(x, y)

    # Interpolate
    # there is also method='cubic' for 2-D data
    z = scipy.interpolate.griddata((ra, dec), data, (x, y), method='linear')

    z = scipy.ndimage.filters.gaussian_filter(z, sigma, mode='nearest')
    z[np.where(z==0)] = np.nan #set zeros to nan

    return(x, y, z)

import numpy as np
from astropy.io import fits

def convert(file):
    '''
    Function which converts Jy/beam to Kelvin
    ----
    Parameters:
    file: str
    file name without '.fits'
    '''
    path = '/Users/cosimaeibensteiner/Desktop/home/PhD/Project/NGC6946/3-PdBI-data/data/raw_data/'
    filename = file +'.fits'

    line_data, line_header = fits.getdata(path + filename, header = True)

    #according to https://science.nrao.edu/facilities/vla/proposing/TBconv
    line_K_header = line_header
    line_K_header['BMAJ'] = line_header['BMAJ'] * 60 * 60               #  Converting degrees into arcseconds
    line_K_header['BMIN'] = line_header['BMIN'] * 60 * 60

    #[(Jy/beam)*1000 / (GHz^2 * arcsec * arcsec)]
    line_K_data = 1.222 * 10**3 * (line_data * 1000)/(115.271**2 * line_K_header['BMAJ'] * line_K_header['BMIN'])


    line_K_header['BUNIT'] = 'K'


    fits.writeto(path + file + '-K.fits', line_K_data, line_K_header)	#it will save instead of the original cubes

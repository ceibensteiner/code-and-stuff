from astropy.coordinates import SkyCoord, FK5
import astropy.units as au
import numpy as np

file = "ngc6946_data_struct_2020_08_14.npy"
struc = np.load("/Users/cosimaeibensteiner/Desktop/home/PhD/Project/NGC6946/3-PdBI-data/database/"+str(file), allow_pickle = True).item()

ra = struc["ra_deg"]
dec = struc["dec_deg"]

# create array with dec and ra assignt to points
points = []
for i in range(len(ra)):
    points.append([ra[i], dec[i]])
points = np.array(points)


# create coordinate frame showing delta-ra and delta-dec
coords_ref = ["20:34:52.32 60:09:14.09"]
skycoords_ref = SkyCoord(coords_ref, frame=FK5, unit=(au.hourangle, au.deg))
coords_map = (ra, dec) *au.deg
skycoords_map = SkyCoord(ra=coords_map[0], dec=coords_map[1], frame=FK5)
aframe = skycoords_ref.skyoffset_frame()
delta_ra = skycoords_map.transform_to(aframe).lon.arcsec
delta_dec = skycoords_map.transform_to(aframe).lat.arcsec

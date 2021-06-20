"""commonly used functions"""
from astropy.io import fits
import numpy as np
import os.path as op 

def load_image(fname, verbose=True):
    img = fits.getdata(fname, ext=0)
    img = np.moveaxis(img, [0], [2])
    if verbose: print(f"{op.basename(fname)}:\t{img.shape}")
    return img
"""commonly used functions"""
from astropy.io import fits
import numpy as np
import os.path as op 

def load_image(fname, verbose=True):
    img = fits.getdata(fname, ext=0)
    img = np.moveaxis(img, [0], [2])
    if verbose: print(f"{op.basename(fname)}:\t{img.shape}")
    return img

def preprocess_image(img, steps, verbose=True):
    for step, opts in steps.items():
        if verbose: print(f"step: {step}")
        if step == 'highpass':  # simple highpass
            fc   = opts.get('fc', 1.0)
            fimg = np.fft.rfft2(img, axes=(0,1))
            fx   = np.fft.rfftfreq(img.shape[0])
            fy   = np.fft.rfftfreq(img.shape[1])
            # print(fx[:2],fy[:2])
            fimg[np.ix_(fx<fc,fy<fc)] = 0
            img  = np.fft.irfft2(fimg, axes=(0,1)).real
        elif step == 'highpass2': # slightly more advanced highpass
            fc   = opts.get('fc', 1.0)
            thre = opts.get('thres', 0.8)
            # mask sources brighter than a given threshold
            mask = np.sum(img > thre,axis=-1) > 0
            img2 = img.copy()
            img2[mask,:] = 0
            fimg = np.fft.rfft2(img2, axes=(0,1))
            fx   = np.fft.rfftfreq(img2.shape[0])
            fy   = np.fft.rfftfreq(img2.shape[1])
            # print(fx[:2],fy[:2])
            fimg[np.ix_(fx>fc,fy>fc)] = 0
            bg   = np.fft.irfft2(fimg, axes=(0,1)).real
            img -= bg
        elif step == 'arcsinh':
            # a arcsinh (b x)
            a    = opts.get('a', 1)
            b    = opts.get('b', 1)
            img  = a*np.arcsinh(b*img)
    return img
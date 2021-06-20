"""This script aims to stack all fit images"""

import argparse, os, os.path as op
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

from common import *

parser = argparse.ArgumentParser()
parser.add_argument("--ifiles", nargs='+')
parser.add_argument("--odir", help='output directory', default='out')
parser.add_argument("--bias", help='bias file to use')
parser.add_argument("--flat", help='flat file to use')
parser.add_argument("--fits", help='if want to save a fits file', action='store_true')
args = parser.parse_args()
if not op.exists(args.odir): os.makedirs(args.odir)
    
# load calibration files
bias = np.load(args.bias)
flat = np.load(args.flat)

stacked = bias*0

for f in tqdm(args.ifiles):
    img  = load_image(f, verbose=False).astype(float)
    img -= bias
    img /= flat
    img /= 255
    stacked += img
stacked /= len(args.ifiles)

ofile = op.join(args.odir,"simple_stack.npy")
print("Writing:", ofile)
np.save(ofile, stacked)

if args.fits:
    hdul = fits.HDUList()
    hdul.append(fits.PrimaryHDU())
    hdul.append(fits.ImageHDU(data=img))
    hdul.writeto(ofile.replace('.npy','.fits'))
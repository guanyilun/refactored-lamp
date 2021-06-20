"""This script prepares calibration files"""

import argparse, os, os.path as op
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

from common import *

parser = argparse.ArgumentParser()
parser.add_argument("--odir", help='output directory', default='out')
parser.add_argument("--bias", help='bias file to use', nargs='+')
parser.add_argument("--flat", help='flat file to use', nargs='+')
args = parser.parse_args()
if not op.exists(args.odir): os.makedirs(args.odir)
    
# load calibration files
bias  = np.array([load_image(f) for f in args.bias], dtype=float)
flat  = np.array([load_image(f) for f in args.flat], dtype=float)
xdim, ydim = flat.shape[1:3]
mbias = np.median(bias, axis=0)
xsel  = slice(int(0.2*xdim),int(0.8*xdim))
ysel  = slice(int(0.2*ydim),int(0.8*ydim))
flat -= mbias[None,...]
flat /= np.mean(flat[:,xsel,ysel,:], axis=(1,2))[:,None,None,:]
mflat = np.mean(flat, axis=0)

# save output
np.save(op.join(args.odir, 'mbias.npy'), mbias)
np.save(op.join(args.odir, 'mflat.npy'), mflat)
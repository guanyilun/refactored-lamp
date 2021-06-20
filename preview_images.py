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
args = parser.parse_args()
if not op.exists(args.odir): os.makedirs(args.odir)
    
# load calibration files
bias = np.load(args.bias)
flat = np.load(args.flat)

for f in tqdm(args.ifiles):
    img  = load_image(f).astype(float)/255
    img -= bias
    img /= flat
    
    plt.figure(figsize=(10,5))
    plt.imshow(img, origin='lower')
    plt.axis('off')
    ofile = op.join(args.odir, op.basename(f).replace('.fit','.pdf'))
    print("Writing:", ofile)
    plt.savefig(ofile,bbox_inches='tight')
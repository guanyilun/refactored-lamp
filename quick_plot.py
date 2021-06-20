""""""

import argparse, os, os.path as op
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

from common import *

parser = argparse.ArgumentParser()
parser.add_argument("ifile")
parser.add_argument("--odir", help='output directory', default='out')
parser.add_argument("--oname", help='output filename', default=None)
args = parser.parse_args()
if not op.exists(args.odir): os.makedirs(args.odir)
    
img = np.load(args.ifile)

# preprocess happening here
# made a mistake in stacking by adding 1/421 to the image
# need to correct it here <-- makes no difference though
# img -= 1/421

plt.figure(figsize=(10,5))
plt.imshow(img, origin='lower')
plt.axis('off')

# write out image
if args.oname: oname = op.join(args.odir, args.oname)
else: oname = op.join(args.odir, op.basename(args.ifile)[:-4]+'.pdf')
print("Writing:", oname)
plt.savefig(oname, bbox_inches='tight')


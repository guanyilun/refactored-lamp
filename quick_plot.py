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
img = preprocess_image(img, steps={
    'highpass': {'fc': 0.1},
    # 'highpass2': {'fc': 0.0003, 'thres': 0.8},
    # 'arcsinh'  : {'a': 1, 'b': 1}
})

plt.figure(figsize=(10,5))
plt.imshow(img, origin='lower')
plt.axis('off')

# write out image
if args.oname: oname = op.join(args.odir, args.oname)
else: oname = op.join(args.odir, op.basename(args.ifile)[:-4]+'.pdf')
print("Writing:", oname)
plt.savefig(oname, bbox_inches='tight')


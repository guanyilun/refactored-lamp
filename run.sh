data=/bgfs/akosowsky/yig20/shared/Cane_Guan
out=out

# prepare master calibration files including both
# flat and bias
# python prepare_calib.py \
#     --flat $data/Calibration*F.fit \
#     --bias $data/Calibration*B.fit \
#     --odir $out

# preview images one by one, after taking the precomputed
# calibration files

# python preview_images.py \
#     --ifiles $data/North_Amreican_Nebula-0001L.fit \
#     --bias   $out/mbias.npy \
#     --flat   $out/mflat.npy \
#     --odir   out
 
python simple_stack.py \
    --ifiles $data/North_Amreican_Nebula-*L.fit \
    --bias   $out/mbias.npy \
    --flat   $out/mflat.npy \
    --odir   out
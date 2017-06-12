import os
import re
from glob import glob

from PIL import Image

FILES_TO_CROP = [
    ('atmos.precip_plot.time_index*png', (10, 150, 800, 500)),
]


def crop(filename, rect):
    if re.search('_cropped', filename):
        print('Already cropped {}'.format(filename))
        return
    print('Cropping {}'.format(filename))
    out_filename = '{}_cropped{}'.format(*os.path.splitext(filename))
    im = Image.open(filename)
    print('Orig size: {}'.format(im.getbbox()))
    cropped_im = im.crop(rect)
    print('Crop size: {}'.format(cropped_im.getbbox()))
    cropped_im.save(out_filename)

def main():
    for filename_glob, rect in FILES_TO_CROP:
        for filename in sorted(glob(filename_glob)):
            crop(filename, rect)


if __name__ == '__main__':
    main()

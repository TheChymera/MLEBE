import os
import nibabel as nib
from matplotlib import pyplot as plt
import numpy as np
from skimage import transform as tf

from utils import *

not_preprocessed_dir = '/usr/share/'
image_dir = '/Users/Hendrik/Documents/mlebe_data/preprocessed'
image_dir_remote = '/mnt/scratch/'


def load_bidsdata():
    """

    :return: list of paths of all the bids files
    """
    paths = []
    filess = []
    for o in os.listdir(not_preprocessed_dir):
        if not o.startswith('irsabi') and o.endswith('bidsdata'):
            for root, dirs, files in os.walk(os.path.join(not_preprocessed_dir, o)):
                for file in files:
                    if file.endswith("_T2w.nii.gz"):
                        print(os.path.join(not_preprocessed_dir, o, root, file))
                        paths.append(os.path.join(not_preprocessed_dir, o, root, file))
                        filess.append(file)
    return paths, filess





def load_img_remote(shape):
    visualisation = False

    im_data = []
    for o in os.listdir(image_dir_remote):
        if o != 'irsabi':
            for x in os.listdir(os.path.join(image_dir_remote, o)):
                if x.endswith('preprocessing'):
                    for root, dirs, files in os.walk(os.path.join(image_dir_remote, o, x)):
                        for file in files:
                            if file.endswith("_T2w.nii.gz"):
                                im_data.append(os.path.join(root, file))



    im_data = np.sort(im_data)
    data = []
    file_names = []
    for i in im_data:
        file_names.append(os.path.basename(i))
        img = nib.load(i)
        img_data = img.get_data()
        temp = np.moveaxis(img_data,2,0)
        img_data = pad_img(temp, shape)
        img_data = data_normalization(img_data)
        path = os.path.join('visualisation', os.path.basename(i), 'padded_data')
        if visualisation == True:
            save_img(img_data, path)
            visualisation = False

        data.append(img_data)
    return data, file_names

def load_img(shape, visualisation ):

    im_data = []
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("TurboRARE_T2w.nii.gz"):
                im_data.append(os.path.join(root, file))

    im_data = np.sort(im_data)
    data = []
    file_names = []
    for i in im_data:
        file_names.append(os.path.basename(i))
        img = nib.load(i)
        img_data = img.get_data()   #shape = (63, 96, 48)
        temp = np.moveaxis(img_data,2,0)    #shape = (48, 63, 96)
        img_data = pad_img(temp, shape)
        img_data = data_normalization(img_data)
        path = os.path.join('visualisation', os.path.basename(i), 'padded_data')
        if visualisation == True:
            save_img(img_data, path)
            visualisation = False

        data.append(img_data)
    return data, file_names


def load_mask(data_dir, shape, visualisation):

    mask = []
    im_data = []
    for o in os.listdir(data_dir):
        if o == 'dsurqec_200micron_mask.nii':
            im_data.append(os.path.join(data_dir,o))

    data = []
    im_data = np.sort(im_data)
    print(im_data)
    for i in im_data:
        img = nib.load(i)
        img_data = img.get_data()
        temp = np.moveaxis(img_data,2,0)
        img_data = pad_img(temp, shape)
        img_data = data_normalization(img_data)
        path = os.path.join('visualisation', os.path.basename(i), 'padded_data')
        if visualisation == True:
            save_img(img_data, path)
            visualisation = False

        data.append(img_data)


    return data





if __name__ == '__main__':      #only gets called if Unet.py is run
    load_bidsdata()
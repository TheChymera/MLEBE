import os
import imageio
import numpy as np
from matplotlib import pyplot as plt



def save_img(img_data, path):
    if not os.path.exists(path):
        os.makedirs(path)
    for j in range(img_data.shape[2]):
        imageio.imwrite(os.path.join(path, 'img_{}.png'.format(j)), img_data[..., j])



def save_datavisualisation3(img_data, myocar_labels, predicted_labels, save_folder, index_first = False, normalized = False):
    img_data_temp = []
    myocar_labels_temp = []
    predicted_labels_temp = []
    if index_first == True:
        for i in range(0, len(img_data)):
            img_data_temp.append(np.moveaxis(img_data[i], 0, -1))
            myocar_labels_temp.append(np.moveaxis(myocar_labels[i], 0, -1))
            predicted_labels_temp.append(np.moveaxis(predicted_labels[i], 0, -1))
    counter = 0
    for i, j, k in zip(img_data_temp[:], myocar_labels_temp[:], predicted_labels_temp[:]):
        print(counter)
        print(i.shape)
        i_patch = i[:, :, 0]
        if normalized == True:
            i_patch = i_patch*255
        # np.squeeze(i_patch)

        j_patch = j[:, :, 0]
        # np.squeeze(j_patch)
        j_patch = j_patch * 255

        k_patch = k[:,:,0]
        k_patch = k_patch*255

        for slice in range(1, i.shape[2]):
            temp = i[:, :, slice]
            # np.squeeze(temp)
            if normalized == True:
                temp = temp * 255
            i_patch = np.hstack((i_patch, temp))


            temp = j[:, :, slice]
            # np.squeeze(temp)
            temp = temp * 255
            j_patch = np.hstack((j_patch, temp))

            temp = k[:,:,slice]
            temp = temp*255
            k_patch = np.hstack((k_patch, temp))

        image = np.vstack((i_patch, j_patch, k_patch))

        print(image.shape)
        imageio.imwrite(save_folder + 'mds' + '%d.png' % (counter,), image)


        counter = counter + 1
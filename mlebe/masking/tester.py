from predict_mask import predict_mask
from mlebe.training import data_loader
import nibabel as nib
import os
"""
With this script one can visualize the performance of the masking functions for a given data set
data_paths: paths to the data that is to be used for testing
"""


data_dir = os.path.expanduser('/usr/share/')
data_paths = data_loader.load_bidsdata(data_dir, studies = ['irsabi_bidsdata'])
data_paths = ['/home/hendrik/.scratch/mlebe/bids/sub-3839/ses-ofM/anat/sub-3839_ses-ofM_acq-TurboRARE_T2w.nii.gz']
save_dir = 'vis/anat/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

visualisation = {
    'bool': True,
    'path': save_dir,
}

for path in data_paths:
    print(path)
    masked_path = predict_mask(path, visualisation_bool = visualisation['bool'], visualisation_path = visualisation['path'], bias_correct_bool = True)[0]
    command = 'mv {a} {b}'.format(a = masked_path, b = os.path.join(save_dir, 'masked_' + os.path.basename(path)))
    print(command)
    os.system(command)



# data_paths = data_loader.load_bidsdata(data_dir, studies = ['irsabi_bidsdata'], input_type = 'func')
# save_dir = 'vis/func/'
# if not os.path.exists(save_dir):
#     os.makedirs(save_dir)
# visualisation = {
#     'bool': True,
#     'path': save_dir,
# }
# for path in data_paths:
#     print(path)
#     masked_path = predict_mask(path, input_type = 'func', visualisation_bool = visualisation['bool'], visualisation_path = visualisation['path'], bias_correct_bool = True)[0]
#     command = 'mv {a} {b}'.format(a = masked_path, b = os.path.join(save_dir, 'masked_' + os.path.basename(path)))
#     print(command)
#     os.system(command)
#
# command = 'rm *.nii.gz'
# os.system(command)
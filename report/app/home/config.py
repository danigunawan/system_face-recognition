# import os 
# from django.conf import settings
# """
#     setting variable
# """
# Start_system = True
# VP_buid = False
# VP_range = 111
# Root = None
# Tree = None
# Range_find = 100000000.0
# K_similarity = 10
# name_upload = 0
# new_Token = None
# static_up_load = 0 
# path_new_numpy = None
# origin_data_npy =os.path.join(settings.BASE_DIR,'home/VGG_feature/')
# origin_HOG_npy = os.path.join(settings.BASE_DIR,'home/HOG_feature/')
# origin_sift_npy = os.path.join(settings.BASE_DIR,'home/Sift_feature/')
# origin_data_img =settings.IMG_ROOT
# origin_facenet_npy = os.path.join(settings.BASE_DIR,'home/facenet_numpy')
# origin_VGG16_npy = os.path.join(settings.BASE_DIR,'home/vgg_feature_npy')
# origin_mix_vgg_facenet_npy = os.path.join(settings.BASE_DIR,'home/mix_vgg_facenet_numpy')
# """
#     MODEL DEEPLEARNING FROM KERAS 
# """
# model_facenet = None
# type_distance = 1


# Root_running_HOG = None
# Root_running_sift = None
# Root_running_facenet = None
# Root_running_vgg16 = None
# Root_running_mix_facenet_vgg16 = None 

# Tree_running_HOG = None
# Tree_running_sift = None
# Tree_running_facenet = None
# Tree_running_vgg16 = None
# Tree_running_mix_facenet_vgg16 = None 


import os 
from django.conf import settings
"""
    setting variable
"""
Start_system = True
VP_buid = False
VP_range = 111
Root = None
Tree = None
Range_find = 100000000.0
K_similarity = 10
name_upload = 0
new_Token = None
static_up_load = 0 
path_new_numpy = None
origin_data_npy =os.path.join(settings.BASE_DIR,'home/VGG_feature/')
origin_HOG_npy = os.path.join(settings.BASE_DIR,'home/HOG_feature/')
origin_sift_npy = os.path.join(settings.BASE_DIR,'home/Sift_feature/')
origin_data_img =settings.IMG_ROOT
origin_facenet_npy = os.path.join(settings.BASE_DIR,'home/facenet_numpy')
origin_VGG16_npy = os.path.join(settings.BASE_DIR,'home/vgg_feature_npy')
origin_mix_vgg_facenet_npy = os.path.join(settings.BASE_DIR,'home/mix_vgg_facenet_numpy')

"""
    MODEL DEEPLEARNING FROM KERAS 
"""
model_facenet = None
type_distance = 1


Root_running_HOG = None
Root_running_sift = None
Root_running_facenet = None
Root_running_vgg16 = None
Root_running_mix_facenet_vgg16 = None 

Tree_running_HOG = None
Tree_running_sift = None
Tree_running_facenet = None
Tree_running_vgg16 = None
Tree_running_mix_facenet_vgg16 = None 

#model SVM, NB, MLP for Voting
#link model: https://drive.google.com/drive/folders/1FVYXoF5TrPb-PF8uhGjwjh7bzGxHdAg7?usp=sharing
svm_model = os.path.join(settings.BASE_DIR,'home/model/svm_face_final_model.sav')
NB_model = os.path.join(settings.BASE_DIR,'home/model/NB_face_model.sav')
mlp_model = os.path.join(settings.BASE_DIR,'home/model/mlp_face_model.sav')
voting_model = os.path.join(settings.BASE_DIR,'home/model/voting_svm_NB_mlp_model.sav')

svm_model_loaded = None
NB_model_loaded = None
mlp_model_loaded = None
voting_model_loaded = None
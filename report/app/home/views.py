from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from . import process_Tree
from . import process_request
from . import reset_system
import os
import numpy as np
from django.conf import settings
from . import config
from . import process_API
import shutil
import cv2
# Create your views here.
from django.http import HttpResponse,StreamingHttpResponse, HttpResponseServerError
from django.views.decorators import gzip

def index(request):

    return render(request, 'pages/home.html')

def evaluation(request):
    f = open("home\\label\\label_of_famous_people.txt", "r")
    t = f.read()
    labels = t.split()
    for i in range(0,len(labels)):
        labels[i] = labels[i].split(":")
    
    

    return render(request, 'pages/evaluation.html')

def upload(request):
    if config.Start_system:
        print("system",config.Start_system)
        reset_system.remove_file()       
    result = {}
    uploaded_file = None
    if request.method == 'POST':
        k_number = request.POST.get("knumber")
        if (k_number is not None and k_number !='' ):
            config.K_similarity = int(k_number)
        choose_method = request.POST.get("choose_method")
        choose_distance = request.POST.get("choose_distance")
        # Format select method: 1 = Hog, 2 = Sift feature, 3 = mix_feature_sift_hog, 4 = VGG16
        uploaded_file = request.FILES['document']
        if uploaded_file:
            fs = FileSystemStorage()
            config.name_upload = config.name_upload+1
            new_name = str(config.name_upload)+ ".png"
            fs.save(new_name, uploaded_file)
            if choose_method=="1":
                process_API.HOG(new_name)
            if choose_method=="2":
                process_API.sift_feature(new_name)
            if choose_method=="3":
                process_API.mix_feature_sift_hog(new_name)
            if choose_method=="4":
                process_API.facenet(new_name)
            if choose_method=="5":
                process_API.resnet(new_name)
            if choose_method=="6":
                process_API.VGG16(new_name)
            if choose_method=="7":
                process_API.mix_facenet_vgg16(new_name)
            process_API.voting_classifer()
            config.type_distance == int(choose_distance)
            result = process_request.process_img(new_name,choose_method)
    return render(request, 'pages/upload.html', result)

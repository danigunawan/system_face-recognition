import base64
import os
import cv2
import shutil
import numpy as np
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import gzip
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseServerError

from . import config
from . import process_API
from . import reset_system
from . import process_Tree
from . import process_request


def index(request):

    return render(request, 'pages/home.html')


def evaluation(request):
    f = open("home\\label\\label_of_famous_people.txt", "r")
    t = f.read()
    labels = t.split()
    for i in range(0, len(labels)):
        labels[i] = labels[i].split(":")

    return render(request, 'pages/evaluation.html')


def upload(request):
    if config.Start_system:
        print("system", config.Start_system)
        reset_system.remove_file()
    result = {}
    uploaded_file = None
    if request.method == 'POST':
        k_number = request.POST.get("knumber")
        if (k_number is not None and k_number != ''):
            config.K_similarity = int(k_number)
        choose_method = request.POST.get("choose_method")
        choose_distance = request.POST.get("choose_distance")
        # Format select method: 1 = Hog, 2 = Sift feature, 3 = mix_feature_sift_hog, 4 = VGG16
        uploaded_file = request.FILES['document']
        if uploaded_file:
            fs = FileSystemStorage()
            config.name_upload = config.name_upload+1
            new_name = str(config.name_upload) + ".png"
            fs.save(new_name, uploaded_file)
            if choose_method == "1":
                process_API.HOG(new_name)
            if choose_method == "2":
                process_API.sift_feature(new_name)
            if choose_method == "3":
                process_API.mix_feature_sift_hog(new_name)
            if choose_method == "4":
                process_API.facenet(new_name)
            if choose_method == "5":
                process_API.resnet(new_name)
            if choose_method == "6":
                process_API.VGG16(new_name)
            if choose_method == "7":
                process_API.mix_facenet_vgg16(new_name)
            config.type_distance == int(choose_distance)
            result = process_request.process_img(new_name, choose_method)
    return render(request, 'pages/upload.html', result)


def screens(request):
    return render(request, 'pages/screens.html')


@csrf_exempt
def getframe(request):
    result = {
        "check": 2
    }
    data = request.body
    print(type(data))

    encoded = base64.encodebytes(data)

    with open(os.path.join(settings.STREAM_ROOT, 'image.png'), 'wb') as f:
        f.write(data)

    image = cv2.imread(os.path.join(settings.STREAM_ROOT, 'image.jpg'))
    print(image)
    # process_API.insightface(data)

    return render(request, 'pages/frame.json', result)

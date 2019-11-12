from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from . import process
from PIL import Image
import os
import cv2
import base64
import urllib.parse
import requests
import json
import sys
import numpy as np
from django.conf import settings
from . import config
# Create your views here.

def index(request):
    
    return render(request, 'pages/home.html')

def get_feature(x):
    """
        get tokenizer
    """
    path = settings.MEDIA_ROOT
    url_token = 'http://service.mmlab.uit.edu.vn/mmlab_api/user_login/post/'
    data ={'user_name': 'admin', 'password': 'admin'}
    headers = {'Content-type': 'application/json'}
    data_json = json.dumps(data)
    response = requests.post(url_token, data = data_json, headers=headers)
    _token = response.json()['token']
    """
        get feature
    """
    url_feature = 'http://service.mmlab.uit.edu.vn/mmlab_api/face/feature_extract/post'
    path_img = os.path.join(path,x)
    print("day la path",path_img)
    filename, file_extension = os.path.splitext(x)
    image = open(path_img, 'rb')
    image_read = image.read()
    encoded = base64.encodestring(image_read)
    encoded_string = encoded.decode('utf-8')
    ######################
    data ={'api_version': '1.0', 'token': _token, 'data': {'method': 'arcface', 'model': '0', 'image_encoded': encoded_string, 'bboxes': [[0, 0, 200, 300]], 'landmarks': [{'have_landmark': 'False'}]}}
    headers = {'Content-type': 'application/json'}
    data_json = json.dumps(data)
    response = requests.post(url_feature, data = data_json, headers=headers)
    decoded_string = base64.b64decode(response.json()['data']['features'][0])
    with open(filename+".npy", "wb") as image_file2:
      image_file2.write(decoded_string);   
  
    return 

# tree=None
# root=None
def upload(request):
    kq = []
    uploaded_file = None
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        if uploaded_file:
            fs = FileSystemStorage()
            fs.save(uploaded_file.name,uploaded_file)
            get_feature(uploaded_file.name)
            filename, file_extension = os.path.splitext(uploaded_file.name)
            
            feature = np.load("C://Users//DELL//Desktop//web-image//ImageSearch-BigData//report//app//"+filename+".npy")
            if config.VP_buid == False:
                config.root = process.vptree(1000)      
                config.root = config.build(0,999)
            
            config.root.search(config.root,feature,5)
            for x in config.root.heap:
                kq.append((x[0],x[1]))
    return render(request,'pages/upload.html')
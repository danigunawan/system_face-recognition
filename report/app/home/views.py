from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from . import process_Tree
from . import process_request
import os
import numpy as np
from django.conf import settings
from . import config
from . import process_API
# Create your views here.

def index(request):
    
    return render(request, 'pages/home.html')

def upload(request):
    result = {}
    uploaded_file = None
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        if uploaded_file:
            fs = FileSystemStorage()
            fs.save(uploaded_file.name,uploaded_file)
            process_API.VGG16(uploaded_file.name)
            result = process_request.process_img(uploaded_file.name)
    return render(request,'pages/upload.html',result)

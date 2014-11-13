# Create your views here.

from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.shortcuts import render_to_response, render
from project.settings import MEDIA_ROOT
import os


@csrf_protect
def index(request):
    """docstring for index"""
    return render(request, 'index.html', {'title': 'test page'})

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        flist = request.FILES.getlist('Filedata')
        for f in flist:
            handle_uploaded_file(f)
    return render_to_response('upload.html', {'flist':flist})


def handle_uploaded_file(f):
    fname = os.path.join(MEDIA_ROOT,f.name).replace('\\','/');
    dirname = os.path.dirname(fname)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(fname, 'wb+') as info:
        for chunk in f.chunks():
            info.write(chunk)
    return f




#######################################################################
def jupload(request):
    return render_to_response('uploadify.html',{})


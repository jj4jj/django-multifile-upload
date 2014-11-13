# Create your views here.

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
 
@csrf_protect
def index(request):
    """docstring for index"""
    return render(request, 'index.html', {'title': 'test page'})
 
def upload(request):
    if request.method == 'POST':
        flist = request.FILES.getlist('pic')
        for f in flist:
            handle_uploaded_file(f)
    return render_to_response('upload.html', {'flist':flist})
 
def handle_uploaded_file(f):
    fname = './upload/'+f.name;
    with open(fname, 'wb+') as info:
        for chunk in f.chunks():
            info.write(chunk)
    return f

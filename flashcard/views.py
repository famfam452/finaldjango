from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
import io,csv

from . import urls
# Create your views here.
def index(request):
    return render(request,'frontend/index.html')

def next(request):
    if request.method == 'POST':
        request_POST = request.POST
        if request_POST['your_name'] != '':
            return render(request,'frontend/next.html',{'nameof':request_POST['your_name']})
    return redirect('index')

def csv_upload(request):
    if request.method == 'GET':
        return redirect('next')
    elif request.method == 'POST':
        csv_file = request.FILES['inputGroupFile01']
        if csv_file.multiple_chunks() != True:
            data_read = csv_file.read().decode('UTF-8-SIG')
        else:
            for realine in csv_file.chunks():
                data_read = realine.decode('UTF-8-SIG')
        data_set = data_read.split()
        if data_set != [] and len(data_set) > 1:
            attribute = data_set[0]
            set_attr = attribute.split(',')
            row_instance = []
            for row in data_set[1:]:
                row_split = row.split(',')
                row_instance.append(row_split)
            return render(request,'frontend/contact.html',{'Attribute':set_attr,'DataInstance':row_instance})
    return redirect('next')

from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
import io,csv

from . import urls
from .forms import Nameform,FileCSVform
# Create your views here.
def index(request):
    if request.method == 'POST':
        request_POST = request.POST
        form = Nameform(request_POST)
        if request_POST['your_name'] != '' and form.is_valid():
            file_form = FileCSVform()
            return render(request,'frontend/next.html',{'nameof':form.cleaned_data['your_name'],'fileform':file_form})
    else:
        form = Nameform()
    return render(request,'frontend/index.html',{'form': form})

def csv_upload(request):
    if request.method == 'GET':
        return redirect('next')
    elif request.method == 'POST':
        csv_file = request.FILES['CSV_file']
        if csv_file.multiple_chunks() != True:
            data_read = csv_file.read().decode('UTF-8-SIG')
        else:
            for realine in csv_file.chunks():
                data_read = realine.decode('UTF-8-SIG')
        data_set = data_read.split('\r\n')
        if data_set != [] and len(data_set) > 1:
            attribute = data_set[0]
            set_attr = attribute.split(',')
            row_instance = []
            for row in data_set[1:]:
                row_split = row.split(',')
                row_instance.append(row_split)
            context = {'Attribute':set_attr,'DataInstance':row_instance}
            if request.POST['nameOf']:
                context.update({'nameof':request.POST['nameOf']})
            return render(request,'frontend/contact.html',context)
    return redirect('next')

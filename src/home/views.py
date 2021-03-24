from django.shortcuts import render, redirect, reverse
from .forms import TableDataForm
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import pandas as pd
import os
from django.urls import reverse_lazy
from timathon.settings import MEDIA_ROOT
# Create your views here.
table_data = []

# the home page
def index(request):
    return render(request, '../templates/home/index.html')

@login_required
def components(request):
    return render(request, '../templates/components/components.html')


def favourites(request):
    return render(request, '../templates/home/favourites.html')


def charts(request):
    return render(request, '../templates/components/charts/charts.html')


# def tables(request):
# parameters = {}
# if request.method == 'POST':
#     uploaded_file = request.FILES['datafile']
#     if uploaded_file.name.endswith('.csv'):
#         parameters = {'result': 'Correct File Uploaded'}
#     else:
#         parameters = {'result': 'Incorrect File Uploaded'}
#     # print(uploaded_file.name)
#     # print(uploaded_file.size)
#     fs = FileSystemStorage()
#     fs.save(uploaded_file.name, uploaded_file)
# return render(request, '../templates/components/tables/tables.html', context=parameters)


def tables(request):
    data = None
    if request.method == 'POST':
        form = TableDataForm(request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            form.save()
            data = pd.read_csv(os.path.join(MEDIA_ROOT, uploaded_file.name))
            table_data.append(data)
            return HttpResponseRedirect(reverse_lazy('home:table_results'))
    else:
        data = None
        form = TableDataForm()
    context = {"form": form}
    return render(request, '../templates/components/tables/tables.html', context)


def table_result(request):
    context = {'data': table_data[-1]}
    return render(request, '../templates/components/table_results/results.html', context)

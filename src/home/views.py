from io import StringIO

import pandas as pd
import os
import openpyxl
import time
import numpy as np

from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from .models import *

from timathon.settings import MEDIA_ROOT
from .forms import TableDataForm, ChartDataForm

# Create your views here.
table_data = []
chart_data = []

# the home page
def index(request):
    return render(request, 'home/index.html')


# @login_required
def components(request):
    return render(request, 'components/components.html')


def favourites(request):
    return render(request, 'home/favourites.html')


def extract_data(fp):
    """

    :param fp: file name
    :return: data in that file
    """

    if fp.endswith('csv'):
        data = pd.read_csv(fp)

    elif fp.endswith('xls') or fp.endswith('xlsx'):
        data = pd.read_excel(fp)

    return data


def tables(request):
    data = None
    if request.COOKIES.get('file'):
        return redirect('home:table_results')

    if request.method == 'POST':
        form = TableDataForm(request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            form.save()
            fn = os.path.join(MEDIA_ROOT, uploaded_file.name)

            UserFile(user_name=request.user.username, file_name=fn).save()

            data = extract_data(fn)
            table_data.append(data)
            # time.sleep(2)
            return HttpResponseRedirect(reverse_lazy('home:table_results'))
        else:
            print('OOF')
    else:
        data = None
        form = TableDataForm()
    context = {"form": form}
    return render(request, 'components/tables/tables.html', context)


def table_result(request):
    try:
        messages.success(request, 'Your Data Has Been Successfully Analyzed By Mentis Oculi')
        headers = []
        for header in table_data[-1]:
            headers.append(header)
        context = {'data': table_data[-1], 'headers': headers}
    except Exception:
        context = {'data': []}
    return render(request, 'components/table_results/results.html', context)


def charts_select(request):
    if request.COOKIES.get('chart_file'):
        # return redirect('home')
        pass
    if request.method == 'POST':
        form = ChartDataForm(request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['chart_file']
            fs = FileSystemStorage()
            # filename = uploaded_file.name
            fs.save(uploaded_file.name, uploaded_file)
            form.save()
            fn = os.path.join(MEDIA_ROOT, uploaded_file.name)
            chart_data.append(fn)
            UserFile(user_name=request.user.username, file_name=fn).save()
            return HttpResponseRedirect(reverse_lazy('home:charts_results'))
            # time.sleep(2)
            # return HttpResponseRedirect(reverse_lazy('home:table_results'))
        else:
            print('OOF')
    else:
        data = None
        form = TableDataForm()
    context = {"form": form}
    return render(request, 'components/tables/tables.html', context)
    # if request.method == 'GET':
    #     return render(request, "components/charts/select.html")
    # elif request.method == 'POST':
    #     # file extraction not working

    #     # print(request.FILES)
    #     # file = request.FILES['file']
    #     #
    #     # type_of_chart = request.POST['type']
    #     # fn = os.path.join(MEDIA_ROOT, file.name)
    #     # data = extract_data(fn)

    #     # making the plot
    #     x = np.arange(0, np.pi * 3, .1)
    #     y = np.sin(x)
    #     fig = plt.figure()
    #     plt.plot(x, y)

    #     # converting
    #     imgdata = StringIO()
    #     fig.savefig(imgdata, format='svg')
    #     imgdata.seek(0)
    #     to_return_plot = imgdata.getvalue()

    #     context = {
    #         'graph': to_return_plot
    #     }

    context = {}
    response = render(request, "components/charts/select.html", context)
    return response


def charts(request):
    global chart_data
    return render(request, 'components/charts/charts.html')


def my_files(request):
    if request.method == 'GET':
        return render(request, 'components/my_files.html')

    else:
        response = render(request, 'components/components.html')
        response.set_cookie("file", request.POST['fn'])
        return response


# Read dis LakBoi
# line 104-is the name of the file uploaded by the user
# line 107-is the whole path
# after the submit button he will be redirected to charts function
# so do the backend in that function
# chart_data[-1] is having the whole path and then u can use matpotlib and all stuff that idk
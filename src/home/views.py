from io import StringIO

import pandas as pd
import os
import openpyxl
import time
import numpy as np

from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from .models import *

from timathon.settings import MEDIA_ROOT
from .forms import TableDataForm, ChartDataForm, UploadedFilesForm

# Create your views here.
table_data = []
chart_data = []


# the home page
def index(request):
    return render(request, 'home/index.html')


# @login_required
def components(request):
    return render(request, 'components/components.html')


def extract_data(file):
    """

    :param fp: file name
    :return: data in that file
    """

    if file.name.endswith('csv'):
        data = pd.read_csv(file)

    elif file.name.endswith('xls') or file.name.endswith('xlsx'):
        data = pd.read_excel(file)

    return data


def save_form(request):
    form = UploadedFilesForm(request.POST, request.FILES)
    # form = TableDataForm(request.FILES)
    if form.is_valid():
        form.save()

    return form


@login_required
def tables(request):
    data = None
    if request.COOKIES.get('file'):
        return redirect('home:table_results')

    if request.method == 'POST':
        form = save_form(request)
        file = form.files["file"]
        data = extract_data(file)

        table_data.append(data)
        # time.sleep(2)
        return HttpResponseRedirect(reverse_lazy('home:table_results'))

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
    if request.COOKIES.get('chartfile'):
        return redirect('home:charts_results')
    if request.method == 'POST':
        form = ChartDataForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_chart_file = request.FILES['chartfile']
            fs = FileSystemStorage()
            # filename = uploaded_file.name
            fs.save(uploaded_chart_file.name, uploaded_chart_file)
            form.save()
            fn = os.path.join(MEDIA_ROOT, uploaded_chart_file.name)
            data = extract_data(fn)
            chart_data.append(data)
            UserFile(user_name=request.user.username, file_name=fn).save()
            return HttpResponseRedirect(reverse_lazy('home:charts_results'))
        else:
            print('OOF')
    else:
        form = ChartDataForm()
    context = {"form": form}
    return render(request, 'components/charts/select.html', context)


def charts(request):
    messages.success(request, 'Your Data Has Been Successfully Visualized By Mentis Oculi')
    global chart_data
    print(chart_data[-1])
    jsonData = chart_data[-1].to_json()
    print(jsonData)
    headers = []
    firstRow = []
    dataRow = []
    for header in chart_data[-1]:
        headers.append(header)
    for firstrow in chart_data[-1][f'{headers[0]}']:
        firstRow.append(firstrow)
    for datarow in chart_data[-1][f'{headers[-1]}']:
        dataRow.append(datarow)
    return render(request, 'components/charts/charts.html',
                  {'headers': headers, 'firstrow': firstRow, 'datarow': dataRow})


def my_files(request):
    if request.method == 'GET':
        return render(request, 'components/my_files.html')

    else:
        response = render(request, 'components/components.html')
        response.set_cookie("file", request.POST['fn'])
        return response


def json_data(request):
    global chart_data
    jsonData = chart_data[-1].to_json()
    print(jsonData)
    return JsonResponse(jsonData, safe=False)


# def debug(request):
#     data = []
#     dat = UserFile.objects.all()
#     for obj in dat:
#         data.append([obj.file, obj.username, obj.original_file_name])
#     return HttpResponse(str(data))

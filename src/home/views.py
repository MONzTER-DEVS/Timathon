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
    # form = TableDataForm(request.FILES)\
    if form.is_valid():
        form.save()

    return form


def tables(request):
    data = None
    if request.COOKIES.get('file'):
        data = extract_data(UserFile.objects.get(id=request.COOKIES.get('file')).file)  # get file data
        if data.username == request.user.username:
            table_data.append(data)
            response = HttpResponseRedirect(reverse_lazy('home:table_results'))
            response.delete_cookie('file')
            return response

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
    if request.COOKIES.get('file') and not request.COOKIES.get('serving_file'):

        # data = extract_data(UserFile.objects.get(id=request.COOKIES.get('file')).file)  # get file data
        # chart_data.append(data)
        # response = HttpResponseRedirect(reverse_lazy('home:charts_results'))
        # response.delete_cookie('file')
        context = {"hide_file_upload": True}
        response = render(request, 'components/charts/select.html', context)
        response.set_cookie("serving_file", 1)
        return response

    if request.method == 'POST':
        file_cookie = request.COOKIES.get("file")
        if file_cookie:
            data = extract_data(UserFile.objects.get(id=file_cookie).file)
        else:
            form = save_form(request)
            data = extract_data(form.files['file'])
        chart_data.append(data)

        response = HttpResponseRedirect(reverse_lazy('home:charts_results'))
        if file_cookie:
            response.delete_cookie("file")
            response.delete_cookie("serving_file")
        return response

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
        all_files = UserFile.objects.filter(username=request.user.username)
        return render(request, 'components/my_files.html', {"all_files": all_files})

    else:
        if request.POST["action"] == "delete":
            obj = UserFile.objects.get(id=request.POST["file_number"])
            if request.user.username == obj.username:
                obj.delete()

            return redirect("/my_files")

        response = redirect("/components")
        response.set_cookie("file", request.POST['pk'])
        return response


def json_data(request):
    global chart_data
    jsonData = chart_data[-1].to_json()
    print(jsonData)
    return JsonResponse(jsonData, safe=False)


def debug(request):
    data = []
    dat = UserFile.objects.all()
    for obj in dat:
        data.append([obj.file, obj.username, obj.original_file_name])
    return HttpResponse(str(data))

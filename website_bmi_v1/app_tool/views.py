from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index/index.html')

@csrf_exempt
def bmi(request, type):
    if request.method == 'GET':
        if type == 'index':
            return render(request, 'bmi/index.html')
@csrf_exempt
def temperature(request, type):
    if request.method == 'GET':
        if type == 'index':
            return render(request, 'temperature/index.html')

@csrf_exempt
def exchangeRate(request, type):
    if request.method == 'GET':
        if type == 'index':
            return render(request, 'exchangeRate/index.html')

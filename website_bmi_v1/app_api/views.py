from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app_api.controller import bmiController, temperatureController, exchangeRateController

@csrf_exempt
def bmi(request, type):
    if request.method == 'POST':
        if type == 'calculate':
            return bmiController.calculate(request)
            
@csrf_exempt
def temperature(request, type):
    if request.method == 'POST':
        if type == 'calculate':
            return temperatureController.calculate(request)
@csrf_exempt
def exchangeRate(request, type):
    if request.method == 'POST':
        if type == 'calculate':
            return exchangeRateController.calculate(request)

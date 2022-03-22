from django.http import JsonResponse
from app_api.util import temperatureUtil

import requests


def calculate(request):
    try:
        # 蒐集資料
        temperature = request.POST.get('temperature', '')
        convertType = request.POST.get('convertType', '')

        # 判斷資料
        if (temperature == ''):    
            raise Exception('缺少必填參數 temperature')
        if (convertType == ''):    
            raise Exception('缺少必填參數 convertType')
   
        # 整理從資料庫得到的資料
        data = temperatureUtil.calculate(temperature, convertType)
        
        # 初始化回傳值
        response = {
            'status' : 'success',
            'message' : 'success',
            'data' : data,
        }
    except Exception as e:
        # 初始化回傳值
        response = {
            'status' : 'error',
			'message' : str(e),
        }

    # 將回傳值回傳
    return JsonResponse(response)
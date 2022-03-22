from django.http import JsonResponse
from app_api.util import bmiUtil

import requests


def calculate(request):
    try:
        # 蒐集資料
        height = request.POST.get('height', '')
        weight = request.POST.get('weight', '')

        # 判斷資料
        if (height == ''):    
            raise Exception('缺少必填參數 height')
        if (weight == ''):    
            raise Exception('缺少必填參數 weight')
   
        # 整理從資料庫得到的資料
        data = bmiUtil.calculate(height, weight)
        
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
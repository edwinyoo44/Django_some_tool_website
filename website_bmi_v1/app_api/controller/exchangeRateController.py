from django.http import JsonResponse
from app_api.util import exchangeRateUtil

import requests


def calculate(request):
    try:
        # 蒐集資料
        amount = request.POST.get('amount', '')
        convertType = request.POST.get('convertType', '')

        # 判斷資料
        if (amount == ''):    
            raise Exception('缺少必填參數 amount')
        if (convertType == ''):    
            raise Exception('缺少必填參數 convertType')
   
        # 整理從資料庫得到的資料
        data = exchangeRateUtil.calculate(amount, convertType)
        
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
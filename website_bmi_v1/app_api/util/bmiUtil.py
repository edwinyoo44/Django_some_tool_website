
def calculate(height, weight):

    height = int(height)
    weight = int(weight)
    bmi = round( weight/(height/100)**2, 2)

    # 整理回傳資料
    response = {
        'weight' : weight,
        'height' : height,
        'bmi' : bmi,
    }
    
    return response

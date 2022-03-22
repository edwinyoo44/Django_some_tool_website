
def calculate(temperature, convertType):

    if (convertType == "F2C") :
        originalType = "°F"
        targetType = "°C"
        originalTemperature = float(temperature)
        targetTemperature = (originalTemperature - 32) * 5 /9

    elif (convertType == "C2F") :
        originalType = "°C"
        targetType = "°F"
        originalTemperature = float(temperature)
        targetTemperature = originalTemperature * 9 /5 + 32
    else :
        raise Exception('未知 convertType')


    # 整理回傳資料
    response = {
        'originalType' : originalType,
        'targetType' : targetType,
        'originalTemperature' : originalTemperature,
        'targetTemperature' : targetTemperature,
    }
    
    return response

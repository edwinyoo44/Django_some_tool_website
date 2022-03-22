import twder

def calculate(amount, convertType):

    if (convertType == "TWD2USD") :
        originalType = "TWD"
        targetType = "USD"
        sellRate = 1 / float(twder.now("USD")[2])
        originalAmount = float(amount)
        targetAmount = originalAmount * sellRate

    elif (convertType == "USD2TWD") :
        originalType = "USD"
        targetType = "TWD"
        sellRate = float(twder.now("USD")[2])
        originalAmount = float(amount)
        targetAmount = originalAmount * sellRate
    else :
        raise Exception('未知 convertType')


    # 整理回傳資料
    response = {
        'sellRate' : sellRate,
        'originalType' : originalType,
        'targetType' : targetType,
        'originalAmount' : originalAmount,
        'targetAmount' : targetAmount,
    }
    
    return response

import ReadAutomaticOutputs


outputs = []
#index 0fan. 1led. 2pump

theDicArray = ReadAutomaticOutputs.readTable()

tempDic = theDicArray[0]
humDic = theDicArray[1]
moisDic = theDicArray[2]
lightDic = theDicArray[3]

minTemp = tempDic["MinValue"]
maxTemp = tempDic["MaxValue"]
minHum = humDic["MinValue"]
maxHum = humDic["MaxValue"]
minMois = moisDic["MinValue"]
maxMois = moisDic["MaxValue"]
minLight = lightDic["MinValue"]
maxLight = lightDic["MaxValue"]


def logicaa(LDRValue, AHSValue, SMSValue, NTCValue):
    #FAN
    if ((NTCValue > maxTemp) or AHSValue > maxMois ):
        outputs[0] = 1
    else:
        outputs[0] = 0

    #LED
    if(LDRValue < minLight):
        outputs[1] = 1
    else:
        outputs[1] = 0
    #PUMP
    if(SMSValue < minMois or AHSValue < minHum):
        outputs[2] = 1
    else:
        outputs[2] = 0

    return outputs






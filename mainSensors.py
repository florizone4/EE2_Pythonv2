import readSMS
import readAHS
import readLDR
import readNTC
# import setFan
# import setLED
# import setPump
import time
# import connectDB
# import ReadManualOutputs

#SETTINGS
maxLight = 50
minLight = 20
maxHum = 50
minHum = 20
maxMois = 30
minMois = 10
maxTemp = 20



#NOTE THE SET FUNCTIONS CAN STILL BE BROKEN!!!

while True:


    # read sensors
    LDRValue = readLDR.get_lightValue() #finished
    AHSValue = readAHS.read_AHSValue() #finished
    SMSValue = readSMS.read_SMSValue() #finished
    NTCValue = readNTC.read_NTC() #change formula!
    # upload sensor data to the measurements database
    print("NTC: " + str(NTCValue) + ", AHS: " + str(AHSValue) + "SMS: " + str(SMSValue) + ", LDR: " + str(LDRValue))
    #connectDB.pushtoDB(LDRValue, AHSValue, SMSValue, NTCValue)

    time.sleep(10)





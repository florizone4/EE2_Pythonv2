import readSMS
import readAHS
import readDB
import readLDR
import readNTC
import setFan
import setLED
import setPump
import time
import connectDB
import ReadManualOutputs


while True:

    #read the outputs DataBase
    data = ReadManualOutputs.read_last_row_from_database()
    #manual mode
    if (len(data) != 0): #the array is only filled when manual mode is on
        setPump = data[1]
        Led = data[2]
        setFan = data[3]

    #AUTOMATIC mode
    # do some enable/disable logic
    # enable/ disable the pump, led, fan
    if(LDRValue > maxLight):
        setLED.setpumpert(0)
    elif(LDRValue < minLight):
        setLED.setpumpert(1)
    if(AHSValue > maxHum):
        setPump.setpumpert(0.9)
    elif(AHSValue < minHum):
        setPump.setpumpert(0)
    if(SMSSValue > maxMois):
        setPump.setpumpert(0.9)
    elif(SMSSValue < minMois):
        setPump.setpumpert(0)
    if(NTC > maxTemp):
        setFan.setpumpert(1)
    else:
        setFan.setpumpert(0)

    # read sensors
    LDRValue = readLDR.get_lightValue() #finished
    AHSValue = readAHS.read_AHSValue() #finished
    SMSValue = readSMS.read_SMSValue() #finished
    NTC = readNTC.read_NTC() #change formula!
    # upload sensor data to the measurements database
    connectDB.pushtoDB(LDRValue, AHSValue, SMSValue, NTC)

    time.sleep(10)





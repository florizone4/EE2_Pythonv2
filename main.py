import readSMS
import readAHS
import readLDR
import readNTC
import setFan
import setLED
import setPump
import time
import connectDB
import ReadManualOutputs
import ReadAutomaticOutputs

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
    LDRValue = readLDR.get_lightValue()         #finished
    AHSValue = readAHS.read_AHSValue()          #finished
    SMSValue = readSMS.read_SMSValue()          #finished
    NTCValue = readNTC.read_NTC()               #finished
    # upload sensor data to the measurements database
    print("NTC: " + str(NTCValue) + ", AHS: " + str(AHSValue) + "SMS: " + str(SMSValue) + ", LDR: " + str(LDRValue))

    #connectDB.pushtoDB(LDRValue, AHSValue, SMSValue, NTC)


    #read the outputs DataBase
    data = ReadManualOutputs.read_last_row_from_database()
    autoTable = ReadAutomaticOutputs.readTable()
    #the logic
    if (len(data) != 0): #the array is only filled when a successful connection is made to the ReadOutputs Database
        #If PumpManualMode is ON, set setPump to the manual value
        #manual
        if(data[4] == 1):
            setPump = data[1]
        #automatic
        else:
            if(AHSValue > autoTable['LowerMois']):
                setPump.setpumpert(0.9)
            elif(AHSValue < autoTable['UpperMois']):
                setPump.setpumpert(0)


        #the same for Led
        #manual
        if(data[5] == 1):
            Led = data[2]
        #automatic
        else:
            if(LDRValue > autoTable['LowerLight']):
                setLED.setpumpert(0)
            elif(LDRValue < autoTable['UpperLight']):
                setLED.setpumpert(1)

        #also the same for Fan
        #manual
        if(data[6]== 1):
            setFan = data[3]
        #automatic
        else:
            if(SMSValue > autoTable('UpperTemp')):
                setFan.setpumpert(0.9)
            elif(SMSValue < autoTable('LowerTemp')):
                setFan.setpumpert(0)



#    else:
        #AUTOMATIC mode
        # do some enable/disable logic
        # enable/ disable the pump, led, fan
#        if(LDRValue > maxLight):
#            setLED.setpumpert(0)
#        elif(LDRValue < minLight):
#            setLED.setpumpert(1)
#        if(AHSValue > maxHum):
#            setPump.setpumpert(0.9)
#        elif(AHSValue < minHum):
#            setPump.setpumpert(0)
#        if(SMSValue > maxMois):
#            setPump.setpumpert(0.9)
#        elif(SMSValue < minMois):
#            setPump.setpumpert(0)
#        if(NTC > maxTemp):
#            setFan.setpumpert(1)
#        else:
#            setFan.setpumpert(0)



    time.sleep(10)





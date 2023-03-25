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


print("koekoek")


while True:


    # read sensors
    LDRValue = readLDR.get_lightValue()         #finished
    AHSValue = readAHS.read_AHSValue()          #finished
    SMSValue = readSMS.read_SMSValue()          #finished
    NTCValue = readNTC.read_NTC()               #finished
    # upload sensor data to the measurements database
    print("NTC: " + str(NTCValue) + ", AHS: " + str(AHSValue) + "SMS: " + str(SMSValue) + ", LDR: " + str(LDRValue))
    connectDB.pushtoDB(LDRValue, AHSValue, SMSValue, NTCValue)

    #UNCOMMENT THIS!!
    #connectDB.pushtoDB(LDRValue, AHSValue, SMSValue, NTC)


    #read the outputs DataBase
    print("Here")
    data = ReadManualOutputs.read_last_row_from_database()
    #   0,          1,         2,         3,           4,            5,           6
    #  ID, autoPumpManualPump, ManualLed, ManualFan, IsPumpManual, IsLedManual, IsFanManual
    print("data " , data[0])
    #the logic
    #the array is only filled when a successful connection is made to the ReadOutputs Database
        #If PumpManualMode is ON, set setPump to the manual value
        #manual
    print("jaja")
        # if(data[4] == 1):
        #     setPump.setpumpert(data[1])
        # #automatic
        # else:
        #     if(LDRValue > maxLight):
        #         setLED.setpumpert(0)
        #     elif(LDRValue < minLight):
        #         setLED.setpumpert(1)
    #FAN
    if(data[9] == 1):
        setFan.setpumpert(data[6]/100)
        print("manual " , data[6]/100)
    else:
        setFan.setpumpert(data[3])
        print("automatic " , data[3])

    #LED
    if (data[8]== 1):
        setLED.setpumpert(data[5]/100)
    else:
        setLED.setpumpert(data[2])

    #PUMP
    if(data[7] == 1):
        setPump.setpumpert(data[4]/100)
        print("manual " , data[4]/100)
    else:
        setPump.setpumpert(data[1])
        print("automatic " , data[1])










        #the same for Led
        #manual
        # if(data[8] == 1):
        #     Led = data[5]/100
        # #automatic
        # else:
        #     Led = data[2]
        # setLED.setpumpert(Led)


        #also the same for Fan
        # #manual
        # if(data[6]== 1):
        #     setFan = data[3]
        # #automatic
        # else:
        #     if(SMSValue > maxMois):
        #         setPump.setpumpert(0.9)
        #     elif(SMSValue < minMois):
        #         setPump.setpumpert(0)



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



    time.sleep(2)





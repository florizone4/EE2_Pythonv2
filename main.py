import ReadAutomaticOutputs
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
import logica

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



    #read the outputs DataBase
    data = ReadManualOutputs.read_last_row_from_database()
    autoData = ReadAutomaticOutputs.readTable()
    #   0,          1,         2,         3,           4,            5,           6
    #  ID, autoPumpManualPump, ManualLed, ManualFan, IsPumpManual, IsLedManual, IsFanManual
    print("data " , data)

    #FAN
    if(data[9] == 1):
        setFan.setpumpert(data[6]/100)
        print("manual " , data[6]/100)
    else:
        setFan.setpumpert(logica.logicaa()[0])
        print("automatic fan " , logica.logicaa()[0])

    #LED
    if (data[8]== 1):
        setLED.setpumpert(data[5]/100)
    else:
        setLED.setpumpert(logica.logicaa()[1])
        print("automatic led " , logica.logicaa()[1])

    #PUMP
    if(data[7] == 1):
        setPump.setpumpert(data[4]/100)
        print("manual " , data[4]/100)
    else:
        setPump.setpumpert(logica.logicaa()[2])
        print("automatic pump" , logica.logicaa()[2])



    time.sleep(10)





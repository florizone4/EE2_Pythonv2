import readSMS
import readAHS
import readDB
import readLDR
import readNTC
from gpiozero import


while True:

    #read the outputs DataBase

    # do some enable/disable logic

    # enable/ disable the pump, led, fan

    # read sensors
    LDRValue = readLDR.get_lightValue() #finished
    AHSValue = readAHS.read_AHSValue() #finished
    SMSValue = readSMS.read_SMSValue() #finished
    NTC = readNTC.read_NTC() #change formula!
    # upload sensor data




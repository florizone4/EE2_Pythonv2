# from gpiozero import MCP3008

# SMS = MCP3008(channel=0, clock_pin=17, mosi_pin=18, miso_pin=27)
# AHS = MCP3008(channel=1, clock_pin=17, mosi_pin=18, miso_pin=27)
# NTC = MCP3008(channel=2, clock_pin=17, mosi_pin=18, miso_pin=27)
# LDR = MCP3008(channel=3, clock_pin=17, mosi_pin=18, miso_pin=27)

import ReadAutomaticOutputs

ReadAutomaticOutputs.readTable()

import ReadManualOutputs

ReadManualOutputs.read_last_row_from_database()


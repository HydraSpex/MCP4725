#!/usr/bin/env python

from MCP4725_lib import MCP4725_60              #MCP4725_61, MCP4725_62, MCP4725_63, MCP4725_64, MCP4725_65, MCP4725_66, MCP4725_67
DAC = MCP4725_60()                              #MCP4725_61, MCP4725_62, MCP4725_63, MCP4725_64, MCP4725_65, MCP4725_66, MCP4725_67

while True:
    i = 0
    while i <= 4095:
        print(i)
        DAC.set_voltage(i) 
        i += 1

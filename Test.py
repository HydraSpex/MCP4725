#!/usr/bin/env python

from MCP4725_lib import MCP4725_60
DAC = MCP4725_60()

while True:
    i = 0
    while i <= 4095:
        print(i)
        DAC.set_voltage(i) 
        i += 1
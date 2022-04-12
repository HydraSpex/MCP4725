# MCP4725
This library is for the MCP4725 12-bit Digital-to-Analog Converter with EEPROM connected via I²C and its variants, and is tested on the MCP4725A0 and MCP4725A1.<br>
Also works with the Adafruit, Sparkfun an other brand Breakout Boards.<br>
It is designed to work on a Raspberry Pi and requires Python 3.

## Installation & Requirements
Just copy the library (MCP4725_lib.py) in your project folder.<br>
Requires "smbus". Normally preinstalled!

## Supports the major MCP4725 features:
- Fast write
- Register write
- EEPROM write
- Power down

## Usage
Use MCP4725_60 if the A0 Pin of the MCP4725A0 is connected to GND and the MCP4725_61 if it is connected to VDD.
Use MCP4725_62 if the A1 Pin of the MCP4725A0 is connected to GND and the MCP4725_63 if it is connected to VDD.
Use MCP4725_64 if the A2 Pin of the MCP4725A0 is connected to GND and the MCP4725_65 if it is connected to VDD.
Use MCP4725_66 if the A3 Pin of the MCP4725A0 is connected to GND and the MCP4725_67 if it is connected to VDD.
The values range from 0 to 4095 (12-Bit)

## Extra
In the repo you will find the datasheet for the MCP4725 series.

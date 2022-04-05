#!/usr/bin/env python

import smbus

#Registry Values
WRITEDAC = 0x40
WRITEFAST = 0x00
WRITEDACEEPROM = 0x60

#Registry Powerdown
POWERDOWN = {1: 0x10, 100: 0x20, 500: 0x30}

# Default I2C-Addresses
MCP4725_DEFAULT_ADDRESS_60  = 0x60                                              #Default for MCP4725A0 T-E/CH with A0 Pin tied to GND
MCP4725_DEFAULT_ADDRESS_61  = 0x61                                              #Default for MCP4725A0 T-E/CH with A0 Pin tied to VDD
MCP4725_DEFAULT_ADDRESS_62  = 0x62                                              #Default for MCP4725A1 T-E/CH with A0 Pin tied to GND
MCP4725_DEFAULT_ADDRESS_63  = 0x63                                              #Default for MCP4725A1 T-E/CH with A0 Pin tied to VDD
MCP4725_DEFAULT_ADDRESS_64  = 0x64                                              #Default for MCP4725A2 T-E/CH with A0 Pin tied to GND
MCP4725_DEFAULT_ADDRESS_65  = 0x65                                              #Default for MCP4725A2 T-E/CH with A0 Pin tied to VDD
MCP4725_DEFAULT_ADDRESS_66  = 0x66                                              #Default for MCP4725A3 T-E/CH with A0 Pin tied to GND
MCP4725_DEFAULT_ADDRESS_67  = 0x67                                              #Default for MCP4725A3 T-E/CH with A0 Pin tied to VDD


class MCP4725_60(object):
    def __init__(self, address = MCP4725_DEFAULT_ADDRESS_60, numbus = 1):
        self._address = address
        self._smbus = smbus.SMBus(numbus)

    def writeReg(self, reg, regdata):                                           #main write command
        self._smbus.write_i2c_block_data(self._address, reg, regdata)

    def set_voltage(self, val, persist=False):                                #value is a positive 12-bit number (0-4095). The corresponding Vout = (VDD*value)/4096 
        val = val & 0xFFF
        data = [(val >> 4) & 0xFF, (val << 4) & 0xFF]
        if persist:
            self.writeReg(WRITEDACEEPROM, data)                                 #If persist = True the value will be stored in EEPROM
        else:
            self.writeReg(WRITEDAC, data)

    def fast_voltage(self, val):
        val = val & 0xFFF
        regval = val >> 8
        regval |= WRITEFAST
        self.writeReg(regval, [val & 0xFF])

    def powerdown(self,res=1):
        if (res == 1) or (res == 100) or (res == 500):
            offmode = POWERDOWN[res]
            offmode |= WRITEFAST
            self.writeReg(offmode, [0x00])
            return res
        else:
            return -1


class MCP4725_61(object):
    def __init__(self, address = MCP4725_DEFAULT_ADDRESS_61, numbus = 1):
        self._address = address
        self._smbus = smbus.SMBus(numbus)

    def writeReg(self, reg, regdata):                                           #main write command
        self._smbus.write_i2c_block_data(self._address, reg, regdata)

    def set_voltage(self, val, persist=False):                                #value is a positive 12-bit number (0-4095). The corresponding Vout = (VDD*value)/4096 
        val = val & 0xFFF
        data = [(val >> 4) & 0xFF, (val << 4) & 0xFF]
        if persist:
            self.writeReg(WRITEDACEEPROM, data)                                 #If persist = True the value will be stored in EEPROM
        else:
            self.writeReg(WRITEDAC, data)

    def fast_voltage(self, val):
        val = val & 0xFFF
        regval = val >> 8
        regval |= WRITEFAST
        self.writeReg(regval, [val & 0xFF])

    def powerdown(self,res=1):
        if (res == 1) or (res == 100) or (res == 500):
            offmode = POWERDOWN[res]
            offmode |= WRITEFAST
            self.writeReg(offmode, [0x00])
            return res
        else:
            return -1


class MCP4725_62(object):
    def __init__(self, address = MCP4725_DEFAULT_ADDRESS_62, numbus = 1):
        self._address = address
        self._smbus = smbus.SMBus(numbus)

    def writeReg(self, reg, regdata):                                           #main write command
        self._smbus.write_i2c_block_data(self._address, reg, regdata)

    def set_voltage(self, val, persist=False):                                #value is a positive 12-bit number (0-4095). The corresponding Vout = (VDD*value)/4096 
        val = val & 0xFFF
        data = [(val >> 4) & 0xFF, (val << 4) & 0xFF]
        if persist:
            self.writeReg(WRITEDACEEPROM, data)                                 #If persist = True the value will be stored in EEPROM
        else:
            self.writeReg(WRITEDAC, data)

    def fast_voltage(self, val):
        val = val & 0xFFF
        regval = val >> 8
        regval |= WRITEFAST
        self.writeReg(regval, [val & 0xFF])

    def powerdown(self,res=1):
        if (res == 1) or (res == 100) or (res == 500):
            offmode = POWERDOWN[res]
            offmode |= WRITEFAST
            self.writeReg(offmode, [0x00])
            return res
        else:
            return -1


class MCP4725_63(object):
    def __init__(self, address = MCP4725_DEFAULT_ADDRESS_63, numbus = 1):
        self._address = address
        self._smbus = smbus.SMBus(numbus)

    def writeReg(self, reg, regdata):                                           #main write command
        self._smbus.write_i2c_block_data(self._address, reg, regdata)

    def set_voltage(self, val, persist=False):                                #value is a positive 12-bit number (0-4095). The corresponding Vout = (VDD*value)/4096 
        val = val & 0xFFF
        data = [(val >> 4) & 0xFF, (val << 4) & 0xFF]
        if persist:
            self.writeReg(WRITEDACEEPROM, data)                                 #If persist = True the value will be stored in EEPROM
        else:
            self.writeReg(WRITEDAC, data)

    def fast_voltage(self, val):
        val = val & 0xFFF
        regval = val >> 8
        regval |= WRITEFAST
        self.writeReg(regval, [val & 0xFF])

    def powerdown(self,res=1):
        if (res == 1) or (res == 100) or (res == 500):
            offmode = POWERDOWN[res]
            offmode |= WRITEFAST
            self.writeReg(offmode, [0x00])
            return res
        else:
            return -1


class MCP4725_64(object):
    def __init__(self, address = MCP4725_DEFAULT_ADDRESS_64, numbus = 1):
        self._address = address
        self._smbus = smbus.SMBus(numbus)

    def writeReg(self, reg, regdata):                                           #main write command
        self._smbus.write_i2c_block_data(self._address, reg, regdata)

    def set_voltage(self, val, persist=False):                                #value is a positive 12-bit number (0-4095). The corresponding Vout = (VDD*value)/4096 
        val = val & 0xFFF
        data = [(val >> 4) & 0xFF, (val << 4) & 0xFF]
        if persist:
            self.writeReg(WRITEDACEEPROM, data)                                 #If persist = True the value will be stored in EEPROM
        else:
            self.writeReg(WRITEDAC, data)

    def fast_voltage(self, val):
        val = val & 0xFFF
        regval = val >> 8
        regval |= WRITEFAST
        self.writeReg(regval, [val & 0xFF])

    def powerdown(self,res=1):
        if (res == 1) or (res == 100) or (res == 500):
            offmode = POWERDOWN[res]
            offmode |= WRITEFAST
            self.writeReg(offmode, [0x00])
            return res
        else:
            return -1


class MCP4725_65(object):
    def __init__(self, address = MCP4725_DEFAULT_ADDRESS_65, numbus = 1):
        self._address = address
        self._smbus = smbus.SMBus(numbus)

    def writeReg(self, reg, regdata):                                           #main write command
        self._smbus.write_i2c_block_data(self._address, reg, regdata)

    def set_voltage(self, val, persist=False):                                #value is a positive 12-bit number (0-4095). The corresponding Vout = (VDD*value)/4096 
        val = val & 0xFFF
        data = [(val >> 4) & 0xFF, (val << 4) & 0xFF]
        if persist:
            self.writeReg(WRITEDACEEPROM, data)                                 #If persist = True the value will be stored in EEPROM
        else:
            self.writeReg(WRITEDAC, data)

    def fast_voltage(self, val):
        val = val & 0xFFF
        regval = val >> 8
        regval |= WRITEFAST
        self.writeReg(regval, [val & 0xFF])

    def powerdown(self,res=1):
        if (res == 1) or (res == 100) or (res == 500):
            offmode = POWERDOWN[res]
            offmode |= WRITEFAST
            self.writeReg(offmode, [0x00])
            return res
        else:
            return -1


class MCP4725_66(object):
    def __init__(self, address = MCP4725_DEFAULT_ADDRESS_66, numbus = 1):
        self._address = address
        self._smbus = smbus.SMBus(numbus)

    def writeReg(self, reg, regdata):                                           #main write command
        self._smbus.write_i2c_block_data(self._address, reg, regdata)

    def set_voltage(self, val, persist=False):                                #value is a positive 12-bit number (0-4095). The corresponding Vout = (VDD*value)/4096 
        val = val & 0xFFF
        data = [(val >> 4) & 0xFF, (val << 4) & 0xFF]
        if persist:
            self.writeReg(WRITEDACEEPROM, data)                                 #If persist = True the value will be stored in EEPROM
        else:
            self.writeReg(WRITEDAC, data)

    def fast_voltage(self, val):
        val = val & 0xFFF
        regval = val >> 8
        regval |= WRITEFAST
        self.writeReg(regval, [val & 0xFF])

    def powerdown(self,res=1):
        if (res == 1) or (res == 100) or (res == 500):
            offmode = POWERDOWN[res]
            offmode |= WRITEFAST
            self.writeReg(offmode, [0x00])
            return res
        else:
            return -1


class MCP4725_67(object):
    def __init__(self, address = MCP4725_DEFAULT_ADDRESS_67, numbus = 1):
        self._address = address
        self._smbus = smbus.SMBus(numbus)

    def writeReg(self, reg, regdata):                                           #main write command
        self._smbus.write_i2c_block_data(self._address, reg, regdata)

    def set_voltage(self, val, persist=False):                                #value is a positive 12-bit number (0-4095). The corresponding Vout = (VDD*value)/4096 
        val = val & 0xFFF
        data = [(val >> 4) & 0xFF, (val << 4) & 0xFF]
        if persist:
            self.writeReg(WRITEDACEEPROM, data)                                 #If persist = True the value will be stored in EEPROM
        else:
            self.writeReg(WRITEDAC, data)

    def fast_voltage(self, val):
        val = val & 0xFFF
        regval = val >> 8
        regval |= WRITEFAST
        self.writeReg(regval, [val & 0xFF])

    def powerdown(self,res=1):
        if (res == 1) or (res == 100) or (res == 500):
            offmode = POWERDOWN[res]
            offmode |= WRITEFAST
            self.writeReg(offmode, [0x00])
            return res
        else:
            return -1
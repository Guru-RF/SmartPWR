import board
import math
import time
import analogio
from digitalio import DigitalInOut, Direction, Pull
import OLED
import usb_cdc
#import countio

serial = usb_cdc.data

btn = DigitalInOut(board.GP12)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

rf1Level = analogio.AnalogIn(board.GP26)
    
#freqCounter = countio.Counter(board.GP15, edge=countio.Edge.RISE)
#
#
#def freq():
#    freqCounter.reset()
#    time.sleep(10)
#    return freqCounter.count

def rf1_voltage():
    return (rf1Level.value / 65535 * rf1Level.reference_voltage)

def rf1_ppower():
    while True:
        result = 0
        for x in range(10000):
            voltage = rf1_voltage()
            if voltage > result:
                result = voltage

        if result > 0.015:
            voltage = rf1_voltage()
            if voltage > result:
                result = voltage
            output = round(result * 5.2,4)
            if output < 1:
                output = output*1000
                msg = 'A {message: <13}'.format(message=str(round(output,2))+" mW")
                if serial is not None and serial.connected:
                    serial.write(str.encode(msg + " Peak\r\n"))
                OLED.printPWR(msg)
            else:
                msg = 'A {message: <13}'.format(message=str(round(output,2))+" W")
                if serial is not None and serial.connected:
                    serial.write(str.encode(msg + " Peak\r\n"))
                OLED.printPWR(msg)
        else:
            return False


def rf1_apower():
    counter = 0
    sum = 0
    while True:
        result = 0
        for x in range(10000):
            voltage = rf1_voltage()
            if voltage > result:
                result = voltage

        if result > 0.04:
            voltage = rf1_voltage()
            sum = voltage + sum
            counter = counter + 1
            output = round((sum/counter) * 3.1,4)
            if output < 1:
                output = output*1000
                msg = 'A {message: <13}'.format(message=str(round(output,2))+" mW")
                if serial is not None and serial.connected:
                    serial.write(str.encode(msg + " Average\r\n"))
                OLED.printPWR(msg)
            else:
                msg = 'A {message: <13}'.format(message=str(round(output,2))+" W")
                if serial is not None and serial.connected:
                    serial.write(str.encode(msg + " Average\r\n"))
                OLED.printPWR(msg)
        else:
            return False
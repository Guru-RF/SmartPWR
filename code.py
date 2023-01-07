import OLED
import time
import SmartPWR

mode='peak'

if mode == 'peak':
    OLED.printTitle("PEAK Pwr")
if mode == 'average':
    OLED.printTitle("AVG Pwr")

while True:
    OLED.printPWR('Waiting...')
    if mode == 'peak':
        SmartPWR.rf1_ppower()
    if mode == 'average':
        SmartPWR.rf1_apower()
import time

import analogio
import board

# reference voltage (more accurate then the RP2040)
ADR4533 = analogio.AnalogIn(board.A3)
AD8307 = analogio.AnalogIn(board.A0)
AD8361 = analogio.AnalogIn(board.A2)


def _voltage_internal(device):
    return device.value / 65535 * device.reference_voltage


def _voltage_adr4533(device):
    return device.value / 65535 * _voltage_internal(ADR4533)


# P(dBm)=(V/25)-84
def _ad8307_PdBm():
    return (_voltage_adr4533(AD8307) / 25) - 84


# P(dBm)=(V/22)-60
def _ad8371_PdBm():
    return (_voltage_adr4533(AD8361) / 22) - 60


while True:
    print(
        "AD8307: V:"
        + str(_voltage_adr4533(AD8307))
        + " P:"
        + str(_ad8307_PdBm())
        + "dBm"
    )
    print(
        "AD8361: V:"
        + str(_voltage_adr4533(AD8361))
        + " P:"
        + str(_ad8371_PdBm())
        + "dBm"
    )
    print(
        "ADR4533: "
        + str(_voltage_internal(ADR4533))
        + " INTERNAL: "
        + str(AD8307.reference_voltage)
    )
    time.sleep(1)


#    if mode == 'peak':
#        SmartPWR.rf1_ppower()
#    if mode == 'average':
#        SmartPWR.rf1_apower()
#
#    if SmartPWR.btn.value is False:
#        print('btn')
#        if mode is 'peak':
#            mode = 'average';
#            OLED.printTitle("AVG  Pwr")
#        elif mode is 'average':
#            mode = 'peak'
#            OLED.printTitle("PEAK Pwr")
#        time.sleep(.5)

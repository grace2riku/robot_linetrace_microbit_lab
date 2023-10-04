# サイトに書いてあったpythonコード → 動かない
# https://switch-education.com/pyfiles/robotbase-linesensor/Robotbase_MotorTestV2-main.py
#imports go at the top
from microbit import *

# Code in a 'While True:' loop repeats forever
while True:
    if button_a.was_pressed():
        pin13.write_digital(0)
        pin15.write_analog(500)
        pin14.write_digital(0)
        pin16.write_analog(500)
        sleep(1000)
        pin15.write_analog(0)
        pin16.write_analog(0)
    if button_b.was_pressed():
        pin13.write_analog(500)
        pin15.write_digital(0)
        pin14.write_analog(500)
        pin16.write_digital(0)
        sleep(1000)
        pin13.write_analog(0)
        pin15.write_analog(0)


# 以下はブロックでコーディングし自動生成されていたpythonコード→期待とおり動いた
# https://makecode.microbit.org/85791-66732-57920-94529
def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P13, 0)
    pins.analog_write_pin(AnalogPin.P15, 500)
    pins.digital_write_pin(DigitalPin.P14, 0)
    pins.analog_write_pin(AnalogPin.P16, 500)
    basic.pause(1000)
    pins.analog_write_pin(AnalogPin.P15, 0)
    pins.analog_write_pin(AnalogPin.P16, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.analog_write_pin(AnalogPin.P13, 500)
    pins.digital_write_pin(DigitalPin.P15, 0)
    pins.analog_write_pin(AnalogPin.P14, 500)
    pins.digital_write_pin(DigitalPin.P16, 0)
    basic.pause(1000)
    pins.analog_write_pin(AnalogPin.P13, 0)
    pins.analog_write_pin(AnalogPin.P14, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

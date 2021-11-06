# SimpleDFPlayerMini-for-Python
Port of https://github.com/thokis/SimpleDFPlayerMini-for-MicroPython for Raspberry Pi.

This module enables Python-based projects to use the DFPlayer Mini via simple function calls.

It only supports **SD-Card playback** and operates in **tranmit only** mode.

## Why?

The DFPlayer generally doesn't bring much benefit on a device like the Raspberry Pi. There are enough other possibilities to play audio. However, I had the case that I already used an I2S sound card for other things (telephony/baresip) and also wanted to play music without having to pay attention to how the volume is set (doorbell). In my opinion, DFPlayer is the easiest and best way to play the ringtone.

## Usage

First import the SimpleDFPlayerMini module from `dfplayer.py`

`from dfplayer import SimpleDFPlayerMini`

Then create an instance of SimpleDFPlayerMini

`player = SimpleDFPlayerMini(5)`

Arguments for the constructor consist of the following parameters:
1. GPIO pin used for TX (pigpio GPIO number, e.g. 5 for GPIO5)

The above constructor initializes a `SimpleDFPlayerMini` object on GPIO pin `5`.
You also need to install pigpio:
sudo apt install pigpio

The function calls are self-explanatory for the most cases. If not take a look at the [wiki](https://github.com/thokis/SimpleDFPlayerMini-for-MicroPython/wiki/API).

## Connection

Basically you only have to connect the `RX` of the DFPlayerMini to the specific `TX` port of your board. Continuing our example from before `RX` from the DFPlayerMini goes to `GPIO5` on the Raspberry Pi.
Also solder a 1k resistor inbetween the connection or professionally speaking in serial.

            |----DFPLAYER-MINI----|
PI 3.3v ----|VCC--------------BUSY|
PI GPIO5 ---|RX---------------USB-|
            |TX---------------USB+|
            |DAC_R---------ADKEY_2|
            |DAC_I---------ADKEY_1|
      |-----|SPK_1------------IO_2|
   Speaker  |GND---------------GND|--- PI GND
      |-----|SPK_2------------IO_1|
            |--------|_SD_|-------|


No other Pins (except VCC and GND) should be used.

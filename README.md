# SimpleDFPlayerMini-for-MicroPython

This module enables MicroPython-based projects to use the DFPlayer Mini via simple function calls.

It only supports **SD-Card playback** and operates in **tranmit only** mode.

## Usage

First import the SimpleDFPlayerMini module from `dfplayer.py`

`from dfplayer import SimpleDFPlayerMini`

Then create an instance of SimpleDFPlayerMini

`player = SimpleDFPlayerMini(1, 0, 1)`

Arguments for the constructor consist of the following parameters:
1. The UART-id
2. Initial volume
3. Initial playback mode

The above constructor initializes a `SimpleDFPlayerMini` object with UART-id `1`, an initial volume of `0` and the `folder repeat` playback mode.
As a example for the ESP8266 this means `UART1` is used which supports TX-only communication via `GPIO2`. This may differ from board to board so take a look at [this](https://docs.micropython.org/en/latest/esp8266/quickref.html#).

The function calls are self-explanatory for the most cases. If not take a look at the [wiki](https://github.com/thokis/SimpleDFPlayerMini-for-MicroPython/wiki/API).

## Connection

Basically you only have to connect the `RX` of the DFPlayerMini to the specific `TX` port of your board. Continuing our example from before `RX` from the DFPlayerMini goes to `GPIO2` on the ESP8266.

Also solder a 1k resistor inbetween the connection or professionaly speaking in serial.

No other Pins (except VCC and GND) should be used.

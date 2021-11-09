"""
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
"""

from dfplayer import SimpleDFPlayerMini
from time import sleep

print("DFPlayer Mini Example")

player = SimpleDFPlayerMini(tx_pin=5)

command = None

def tryGetCommand(name):
    '''queries dfplayer.py for the method name and returns the method'''
    try:
        func = getattr(player, name)
        command = func()
        print("Command is: " + name)
    except AttributeError:
        print("Command " + name + "not found, try to write 'next_track' to invoke def next_track in dfplayer.py")
        print("Only commands without parameters are supported")
        print("'exit' to close the program'")

tryGetCommand("play") #finds the play method and saves it into 'command'

while True:
    if command is not None:
        command() #execute the last command

    userInput = input("Write command: ") # ask user for next command
    
    if userInput == "exit":
        player.reset()
        exit()

    tryGetCommand(userInput)

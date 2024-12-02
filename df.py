from dfplayer import SimpleDFPlayerMini
from utime import sleep

# Assuming TX pin for UART is connected to GPIO15 (adjust based on your setup)
TX_PIN = 26  

# Initialize the DFPlayer Mini
print("setting dfplayer object")
player = SimpleDFPlayerMini(tx_pin=TX_PIN)

# Set the volume (range: 0-30)
print("setting volume")
player.set_vol(20)

# Select a track to play (assuming tracks are numbered starting from 1)

print("setting track number")
track_number = 1
player.sel_track(track_number)

print("Ready to play track 1")
# Play the selected track
player.play()

print("Playing track 1.")
# Keep the program running while the track plays
try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    print("Stopping playback.")

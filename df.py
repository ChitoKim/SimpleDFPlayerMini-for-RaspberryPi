from dfplayer import SimpleDFPlayerMini
from time import slee

# Assuming TX pin for UART is connected to GPIO15 (adjust based on your setup)
TX_PIN = 15  

# Initialize the DFPlayer Mini
player = SimpleDFPlayerMini(tx_pin=TX_PIN)

# Set the volume (range: 0-30)
player.set_vol(20)

# Select a track to play (assuming tracks are numbered starting from 1)
track_number = 1
player.sel_track(track_number)

# Play the selected track
player.play()

# Keep the program running while the track plays
while True:
    pass

from microbit import *
import music, uart

# Initialize UART to match the 115200 Baud rate in H0
uart.init(baudrate=115200)

def fear_response():
    """The physical expression of the fear state."""
    display.show(Image.SKULL)
    # Play a 'startle' sequence: notes and durations
    music.play(['c5:1', 'b4:1', 'a4:2'])
    display.clear()

# Main Event Loop
while True:
    if uart.any():
        # Read the incoming message and clean up formatting
        msg = uart.readline().strip().upper()

        # Check if the message matches our 'contract' from H0
        if msg == b'FEAR':
            fear_response()

    # Minimal sleep to prevent the CPU from overheating
    # while staying responsive to incoming commands
    sleep(10)

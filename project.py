#This project uses a MIDI Lanuchpad to control X-Plane, a flight simulator game.
import os
os.environ['MIDO_BACKEND'] = 'mido.backends.pygame'

import mido
import keyboard

# Function to print all received messages
def print_received_messages():
    print("Listening for ALL MIDI events...")
    with mido.open_input(None) as inport:
        for msg in inport:
            print("Received message:", msg)

print_received_messages()


# Replace this with the name of your MIDI device
midi_device_name = 'Launchpad'

# Function to map MIDI messages to key presses
def midi_to_key(midi_msg):
    print("The MIDI message is: ", midi_msg)
    if midi_msg.note == 0:
        return 'a'  # Example: Map button at (0,0) to the 'a' key
    elif midi_msg.note == 1:
        return 's'  # Example: Map button at (0,1) to the 's' key
    # Add more mappings as needed
    return None

# Find the MIDI device
input_device = None
for device in mido.get_input_names():
    if midi_device_name in device:
        print("The input device has been found.")
        input_device = device
        break

if not input_device:
    print("MIDI device not found")
else:
    # Open the MIDI device and listen for events
    with mido.open_input(input_device) as inport:
        print("Listening for MIDI events...")
        for msg in inport:
            print("The MIDI message is: ", msg)
            if msg.type == 'note_on':
                key = midi_to_key(msg)
                if key:
                    keyboard.press(key)
            elif msg.type == 'note_off':
                key = midi_to_key(msg)
                if key:
                    keyboard.release(key)

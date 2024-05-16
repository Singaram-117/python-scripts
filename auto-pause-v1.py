import psutil
import pyautogui
import time
import pygetwindow as gw
from pywinauto import Desktop

# List of video player process names and browser process names
VIDEO_PLAYERS = ['vlc', 'mpv', 'potplayer', 'mplayer', 'wmplayer']
BROWSERS = ['chrome', 'firefox', 'msedge', 'brave', 'opera']

TITLES = ['youtube', 'udemy',]

# Function to get the active window's process name and title
def get_active_process_info():
    try:
        active_window = gw.getActiveWindow()
        if active_window:
            window_title = active_window.title.lower()
            app = Desktop(backend='uia').window(handle=active_window._hWnd)
            process_id = app.process_id()
            process = psutil.Process(process_id)
            process_name = process.name().lower()
            return process_name, window_title
    except Exception as e:
        print(f"Error getting active process info: {e}")
    return None, None

# Function to check if any video player or browser with YouTube is the active window
def is_video_playing():
    process_name, window_title = get_active_process_info()
    if process_name:
        # Check if the active window's process is a known video player or browser with YouTube
        if any(player in process_name for player in VIDEO_PLAYERS):
            return True
        if any(browser in process_name for browser in BROWSERS):
            for title in TITLES:
                if title in window_title:
                    return True
    return False

# Function to pause or play Spotify
def control_spotify(action):
    # Simulate media key press to control Spotify
    pyautogui.press('playpause')

# Main function
def main():
    spotify_paused = False

    while True:
        if is_video_playing():
            if not spotify_paused:
                control_spotify('pause')
                spotify_paused = True
                print("Paused Spotify")
        else:
            if spotify_paused:
                control_spotify('play')
                spotify_paused = False
                print("Resumed Spotify")
        
        time.sleep(0.1)  # Adjust the sleep time as needed

if __name__ == "__main__":
    main()

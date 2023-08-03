# Python Keylogger with Email Reporting

## Features

- Captures keystrokes from the keyboard, including normal characters and special keys.
- Periodically sends the collected keystrokes via email to a specified email address using the SMTP server of your choice.
- Handles both plain text and special keys like space.
- Runs in the background and silently captures keystrokes.

## Prerequisites

Before running the keylogger, ensure you have the following:

- Python 3.x installed on your system.
- The `pynput` library installed. You can install it using pip: `pip install pynput`

## Usage

1. Clone the repository to your local machine or download the keylogger script.

2. Open the `keylogger.py` script in a text editor.

3. Replace `"user@gmail.com"` and `"password"` with your email and password for the SMTP server you want to use. Update the server address and port if required. Also, change the email in `send_email()` function to the recipient email address.

4. Save the changes.

5. Open a terminal or command prompt and navigate to the directory where the `keylogger.py` script is located.

6. Run the keylogger script using the following command: `python keylogger.py`

7. The keylogger will start capturing keystrokes and display them on the console.

9. To stop the keylogger, press `Ctrl + C` in the terminal or command prompt.

## Important Notes
- **SMTP Servers**: You can use the SMTP server of your email provider to send the emails. For Gmail, the server address is "smtp.gmail.com" and the port is 587 (STARTTLS). For other providers, you may need to check their documentation for the correct server address and port.

- **SMTP Authentication**: Most SMTP servers require authentication. Make sure to provide the correct email and password for your email account.

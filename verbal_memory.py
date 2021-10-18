# opens and completes the human-benchmark verbal memory test

import os
import pyautogui
import subprocess
import time
import webbrowser

url = 'https://humanbenchmark.com/tests/verbal-memory'

chrome_path = '/usr/bin/google-chrome %s'

webbrowser.get(chrome_path).open(url)

time.sleep(2)  # wait for page to load


def click_seen():
    pyautogui.moveTo(900, 520)
    pyautogui.click()


def click_new():
    pyautogui.moveTo(1050, 520)
    pyautogui.click()


def verbal_memory():

    word_seen = set()

    # move to and click start button
    pyautogui.moveTo(960, 600)
    pyautogui.click()

    for _ in range(2000):  # change to number of words you want
        # get word on screen
        pyautogui.screenshot('word.png', region=(800, 400, 400, 80))
        subprocess.run(['tesseract', 'word.png', 'word-result', '--dpi', '150'])
        with open('word-result.txt', 'r') as file:
            word = file.readline().replace('\n', '')

            if word in word_seen:
                click_seen()
            else:
                word_seen.add(word)
                click_new()

            time.sleep(0.01)  # wait between words

        # cleanup
        os.remove('word-result.txt')
        os.remove('word.png')

    # visually see program done running
    pyautogui.moveTo(100, 100)


verbal_memory()

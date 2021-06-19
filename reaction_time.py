import pyautogui
import time
import webbrowser


url = 'https://humanbenchmark.com/tests/reactiontime'

# Open Website On Linux
chrome_path = '/usr/bin/google-chrome %s'

webbrowser.get(chrome_path).open(url)


# Click to Start
pyautogui.moveTo(320, 400)
time.sleep(2)  # wait for page to load
pyautogui.click()

num_times = 0

while True:

    # Click when green
    if pyautogui.pixel(320, 400).green > 150:
        pyautogui.click()

        num_times += 1
        if num_times == 5:
            # Test runs 5 times
            break

        # Click to start again
        time.sleep(1)
        pyautogui.click()

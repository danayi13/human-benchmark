# human-benchmark
For fun, write scripts that do very well on the human benchmark tests, which can be found here: https://humanbenchmark.com/

## Setup
`pip3 install pyautogui  # Mouse/Keyboard/Screen Control`

`npm install open // js open websites`

`npm install robotjs // equivalent of pyautogui for JS`

`sudo apt install tesseract-ocr // install tesseract on command line (image recognition)`

`sudo apt install libtesseract-dev // not sure if this one is actually necessary`

## To Run
<b>Aim Trainer:</b> `node aim_trainer.js` <br>
<b>Chimp Test:</b> TODO <br>
<b>Number Memory:</b> TODO <br>
<b>Reaction Time (Python [SLOW]):</b> `python3 reaction_time.py` <br>
<b>Reaction Time (JavaScript [FAST]):</b> `node reaction_time.js` <br>
<b>Sequence Memory:</b> TODO <br>
<b>Typing:</b> `python3 typing.py` <br>
<b>Verbal Memory:</b> python3.8 verbal_memory.py <br>
<b>Visual Memory:</b> TODO

## Notes
- Made to run on a Linux (Ubuntu) machine with a 1920x1200 display with Chrome in full-screen

## JavaScript Info
robotjs:
  - Docs: https://github.com/octalmage/robotjs
  - API: https://robotjs.io/docs/syntax
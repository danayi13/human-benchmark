// Opens and completes the reaction time test on the human benchmark

url = "https://humanbenchmark.com/tests/reactiontime"

// Naive sleep function
function sleep(delay) {
    const start = new Date().getTime();
    while (new Date().getTime() < start + delay);
}

function reaction_time() {
    // open website
    const open = require("open");
    open(url);

    // mover and clicker
    const robot = require("robotjs");

    let num = 0; // number of tests completed

    // wait for page to load
    setTimeout(function () {
        // click to start
        robot.dragMouse(320, 400);
        robot.mouseClick();

        while (true) {
            // click when green
            if (robot.getPixelColor(320, 400) == "4bdb6a") {
                robot.mouseClick();

                if (++num == 5) {
                    return;
                }

                // wait for prompt to keep going
                sleep(1000);
                robot.mouseClick();
            }
        }
    }, 2000);
}

reaction_time();
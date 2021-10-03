// Opens and completes the aim trainer test on the human benchmark

url = "https://humanbenchmark.com/tests/aim"

function aim_trainer() {

    // open website
    const open = require("open");
    open(url);

    // boundaries
    const left_x = 450;
    const right_x = 1470;
    const top_y = 250;
    const bottom_y = 640;

    // size of "squares" to check
    // NOTE: bigger = faster but more likely to not see a target
    //       smaller = slower but less likely to miss a target
    const pixel_increment = 35;

    // mover and clicker
    const robot = require("robotjs");

    // colors to check for
    const yellow = "ffd154"; // done button
    const target = "95c3e8";

    // wait for page to load
    setTimeout(function () {
        // click to start
        robot.dragMouse(950, 450);
        robot.mouseClick();

        while (true) {
            for (let i = left_x; i < right_x; i += pixel_increment) {
                for (let j = top_y; j < bottom_y; j += pixel_increment) {
                    if (robot.getPixelColor(i, j) == target) {
                        robot.dragMouse(i, j);
                        robot.mouseClick();

                        // stop when "save score" shows up
                        if (robot.getPixelColor(925, 600) == yellow) {
                            return;
                        }
                    }
                }

                // stop when "save score" shows up
                if (robot.getPixelColor(925, 600) == yellow) {
                    return;
                }
            }
        }
    }, 2000);

}

aim_trainer();
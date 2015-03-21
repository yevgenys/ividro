(function (win, doc) {

    "use strict";

    var main = doc.getElementById("loading"),
        mainCtx = main.getContext("2d"),
        sub = doc.createElement("canvas"),
        subCtx = sub.getContext("2d"),
        i = 0,
        WIDTH = 250,
        HEIGHT = 50,
        SIZE = 5,
        INTERVAL = 5;

    main.width = sub.width = WIDTH;
    main.height = sub.height = HEIGHT;

    build(0);

    setInterval(function () {
        main.width = WIDTH;
        mainCtx.font = "30px AvenirNext-Heavy";
        mainCtx.fillText("HELLO WORLD.", 0, 30);
        mainCtx.globalCompositeOperation = "destination-in";
        mainCtx.drawImage(sub, 0, 0);
    }, 1000 / 24);

    function build(i) {
        var height = HEIGHT / SIZE,
            max = (i + 1 < height) ? (i + 1) : height;

        (function setRect(j) {
            if (j < max) {
                subCtx.rect((i - j) * SIZE, j * SIZE, SIZE, SIZE);
                subCtx.fill();
                setTimeout(function () {
                    setRect(++j);
                }, INTERVAL);
            } else {
                if ((i - HEIGHT / SIZE) * SIZE < win.innerWidth) {
                    build(++i);
                }
            }
        })(0);
    }

})(this, document);